from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return "Serviço rodando no Render! 🚀"

# Inicia seu script principal como subprocesso
subprocess.Popen(["python3", "jexarindia.py"])

import os
port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)
