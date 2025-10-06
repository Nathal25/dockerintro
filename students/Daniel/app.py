from flask import Flask, request, jsonify
import os, pathlib, datetime

app = Flask(__name__)

STUDENT = os.getenv("STUDENT_NAME", "Daniel Cárdenas")
BARRIO = os.getenv("BARRIO", "Fenalco Kennedy")
LOG_PATH = "/var/log/app/visitas.log"

pathlib.Path("/var/log/app").mkdir(parents=True, exist_ok=True)

def log_visit(msg: str):
    ts = datetime.datetime.utcnow().isoformat()
    line = f"{ts} ip={request.remote_addr} path={request.path} msg={msg}\n"
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line)

@app.get("/")
def root():
    msg = f"Hi, I am {STUDENT} and I live in {BARRIO} neighborhood"
    log_visit(msg)
    return msg, 200, {"Content-Type":"text/plain; charset=utf-8"}

@app.get("/health")
def health():
    return jsonify(ok=True), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)