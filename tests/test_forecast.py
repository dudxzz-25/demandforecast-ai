import sys, unittest
from pathlib import Path
import pandas as pd
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src.forecast import feature_engineering
class TestFeatures(unittest.TestCase):
    def test_lags(self):
        df=pd.DataFrame({"product_id":[1]*6,"month":pd.date_range("2026-01-01",periods=6,freq="MS"),"promotion":[0]*6,"demand":[10,20,30,40,50,60]})
        out=feature_engineering(df)
        self.assertEqual(out.iloc[0].lag_1,30)
        self.assertEqual(out.iloc[0].rolling_3,20)
if __name__=="__main__": unittest.main()
