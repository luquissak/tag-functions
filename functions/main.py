from firebase_functions import https_fn
from firebase_admin import initialize_app, firestore
import json

initialize_app()
db = firestore.client()


@https_fn.on_request()
def verificar_login(req: https_fn.Request) -> https_fn.Response:
    # 1. Tratamento de CORS para chamadas do Frontend
    if req.method == "OPTIONS":
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST",
            "Access-Control-Allow-Headers": "Content-Type",
        }
        return https_fn.Response("", status=204, headers=headers)

    headers = {"Access-Control-Allow-Origin": "*"}

    if req.headers.get("X-Firebase-AppCheck") is None:
        return https_fn.Response("Não autorizado pelo App Check", status=401)

    try:
        data = req.get_json()
        email_fornecido = data.get("email")

        if not email_fornecido:
            return https_fn.Response("Email ausente", status=400, headers=headers)

        db = firestore.client()
        # Busca o email na coleção do Firestore
        docs = db.collection("usuarios_autorizados").where(
            "email", "==", email_fornecido).stream()
        authorized = any(docs)

        log_entry = {
            "email": email_fornecido,
            "status": "sucesso" if authorized else "falha",
            "timestamp": firestore.SERVER_TIMESTAMP,
            #            "ip": req.remote_addr, # Pega o IP do cliente
            "ip": req.headers.get('X-Forwarded-For', req.remote_addr),
            "user_agent": req.headers.get("User-Agent")
        }
        db.collection("audit_logs").add(log_entry)

        if authorized:
            return https_fn.Response(json.dumps({"auth": True}), status=200, headers=headers, mimetype="application/json")
        else:
            return https_fn.Response(json.dumps({"auth": False}), status=403, headers=headers, mimetype="application/json")

    except Exception as e:
        db.collection("audit_logs").add({"status": "erro_sistema", "erro": str(
            e), "timestamp": firestore.SERVER_TIMESTAMP})
        return https_fn.Response(str(e), status=500, headers=headers)


@https_fn.on_request()
def chat(req: https_fn.Request) -> https_fn.Response:
    # 1. Configuração de CORS (Obrigatório para o fetch do HTML funcionar)
    if req.method == "OPTIONS":
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST",
            "Access-Control-Allow-Headers": "Content-Type, X-Firebase-AppCheck",
        }
        return https_fn.Response("", status=204, headers=headers)

    headers = {"Access-Control-Allow-Origin": "*"}

    # 2. Validação de Segurança (App Check)
#    if req.headers.get("X-Firebase-AppCheck") is None:
#        return https_fn.Response("Acesso não autorizado", status=401, headers=headers)

    try:
        data = req.get_json()
        pergunta = data.get("query")
        session_id = data.get("session_id")

        # 3. Lógica do Agente (Exemplo: Chamada para Vertex AI ou lógica customizada)
        # Aqui você integraria com o seu backend de IA
        resposta_ia = f"Olá! Você perguntou: '{pergunta}'. Eu sou o agente da CEF rodando no GCP."

        # 4. Auditoria do Chat no Firestore
        db.collection("historico_chat").add({
            "session_id": session_id,
            "pergunta": pergunta,
            "resposta": resposta_ia,
            "timestamp": firestore.SERVER_TIMESTAMP
        })

        return https_fn.Response(
            json.dumps({"answer": resposta_ia}),
            status=200,
            headers=headers,
            mimetype="application/json"
        )

    except Exception as e:
        return https_fn.Response(str(e), status=500, headers=headers)
