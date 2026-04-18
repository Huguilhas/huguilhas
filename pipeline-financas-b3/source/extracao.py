import yfinance as yf
import pandas as pd
from datetime import datetime
import os

ACOES = ["PETR4.SA", "VALE3.SA", "ITUB4.SA", "BBDC4.SA", "WEGE3.SA"]

def extracao(acoes: list, periodo: str = "1y") -> pd.DataFrame:
    print(f"Extraindo Dados Para: {acoes}")
    df = yf.download(acoes, period=periodo)
    
    caminho_de_saida = f"data/bronze/raw_{datetime.today().date()}.csv"
    
    #Cria a Pasta se Ela Não Existir
    os.makedirs("data/bronze", exist_ok=True)
    
    df.to_csv(caminho_de_saida)
    
    print(f"Extraindo {len(df)} Registros")
    print(f"Salvo em {caminho_de_saida}")
    
    return df

if __name__ == "__main__":
    extracao(ACOES)
