# DemandForecast AI

[![CI](https://github.com/dudxzz-25/demandforecast-ai/actions/workflows/ci.yml/badge.svg)](https://github.com/dudxzz-25/demandforecast-ai/actions/workflows/ci.yml)

Projeto de **previsão de demanda mensal** que compara um baseline simples com modelos supervisionados usando features temporais, lags e média móvel.

## 🎯 Objetivo

Avaliar se modelos de Machine Learning conseguem superar um baseline de média móvel em um cenário de demanda por produto.

## 🛠️ Stack

**Python · Pandas · scikit-learn · SQLite · SQL**

## ⚙️ Feature engineering

O pipeline cria:

- mês do ano;
- índice temporal;
- indicador de promoção;
- `lag_1`, `lag_2` e `lag_3`;
- média móvel dos 3 períodos anteriores.

A separação entre treino e teste respeita a ordem temporal dos dados.

## 📊 Resultados atuais

| Modelo | MAE | RMSE |
|---|---:|---:|
| Linear Regression | **63,49** | **79,47** |
| Random Forest | 80,57 | 95,92 |
| Moving Average 3 | 134,54 | 161,36 |

Neste conjunto, a **Regressão Linear** apresentou o menor erro absoluto médio e superou o baseline de média móvel.

> Os dados são sintéticos e foram criados para estudo e demonstração técnica.

## 📂 Estrutura

```text
demandforecast-ai/
├── data/
│   ├── raw/
│   └── output/
├── scripts/generate_data.py
├── sql/analysis.sql
├── src/forecast.py
├── tests/test_forecast.py
├── requirements.txt
└── README.md
```

## ▶️ Como executar

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/generate_data.py
python src/forecast.py
```

Saídas em `data/output/`:

- `metrics.csv`
- `predictions.csv`
- `forecast.db`

### Testes

```bash
python -m unittest discover -s tests -v
```

## 🧠 O que este projeto demonstra

- séries temporais e prevenção de leakage;
- criação de lags e médias móveis;
- comparação contra baseline;
- avaliação com MAE e RMSE;
- persistência de previsões e métricas em SQLite.

## ⚠️ Limitações

O projeto não utiliza modelos específicos de séries temporais, intervalos de confiança, variáveis externas complexas ou backtesting em múltiplas janelas. A proposta é demonstrar uma abordagem simples, reproduzível e comparável.

---

Desenvolvido por **Eduardo de Toledo Dias**.

[Portfólio](https://dudxzz-25.github.io/portfolio-web/) · [GitHub](https://github.com/dudxzz-25) · [LinkedIn](https://www.linkedin.com/in/eduardo-de-toledo-dias-880b9834b/)