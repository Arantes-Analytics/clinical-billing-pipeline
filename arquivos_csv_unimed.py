import pandas as pd
from tools import identificar_convenio


def processar_csv_unimed(caminho_csv):
    convenio = identificar_convenio(caminho_csv)

    # LEITURA ROBUSTA DO CSV
    df = pd.read_csv(
        caminho_csv,
        sep=None,           # detecta separador automaticamente
        engine="python",
        encoding="latin1",
        dtype=str
    )

    # limpar nomes das colunas
    df.columns = df.columns.str.strip().str.replace("\ufeff", "")

    # verificar se coluna existe
    if "Cod.Doc.Prest." not in df.columns:
       # print("❌ Coluna Cod.Doc.Prest. não encontrada!")
        return []
    
    # LIMPEZA DOS DADO
    df["Cod.Doc.Prest."] = (
        df["Cod.Doc.Prest."]
        .astype(str)
        .str.replace(",", ".", regex=False)
        .str.strip()
    )

    df["Valor Pago"] = (
        df["Valor Pago"]
        .astype(str)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
    )

    df["Valor Glosa"] = (
        df["Valor Glosa"]
        .astype(str)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
    )

    df["Glosa"] = df["Glosa"].astype(str).str.strip()

    df["Valor Pago"] = pd.to_numeric(df["Valor Pago"], errors="coerce").fillna(0)
    df["Valor Glosa"] = pd.to_numeric(df["Valor Glosa"], errors="coerce").fillna(0)

    # AGRUPAR POR GUIA (Cod.Doc.Prest.)
    df_agrupado = df.groupby("Cod.Doc.Prest.", as_index=False).agg({
        "Valor Pago": "sum",
        "Valor Glosa": "sum",
        "Glosa": lambda x: " | ".join(x.dropna().unique())
    })

    dados_extraidos = []

    for _, linha in df_agrupado.iterrows():
        guia = str(linha["Cod.Doc.Prest."]).strip()

        valor_pago = linha["Valor Pago"]
        valor_glosa = linha["Valor Glosa"]
        motivo_glosa = linha["Glosa"]

        dados_extraidos.append({
            "convenio": convenio,
            "guia": guia,
            "protocolo": "",
            "valor_pago": valor_pago,
            "glosa": valor_glosa,
            "motivo_glosa": motivo_glosa,
            "data_pagamento": None
        })

    return dados_extraidos
