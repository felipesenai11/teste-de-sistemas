from fastapi import FastAPI
from database import Base, engine
from routers import auth_router, rooms_router, bookings_router, incidents_router

# Cria todas as tabelas no SQLite automaticamente
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema de Reservas de Laboratório (SRL)",
    description="API REST para gerenciamento de reservas de laboratório.",
    version="1.0.0",
    docs_url="/docs",       # Swagger UI  → http://127.0.0.1:8000/docs
    redoc_url="/redoc",     # ReDoc       → http://127.0.0.1:8000/redoc
)

app.include_router(auth_router.router)
app.include_router(rooms_router.router)
app.include_router(bookings_router.router)
app.include_router(incidents_router.router)


@app.get("/", tags=["Status"])
def root():
    return {"status": "online", "docs": "/docs"}
