# PRODUCT REQUIREMENT DOCUMENTS (PRD)-DataSense AI
## 1. Problem Statement
Data Analyst lose hours translating raw CSV files into executive summaries and SQL queries. The General LLM hallucinates and cannot do exact computation,non-technical teams can also not contruct a robust prompt to the LLM.
## 2. Target User Persona
* **Primary Persona** Lucky Linda (Business Intelligence Analyst)- Needs fast, natural language summaries of the dataset that they can present to the stakeholders without writing complex codes manually.
## 3. Product Features and User Stories
* **Data Summaries & Quality Profiler**
* *User Story 1*: As a BI analyst, I want to upload a CSV or Excel file (.xlsx, .xls), or paste a Google Sheets link, so that i can get the exact metric counts and the data trends instantly.
* *Supported Data Sources*:
  * **CSV** (.csv)
  * **Excel** (.xlsx, .xls) - with a sheet picker for workbooks that have multiple sheets
  * **Google Sheets** - via a share link; the sheet must be shared as "Anyone with the link can view"
* *Text-to-SQL 2* :As an Analyst, I want to ask questions a plain English so that i can receive a valid SQL queries with explanation.

## 4. Key Performance Indicators
* **Response Speed**: Delivers insights within 3 seconds.

