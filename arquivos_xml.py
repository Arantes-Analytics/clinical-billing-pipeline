import xml.etree.ElementTree as ET
from datetime import datetime
from tools import identificar_convenio


def processar_xml(caminho_xml):
    '''
    # CÉLULA 4 - PROCESSAR XML
    '''
    try:
        tree = ET.parse(caminho_xml)
        root = tree.getroot()
        ns = {'ans': 'http://www.ans.gov.br/padroes/tiss/schemas'}
        dados_extraidos = []

        # 🔹 pegar data real de pagamento
        data_pagamento_tag = root.find(".//ans:dataPagamento", ns)
        data_pagamento = data_pagamento_tag.text if data_pagamento_tag is not None else None
        data_pagamento = datetime.strptime(data_pagamento, "%Y-%m-%d").strftime("%d/%m/%Y")
        protocolos = root.findall(".//ans:relacaoProtocolos", ns)
        convenio = identificar_convenio(root.find('.//ans:nomeOperadora', ns).text)

        for protocolo in protocolos:
            numero_protocolo_tag = protocolo.find("ans:numeroProtocolo", ns)
            # data_protocolo_tag = protocolo.find("ans:dataProtocolo", ns)

            if numero_protocolo_tag is None:
                continue

            numero_protocolo = numero_protocolo_tag.text
            # data_pagamento = data_protocolo_tag.text if data_protocolo_tag is not None else None

            guias = protocolo.findall(".//ans:guiasDoLote", ns)

            for guia in guias:

                numero_guia_tag = guia.find("ans:numeroGuiaPrestador", ns)
                valor_liberado_tag = guia.find("ans:valorLiberadoGuia", ns)
                valor_glosa_tag = guia.find("ans:valorGlosaGuia", ns)

                if numero_guia_tag is None:
                    continue

                numero_guia = numero_guia_tag.text

                dados_extraidos.append({
                    "convenio": convenio,
                    "guia": numero_guia,
                    "protocolo": numero_protocolo,
                    "valor_pago": float(valor_liberado_tag.text.replace(',', '.')) if valor_liberado_tag is not None else 0,
                    "glosa": float(valor_glosa_tag.text.replace(',', '.')) if valor_glosa_tag is not None else 0,
                    "data_pagamento": data_pagamento
                })

        return dados_extraidos

    except Exception as e:
        print("Erro ao processar XML:", e)
