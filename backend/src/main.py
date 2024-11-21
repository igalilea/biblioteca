from fastapi import FastAPI

app = FastAPI(
    title="My Library API",
    description="API para gestionar una biblioteca personal",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {"message": "Bienvenido a My Library API"}