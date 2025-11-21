from fastapi import FastAPI
from src.api.routes import health, calculo, validacao

app = FastAPI(
    title="API IML/PCDF - Cálculo de Custos de Perícia",
    description="Sistema para cálculo de custos de exames periciais do IML/PCDF",
    version="1.0.0"
)

# Incluir rotas
app.include_router(health.router)
app.include_router(calculo.router)
app.include_router(validacao.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
