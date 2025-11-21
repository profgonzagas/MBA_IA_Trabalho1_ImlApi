from decimal import Decimal
from src.models.schemas import CalculoCustoRequest, CalculoCustoResponse
from src.core.config import CUSTOS_BASE, CUSTO_POR_AMOSTRA, ACRESCIMO_URGENCIA, TEMPO_ESTIMADO


class CalculoService:
    """Serviço para cálculo de custos de exames periciais"""
    
    @staticmethod
    def calcular_custo(request: CalculoCustoRequest) -> CalculoCustoResponse:
        """
        Calcula o custo total de um exame pericial com base nos parâmetros fornecidos.
        """
        # Cálculo do custo base
        custo_base = CUSTOS_BASE[request.tipo_exame][request.complexidade]

        # Cálculo do custo adicional por amostras (primeira amostra inclusa no custo base)
        amostras_extras = max(0, request.amostras - 1)
        custo_amostras = amostras_extras * CUSTO_POR_AMOSTRA

        # Cálculo do acréscimo por urgência
        acrescimo_urgencia = Decimal("0.00")
        if request.urgente:
            acrescimo_urgencia = (custo_base + custo_amostras) * ACRESCIMO_URGENCIA

        # Cálculo do total
        total = custo_base + custo_amostras + acrescimo_urgencia

        # Tempo estimado
        tempo_estimado = TEMPO_ESTIMADO[request.complexidade]
        if request.urgente:
            tempo_estimado = "2-3 dias (urgente)"

        return CalculoCustoResponse(
            tipo_exame=request.tipo_exame,
            complexidade=request.complexidade,
            amostras=request.amostras,
            urgente=request.urgente,
            numero_processo=request.numero_processo,
            custo_base=custo_base,
            custo_amostras=custo_amostras,
            acrescimo_urgencia=acrescimo_urgencia,
            total=total,
            tempo_estimado=tempo_estimado
        )
