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

# Run locally

```bash
Stop-Process -Id (Get-NetTCPConnection -LocalPort 4000).OwningProcess -Force
firebase emulators:start --only functions
```

# Teste

```bash
$url = "http://127.0.0.1:5001/llm-studies/us-central1/verificar_login"
$url_nuvem = "https://verificar-login-3hqo37xxza-uc.a.run.app"
$body = @{ email = "lquissakng@gmail.com" } | ConvertTo-Json
Invoke-RestMethod -Uri $url -Method Post -ContentType "application/json" -Body $body
Invoke-RestMethod -Uri $url_nuvem -Method Post -ContentType "application/json" -Body $body

```

# Deploy

```bash
functions\venv\Scripts\activate
pip freeze > .\functions\requirements.txt
firebase deploy --only functions
```

# Links

- [Cloud Firestore](https://console.firebase.google.com/project/llm-studies/firestore/databases/-default-/data/~2Fusuarios_autorizados)
