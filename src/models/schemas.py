from pydantic import BaseModel, Field, field_validator
from typing import Literal
from decimal import Decimal


class CalculoCustoRequest(BaseModel):
    tipo_exame: Literal["toxicológico", "lesão corporal", "DNA", "sexologia", "antropologia"] = Field(
        ..., description="Tipo de exame pericial"
    )
    complexidade: Literal["baixa", "média", "alta"] = Field(
        ..., description="Complexidade do exame"
    )
    amostras: int = Field(..., ge=1, le=10, description="Quantidade de amostras (1-10)")
    urgente: bool = Field(False, description="Se o exame é urgente")
    numero_processo: str = Field(..., min_length=10, max_length=20, description="Número do processo")

    @field_validator('numero_processo')
    @classmethod
    def validate_numero_processo(cls, v):
        if not v.startswith('PCDF-'):
            raise ValueError('Número do processo deve iniciar com PCDF-')
        return v


class CalculoCustoResponse(BaseModel):
    tipo_exame: str
    complexidade: str
    amostras: int
    urgente: bool
    numero_processo: str
    custo_base: Decimal
    custo_amostras: Decimal
    acrescimo_urgencia: Decimal
    total: Decimal
    tempo_estimado: str


class ValidacaoProcessoRequest(BaseModel):
    numero_processo: str = Field(..., min_length=10, max_length=20)


class ValidacaoProcessoResponse(BaseModel):
    numero_processo: str
    valido: bool
    mensagem: str
