import csv
import re


def processar_csv_bradesco(caminho_csv):
    convenio = "BRADESCO"
    dados_extraidos = []
    data_pagamento = None

    with open(caminho_csv, "r", encoding="latin1") as f:
        leitor = csv.reader(f, delimiter=";")
        for linha in leitor:
            if not linha:
                continue

            # CAPTURAR DATA PAGAMENTO
            if "Liberado para cr" in linha[0]:
                match = re.search(r"\d{2}/\d{2}/\d{4}", linha[0])
                if match:
                    data_pagamento = match.group()
                continue

            # IGNORAR CABEÇALHO
            if "Doc Original" in linha:
                continue

            # LINHA COM GUIA
            if len(linha) > 9 and linha[7].strip() != "":

                guia = linha[7].strip()
                valor = linha[9].replace(".", "").replace(",", ".").strip()
                justificativa = ""

                if len(linha) > 10:
                    justificativa = linha[10].strip()

                try:
                    valor = float(valor)
                except:
                    valor = 0

                dados_extraidos.append({
                    "convenio": convenio,
                    "guia": guia,
                    "protocolo": "",
                    "valor_pago": valor,
                    "glosa": 0,
                    "motivo_glosa": justificativa,
                    "data_pagamento": data_pagamento
                })

    return dados_extraidos