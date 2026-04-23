import pandas as pd


def processar_xlsx_intermedica(caminho):
    dados = []
    try:
        # ler planilha com cabeçalho correto
        df = pd.read_excel(caminho, header=17)

        # pegar data pagamento (fica no topo do arquivo)
        df_topo = pd.read_excel(caminho, header=None)
        data_pagamento = None

        for i, row in df_topo.iterrows():
            for val in row:
                if isinstance(val, str) and "Previsão Pagamento" in val:
                    try: 
                        data_pagamento = df_topo.iloc[i+1, row.index(val)]
                    except Exception as eror:
                        #print('Erro de index', eror)
                        continue
                    break

        for _, row in df.iterrows():
            guia = row.get("Autorizacao")

            if pd.isna(guia):
                continue

            valor_pago = row.get("Valor Pago", 0)
            valor_glosa = row.get("Valor Glosado", 0)
            motivo = row.get("Motivos Glosa", "")

            dados.append({
                "convenio": "INTERMEDICA",
                "protocolo": "",
                "senha": str(guia).replace(".0", "").strip(),
                "valor_pago": float(valor_pago.replace(',', '.')),
                "glosa": float(valor_glosa.replace(',', '.')),
                "motivo_glosa": motivo,
                "data_pagamento": data_pagamento
            })
    except:
        pass

    return dados
