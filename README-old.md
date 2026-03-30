# tag-functions

functions firebase

# Setup Firebase Functions

```bash
firebase init functions
cd functions
.\venv\Scripts\activate
python -m pip install firebase-functions firebase-admin
python -m pip install --upgrade pip
python -c "import firebase_functions; print('Firebase pronto!')"
```

# Load var

```bash
get-content .env | foreach {
    $name, $value = $_.split('=')
    set-content env:\$name $value
    echo $name $value
}
```

# Run locally

```bash
Stop-Process -Id (Get-NetTCPConnection -LocalPort 4400).OwningProcess -Force
firebase emulators:start --only functions
```

# Teste Verificar Login

```bash
$url = "http://127.0.0.1:5001/llm-studies/us-central1/verificar_login"
$url_nuvem = "https://verificar-login-3hqo37xxza-uc.a.run.app"
$body = @{ email = "lquissakng@gmail.com" } | ConvertTo-Json
Invoke-RestMethod -Uri $url -Method Post -ContentType "application/json" -Body $body
Invoke-RestMethod -Uri $url_nuvem -Method Post -ContentType "application/json" -Body $body
```

# Teste Chat

```bash
$url_chat = "http://127.0.0.1:5001/llm-studies/us-central1/chat"
$body_chat = @{
    query = "Como estão os dados no BigQuery?";
    session_id = "lquissak_teste"
} | ConvertTo-Json

Invoke-RestMethod -Uri $url_chat -Method Post -ContentType "application/json" -Body $body_chat
```

# Deploy

```bash
functions\venv\Scripts\activate
pip freeze > .\functions\requirements.txt
firebase deploy --only functions
```

# Local venv

```bash
py -m venv .local_venv
.local_venv\scripts\activate
pip install google-auth google-auth-oauthlib google-auth-httplib2
```

# Agent tests

```bash
python -m pytest
python tests\call_data_agent_client.py
gcloud projects add-iam-policy-binding llm-studies --member="serviceAccount:firebase-adminsdk-fbsvc@llm-studies.iam.gserviceaccount.com" --role="roles/aiplatform.user"
gcloud auth application-default print-access-token
curl -H "Authorization: Bearer " https://geminidataanalytics.googleapis.com/v1beta/projects/llm-studies/locations/us-central1/dataAgents/ga_data_agent
```

# Links

- [Cloud Firestore](https://console.firebase.google.com/project/llm-studies/firestore/databases/-default-/data/~2Fusuarios_autorizados)
