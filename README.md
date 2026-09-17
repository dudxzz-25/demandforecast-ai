# DemandForecast AI

Sistema de previsão de demanda mensal que compara um **baseline de média móvel**, Regressão Linear e Random Forest usando features temporais e lags.

## Stack
Python, Pandas, scikit-learn, SQLite e SQL.

## Execução
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/generate_data.py
python src/forecast.py
```

## Testes
```bash
python -m unittest discover -s tests -v
```
