# 📊 Sistema de Processamento de Faturamento Hospitalar

🇺🇸 Clinical Billing Data Processing System

---

**Visão Geral | Overview**

🇧🇷 Projeto desenvolvido para automatizar a leitura e conciliação de arquivos de pagamento de operadoras de saúde, atualizando automaticamente uma planilha de faturamento e alimentando dashboards analíticos.

🇺🇸 Project developed to automate the processing and reconciliation of healthcare billing files, updating a structured spreadsheet and feeding analytical dashboards.

---

**Objetivo | Objective**

🇧🇷 Automatizar a conferência de faturamento, reduzindo drasticamente o tempo operacional.

🇺🇸 Automate billing reconciliation, reducing manual work and improving reliability.

---

**Como Funciona | How It Works**

🇧🇷

* Leitura de arquivos CSV, Excel e XML
* Identificação automática da operadora
* Processamento específico por tipo de arquivo
* Atualização da planilha de faturamento

🇺🇸

* Reads CSV, Excel and XML files
* Identifies provider automatically
* Uses specific processors
* Updates billing spreadsheet

---

**Estrutura de Entrada | Input Structure**

```
arquivos/
├── CSV/
├── EXCEL/
└── XML/
```

---

**Planilha de Faturamento | Billing Spreadsheet**

🇧🇷 A planilha principal deve conter a aba **FATURADO**.

Exemplo:

```
C:\Projeto Conciliação de Pagamentos\Clínica\FATURAMENTO 2026.xlsx
```

🇺🇸 Main spreadsheet must include the **FATURADO** sheet.

---

**Dashboard (Power BI)**

🇧🇷 O arquivo `Dashboard.pbix` consome dados da pasta:

```
Planilhas/
```

🇺🇸 The `Dashboard.pbix` reads data from:

```
Planilhas/
```

---

**Logs e Tratamento de Erros | Logs & Error Handling**

🇧🇷

* Registros encontrados → atualizados automaticamente
* Registros não encontrados → enviados para log

📁 Pasta:

```
logs/
```

🇺🇸

* Found records → updated
* Not found → logged

---

**Tecnologias | Technologies**

* Python
* Tkinter
* Pandas
* OpenPyXL
* Power BI

---

**Como Usar | How to Use**

🇧🇷

1. Inserir arquivos nas pastas (`CSV`, `EXCEL`, `XML`)
2. Informar a planilha
3. Executar o sistema
4. Verificar resultados e logs

🇺🇸

1. Place files in folders
2. Provide spreadsheet
3. Run system
4. Check results

---

**Segurança | Data Security**

🇧🇷 Dados anonimizados e uso exclusivo para portfólio.

🇺🇸 Data anonymized for portfolio use.

---

**Créditos | Credits**

Projeto desenvolvido em parceria com **LS Treinamentos**.
