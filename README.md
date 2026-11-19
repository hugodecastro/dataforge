# ⚡ DataForce — End-to-End AI & Modern Data Stack Analytics

![Apache Spark](https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)

O **DataForce** é uma plataforma analítica de ponta a ponta (*End-to-End*) projetada para transformar grandes volumes de avaliações de clientes (*reviews*) não estruturadas em insights acionáveis de negócio.

O projeto integra engenharia de dados em larga escala (**Apache Spark**), armazenamento em nuvem (**Snowflake**), modelagem analítica (**dbt**), enriquecimento semântico com **Inteligência Artificial** e visualização interativa em **React**.

---

## 🏛️ Arquitetura do Sistema

O fluxo de dados segue a arquitetura de **Modern Data Stack** combinada com uma camada de enriquecimento por IA:

```text
[ Dataset Bruto (JSON / CSV) ]
            │
            ▼
  1. Apache Spark (PySpark)   ──► Ingestão, limpeza pesada e carga na camada RAW
            │
            ▼
  2. Snowflake (Cloud DW)     ──► Armazenamento escalável (RAW ➔ STAGING ➔ MARTS)
            │
            ▼
  3. dbt (Analytics Eng.)     ──► Transformações SQL, testes de qualidade e linhagem
            │
            ▼
  4. Inteligência Artificial  ──► Análise de sentimento e resumos executivos (LLMs)
            │
            ▼
  5. Backend API (FastAPI)    ──► Exposição dos dados consolidados via REST
            │
            ▼
  6. Frontend (React + Vite)  ──► Dashboard interativo com gráficos e filtros
```

---

## 🛠️ Stack Tecnológica & Responsabilidades

* **Engenharia de Dados (`1_ingestion_spark`):** Processamento distribuído com **PySpark** para leitura de datasets volumosos, tratamento de valores nulos, tipagem e escrita no Snowflake via conector oficial.
* **Data Warehouse (`Snowflake`):** Repositório central de dados em nuvem, isolando dados brutos (`RAW`) das tabelas analíticas finais (`ANALYTICS`).
* **Analytics Engineering (`2_transformation_dbt`):** Modelagem modular em SQL com **dbt**, incluindo testes automatizados (`not_null`, `unique`, `accepted_values`) e documentação de linhagem (*Data Lineage*).
* **Inteligência Artificial (`3_ai_enrichment`):** Pipeline Python que consome os dados tratados no Snowflake, aplica modelos de NLP/LLMs para classificar sentimentos e gera resumos executivos sobre pontos fortes e fracos de cada produto.
* **API REST (`4_backend_api`):** Construída com **FastAPI**, servindo como ponte segura e performática entre o Snowflake e a interface web.
* **Frontend (`5_frontend_react`):** Single Page Application (SPA) desenvolvida em **React**, estilizada com **Tailwind CSS** e equipada com gráficos interativos (**Recharts**).

---

## 📁 Estrutura do Repositório

```text
dataforce/
├── .env.example                  # Modelo de variáveis de ambiente
├── .gitignore                    # Arquivos ignorados pelo Git
├── README.md                     # Documentação do projeto
├── data/                         # Amostras locais de datasets para desenvolvimento
├── 1_ingestion_spark/            # Jobs PySpark para ingestão no Snowflake (RAW)
├── 2_transformation_dbt/         # Modelos SQL (Staging & Marts) e testes de qualidade
├── 3_ai_enrichment/              # Scripts de NLP, prompts e integração com LLMs
├── 4_backend_api/                # API REST em FastAPI conectada ao Snowflake
└── 5_frontend_react/             # Aplicação web e componentes de dashboard
```

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Python 3.10+ e Java 11/17 (necessário para o Apache Spark)
* Node.js 18+ e npm/yarn
* Uma conta ativa no **Snowflake** (o *Free Trial* de 30 dias é suficiente)
* Chave de API de um provedor de IA (ex: Google Gemini API ou OpenAI)

### 1. Configuração Inicial
Clone o repositório e configure as variáveis de ambiente:

```bash
git clone https://github.com/seu-usuario/dataforce.git
cd dataforce
cp .env.example .env
# Preencha o arquivo .env com suas credenciais do Snowflake e da API de IA
```

### 2. Ingestão de Dados (Apache Spark)
```bash
cd 1_ingestion_spark
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python jobs/ingest_reviews.py
```

### 3. Transformação e Testes (dbt)
```bash
cd ../2_transformation_dbt
pip install dbt-snowflake
dbt debug   # Verifica a conexão com o Snowflake
dbt run     # Executa os modelos Staging e Marts
dbt test    # Valida a integridade dos dados
```

### 4. Enriquecimento com IA
```bash
cd ../3_ai_enrichment
pip install -r requirements.txt
python main.py
```

### 5. Backend API (FastAPI)
```bash
cd ../4_backend_api
pip install -r requirements.txt
uvicorn app.main:app --reload
# A documentação interativa estará disponível em http://localhost:8000/docs
```

### 6. Frontend Dashboard (React)
```bash
cd ../5_frontend_react
npm install
npm run dev
# Acesse a aplicação em http://localhost:5173
```

---

## 📈 Funcionalidades do Dashboard

* **KPIs Consolidados:** Total de avaliações processadas, média geral de satisfação e taxa de sentimento positivo.
* **Análise de Sentimento:** Gráficos comparativos mostrando a evolução e distribuição das opiniões por categoria.
* **Resumo Executivo por IA:** Painel dinâmico que sintetiza centenas de comentários de um produto em 3 tópicos principais de elogios e pontos de melhoria.
* **Exploração Granular:** Tabela pesquisável com filtros por nota, sentimento e categoria.

---

## 🔮 Próximos Passos (Roadmap)

* [ ] Adicionar orquestração automatizada do pipeline utilizando **Apache Airflow** ou **Prefect**.
* [ ] Implementar ingestão contínua via **Spark Structured Streaming**.
* [ ] Adicionar containerização completa com `docker-compose.yml`.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.