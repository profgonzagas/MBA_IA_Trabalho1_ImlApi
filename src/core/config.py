from decimal import Decimal

# Tabela de custos base por tipo de exame e complexidade
CUSTOS_BASE = {
    "toxicológico": {"baixa": Decimal("800.00"), "média": Decimal("1200.00"), "alta": Decimal("1800.00")},
    "lesão corporal": {"baixa": Decimal("600.00"), "média": Decimal("900.00"), "alta": Decimal("1400.00")},
    "DNA": {"baixa": Decimal("1500.00"), "média": Decimal("2200.00"), "alta": Decimal("3200.00")},
    "sexologia": {"baixa": Decimal("400.00"), "média": Decimal("600.00"), "alta": Decimal("900.00")},
    "antropologia": {"baixa": Decimal("1000.00"), "média": Decimal("1500.00"), "alta": Decimal("2200.00")}
}

# Custo adicional por amostra extra (acima da primeira)
CUSTO_POR_AMOSTRA = Decimal("150.00")

# Acréscimo para exames urgentes (percentual)
ACRESCIMO_URGENCIA = Decimal("0.30")  # 30%

# Tempo estimado por complexidade (dias)
TEMPO_ESTIMADO = {
    "baixa": "5-7 dias",
    "média": "10-15 dias",
    "alta": "20-30 dias"
}
