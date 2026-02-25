import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import APP_NAME, DEBUG

app = FastAPI(
    title=APP_NAME,
    description="Auction System APIs",
    version="1.0.0",
    debug=DEBUG,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# ---------- CORS SETUP ----------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- FUTURE ROUTERS PLACEHOLDER ----------

# Example:
from app.routers.auth import router as auth_router

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

# ---------- UVICORN RUNNER ----------

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=DEBUG, log_level="info")
