# 🏷️ Tag Functions - Firebase & AI Integration

Este repositório contém um conjunto de **Cloud Functions (Firebase)** desenvolvidas em Python, focadas em integração com LLMs, autenticação e análise de dados no Google Cloud Platform (GCP).

## 🚀 O que este projeto faz?

O projeto serve como um backend serverless para:
* **Gestão de Sessão e Login:** Verificação de usuários autorizados via Firestore.
* **Interface de Chat:** Endpoint configurado para interagir com modelos de linguagem (LLMs).
* **Análise de Dados:** Integração com BigQuery para consultas de dados via agentes de IA.
* **Agentes de Dados:** Testes e implementação de `Data Agents` (Gemini) para automação de analytics.

## 🛠️ Stack Tecnológica
* **Linguagem:** Python 3.10+
* **Infraestrutura:** Firebase Functions & Google Cloud Run
* **Banco de Dados:** Cloud Firestore & BigQuery
* **IA:** Gemini (AI Platform / Vertex AI)

## 📂 Estrutura do Repositório
* `/functions`: Contém a lógica principal das funções e o `main.py`.
* `/tests`: Scripts de teste para chamadas de API e validação de agentes.
* `/rules`: Configurações de segurança do Firestore.
* `/clients`: Exemplos de como consumir as funções.

## 🔧 Como Testar Localmente
Certifique-se de ter o Firebase CLI instalado e o ambiente virtual configurado:
```bash
cd functions
.\venv\Scripts\activate
firebase emulators:start --only functions