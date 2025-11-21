from fastapi import APIRouter
from src.models.schemas import ValidacaoProcessoRequest, ValidacaoProcessoResponse
from src.services.validacao_service import ValidacaoService

router = APIRouter(prefix="/validar", tags=["Validação"])


@router.post("", response_model=ValidacaoProcessoResponse)
async def validar_processo(request: ValidacaoProcessoRequest):
    """
    Valida o formato do número do processo PCDF.
    Formato esperado: PCDF-AAAA-NNNNN (ex: PCDF-2023-12345)
    """
    return ValidacaoService.validar_processo(request)
