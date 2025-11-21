from fastapi import APIRouter, HTTPException
from src.models.schemas import CalculoCustoRequest, CalculoCustoResponse
from src.services.calculo_service import CalculoService

router = APIRouter(prefix="/calcular", tags=["Cálculo"])


@router.post("", response_model=CalculoCustoResponse)
async def calcular_custo(request: CalculoCustoRequest):
    """
    Calcula o custo total de um exame pericial com base nos parâmetros fornecidos.
    """
    try:
        return CalculoService.calcular_custo(request)
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Parâmetro inválido: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno no cálculo: {str(e)}")
