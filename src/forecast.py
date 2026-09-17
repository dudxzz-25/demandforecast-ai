from pathlib import Path
import sqlite3
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/"data"/"raw"/"monthly_demand.csv"
OUT=ROOT/"data"/"output"; OUT.mkdir(parents=True,exist_ok=True)
FEATURES=["product_id","month_number","time_index","promotion","lag_1","lag_2","lag_3","rolling_3"]


def feature_engineering(df):
    x=df.copy(); x["month"]=pd.to_datetime(x["month"]); x=x.sort_values(["product_id","month"])
    x["month_number"]=x["month"].dt.month
    x["time_index"]=(x["month"].dt.year-x["month"].dt.year.min())*12+x["month"].dt.month
    g=x.groupby("product_id")["demand"]
    x["lag_1"]=g.shift(1); x["lag_2"]=g.shift(2); x["lag_3"]=g.shift(3)
    x["rolling_3"]=g.transform(lambda s:s.shift(1).rolling(3).mean())
    return x.dropna().reset_index(drop=True)


def evaluate_models(df):
    cutoff=df["month"].max()-pd.DateOffset(months=8)
    train=df[df["month"]<=cutoff]; test=df[df["month"]>cutoff].copy()
    baseline=test["rolling_3"]
    models={"linear_regression":LinearRegression(),"random_forest":RandomForestRegressor(n_estimators=250,max_depth=8,random_state=42,n_jobs=-1)}
    metrics=[]; predictions={"moving_average_3":baseline.values}
    metrics.append({"model":"moving_average_3","mae":mean_absolute_error(test.demand,baseline),"rmse":mean_squared_error(test.demand,baseline)**0.5})
    for name,model in models.items():
        model.fit(train[FEATURES],train["demand"]); pred=model.predict(test[FEATURES]); predictions[name]=pred
        metrics.append({"model":name,"mae":mean_absolute_error(test.demand,pred),"rmse":mean_squared_error(test.demand,pred)**0.5})
    for name,pred in predictions.items(): test[f"pred_{name}"]=pred
    metrics=pd.DataFrame(metrics).round(2).sort_values("mae")
    return metrics,test


def main():
    df=feature_engineering(pd.read_csv(RAW))
    metrics,preds=evaluate_models(df)
    metrics.to_csv(OUT/"metrics.csv",index=False); preds.to_csv(OUT/"predictions.csv",index=False,date_format="%Y-%m-%d")
    with sqlite3.connect(OUT/"forecast.db") as conn:
        metrics.to_sql("model_metrics",conn,if_exists="replace",index=False)
        preds.assign(month=preds.month.dt.strftime("%Y-%m-%d")).to_sql("predictions",conn,if_exists="replace",index=False)
    print(metrics.to_string(index=False))

if __name__=="__main__": main()
