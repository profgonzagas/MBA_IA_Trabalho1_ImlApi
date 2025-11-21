from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/")
async def root():
    return {
        "message": "API IML/PCDF - Sistema de Cálculo de Custos de Perícia",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "calcular_custo": "/calcular",
            "validar_processo": "/validar"
        }
    }


@router.get("/health")
async def health_check():
    return {"status": "healthy", "service": "IML/PCDF API"}
