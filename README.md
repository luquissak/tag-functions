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


```bash
Stop-Process -Id (Get-NetTCPConnection -LocalPort 4000).OwningProcess -Force
firebase emulators:start --only functions
```