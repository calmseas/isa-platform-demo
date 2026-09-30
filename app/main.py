"""FastAPI application entry point."""
from fastapi import FastAPI

from app.routes import accounts, admin, contributions, health, transfers

app = FastAPI(title="ISA Platform (demo)", version="0.1.0")

app.include_router(health.router)
app.include_router(accounts.router)
app.include_router(contributions.router)
app.include_router(transfers.router)
app.include_router(admin.router)


@app.get("/")
def root() -> dict[str, str]:
    return {"service": "isa-platform-demo", "docs": "/docs"}
