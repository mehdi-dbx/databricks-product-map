import os
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

STATIC_DIR = Path(__file__).parent / "static"

app = FastAPI(title="Databricks AI Tree Mindmap")


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/")
def index():
    return FileResponse(STATIC_DIR / "index.html")


# Serve any other static assets (none required today, but future-proof)
app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")


if __name__ == "__main__":
    port = int(os.environ.get("DATABRICKS_APP_PORT", os.environ.get("PORT", "8000")))
    uvicorn.run(app, host="0.0.0.0", port=port)
