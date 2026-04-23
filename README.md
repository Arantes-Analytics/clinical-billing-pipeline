# 📊 Sistema de Processamento de Faturamento Hospitalar
# 📊 Clinical Billing Data Processing System

---
🇧🇷 Visão Geral
Projeto desenvolvido para automatizar a leitura e conciliação de arquivos de pagamento de operadoras de saúde (convênios), atualizando automaticamente uma planilha de faturamento e alimentando dashboards analíticos.
---
🇺🇸 Overview
Project developed to automate the processing and reconciliation of healthcare billing files from insurance providers, updating a structured billing spreadsheet and feeding analytical dashboards.
---

🚀 Objetivo | Objective
🇧🇷
Automatizar o processo de conferência de faturamento, reduzindo drasticamente o tempo operacional e aumentando a confiabilidade dos dados.

🇺🇸
Automate billing reconciliation, drastically reducing manual work and improving data reliability.
---

🧠 Como Funciona | How It Works
🇧🇷
* Leitura de arquivos CSV, Excel e XML
* Identificação automática da operadora
* Processamento específico por tipo de arquivo
* Atualização da planilha de faturamento

🇺🇸
* Reads CSV, Excel and XML files
* Automatically identifies the provider
* Uses specific processors for each format
* Updates the billing spreadsheet
---

📂 Estrutura de Entrada | Input Structure
```
arquivos/
├── CSV/
├── EXCEL/
└── XML/
```
🇧🇷
Cada pasta deve conter apenas arquivos do tipo correspondente.

🇺🇸
Each folder must contain only files of its respective type.
---

📄 Planilha de Faturamento | Billing Spreadsheet
🇧🇷
A planilha principal deve ser informada no sistema e conter a aba:
* FATURADO

📍 Exemplo:
```
C:\Projeto Conciliação de Pagamentos\Clínica\FATURAMENTO 2026.xlsx
```

🇺🇸
The main spreadsheet must be provided in the system and contain the sheet:
* FATURADO
---

📊 Dashboard (Power BI)
🇧🇷
O arquivo `Dashboard.pbix` consome dados da pasta:

```
Planilhas/
```
Permite:

* Análise financeira
* Identificação de glosas
* Indicadores automatizados

🇺🇸
The `Dashboard.pbix` file reads data from:

```
Planilhas/
```
Provides:

* Financial analysis
* Glosa (denials) tracking
* Pre-built indicators
---

🧾 Logs e Tratamento de Erros | Logs & Error Handling
🇧🇷
O sistema gera logs automaticamente quando registros não são encontrados na planilha.

📁 Local:
```
logs/
```

📌 Funcionamento:
* ✔ Registro encontrado → atualizado automaticamente
* ❌ Registro não encontrado → enviado para log

Objetivo:
* Auditoria
* Conferência manual
* Correção de inconsistências
---

🇺🇸
The system generates logs when records are not found in the billing spreadsheet.

📁 Location:
```
logs/
```

📌 Behavior:
* ✔ Found → automatically updated
* ❌ Not found → written to log

Purpose:
* Auditing
* Manual validation
* Data correction
---

🛠️ Tecnologias | Technologies

* Python
* Tkinter
* Pandas
* OpenPyXL
* Power BI
---

▶️ Como Usar | How to Use
🇧🇷
1. Insira os arquivos nas pastas:
   * `CSV`, `EXCEL`, `XML`
2. Informe a planilha de faturamento
3. Execute o sistema
4. Verifique a planilha e os logs
---

🇺🇸
1. Place files in folders:
   * `CSV`, `EXCEL`, `XML`
2. Provide the billing spreadsheet
3. Run the system
4. Check updated data and logs
---

🔒 Segurança | Data Security
🇧🇷
* Dados reais foram removidos
* Informações anonimizadas
* Uso exclusivo para portfólio

🇺🇸
* Real data removed
* All information anonymized
* Portfolio use only
---

👥 Créditos | Credits
🇧🇷
Projeto desenvolvido em parceria com a **LS Treinamentos**.

🇺🇸
Project developed in partnership with **LS Treinamentos**.
---

💡 Diferenciais | Highlights

* Automação de processo crítico
* Redução de tempo operacional
* Estrutura escalável
* Integração com BI
* Geração de logs para auditoria
---

📈 Impacto | Impact
🇧🇷
Projeto demonstra aplicação prática de engenharia de dados e automação.

🇺🇸
Demonstrates real-world data engineering and automation application.
---

