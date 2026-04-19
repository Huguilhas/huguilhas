# Pipeline de Cotacoes B3

pipeline de dados para coleta, tratamento e analise de cotacoes da b3, seguindo a arquitetura medalion

---
![Python](https://img.shields.io/badge/python-3.11-blue)
![dbt](https://img.shields.io/badge/dbt-core-orange)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![yfinance](https://img.shields.io/badge/yfinance-1.3.0-yellow)
![Pandas](https://img.shields.io/badge/pandas-2.x-150458?logo=pandas&logoColor=white)
![DuckDB](https://img.shields.io/badge/duckdb-yellow?logo=duckdb&logoColor=black)
![Airflow](https://img.shields.io/badge/airflow-2.x-017CEE?logo=apacheairflow&logoColor=white)
![Streamlit](https://img.shields.io/badge/streamlit-red?logo=streamlit&logoColor=white)

# Arquitetura
![arquitetura](arquitetura.png)

## 🗒️Stack
- **yfinance** — coleta de cotações da B3
- **pandas** — manipulação dos dados
- **dbt + DuckDB** — transformação em camadas bronze/silver/gold
- **Apache Airflow** — orquestração e agendamento do pipeline
- **Streamlit** — visualização dos dados

## Arquitetura
`yfinance` → `bronze (raw)` → `silver (limpo)` → `gold (analítico)` → `Streamlit`

## **Passo a Passo**
### 1. Criar venv
```bash
 python -m venv venv  
 venv\Scripts\activate
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

### 3. Extrair dados
```bash
python source/extracao.py
```