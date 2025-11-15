from fastapi import FastAPI

from .routes import analyze, demo, causal

app = FastAPI(
    title="Wuwei Psyche Causal Lab API",
    version="0.1.0",
)

app.include_router(analyze.router, prefix="/v1")
app.include_router(causal.router, prefix="/v1")
app.include_router(demo.router)