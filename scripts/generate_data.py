from pathlib import Path
import math, random
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"data"/"raw"; OUT.mkdir(parents=True,exist_ok=True)
random.seed(42)
months=pd.date_range("2021-01-01","2026-08-01",freq="MS")
rows=[]
for product_id,base in [(1,900),(2,650),(3,420)]:
    for i,d in enumerate(months):
        trend=i*7
        season=120*math.sin(2*math.pi*(d.month-1)/12)
        promo=1 if d.month in (5,11) else 0
        demand=max(50,round(base+trend+season+promo*180+random.gauss(0,55)))
        rows.append([product_id,d.strftime("%Y-%m-%d"),promo,demand])
pd.DataFrame(rows,columns=["product_id","month","promotion","demand"]).to_csv(OUT/"monthly_demand.csv",index=False)
print("Rows:",len(rows))
