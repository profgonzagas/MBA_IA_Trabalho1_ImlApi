import pytest
from fastapi.testclient import TestClient
from src.api.app import app

client = TestClient(app)


def test_root():
    """Testa o endpoint raiz"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "API IML/PCDF - Sistema de Cálculo de Custos de Perícia"
    assert data["version"] == "1.0.0"


def test_health_check():
    """Testa o health check"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "IML/PCDF API"


def test_calcular_custo_basico():
    """Testa cálculo básico de custo"""
    request_data = {
        "tipo_exame": "toxicológico",
        "complexidade": "baixa",
        "amostras": 1,
        "urgente": False,
        "numero_processo": "PCDF-2024-12345"
    }
    response = client.post("/calcular", json=request_data)
    assert response.status_code == 200
    data = response.json()
    assert data["custo_base"] == "800.00"
    assert data["custo_amostras"] == "0.00"
    assert data["acrescimo_urgencia"] == "0.00"
    assert data["total"] == "800.00"
    assert data["tempo_estimado"] == "5-7 dias"


def test_calcular_custo_com_amostras_extras():
    """Testa cálculo com amostras extras"""
    request_data = {
        "tipo_exame": "DNA",
        "complexidade": "alta",
        "amostras": 3,
        "urgente": False,
        "numero_processo": "PCDF-2024-12345"
    }
    response = client.post("/calcular", json=request_data)
    assert response.status_code == 200
    data = response.json()
    assert data["custo_base"] == "3200.00"
    assert data["custo_amostras"] == "300.00"  # 2 amostras extras * 150
    assert data["acrescimo_urgencia"] == "0.00"
    assert data["total"] == "3500.00"


def test_calcular_custo_urgente():
    """Testa cálculo com urgência"""
    request_data = {
        "tipo_exame": "lesão corporal",
        "complexidade": "média",
        "amostras": 1,
        "urgente": True,
        "numero_processo": "PCDF-2024-12345"
    }
    response = client.post("/calcular", json=request_data)
    assert response.status_code == 200
    data = response.json()
    assert data["custo_base"] == "900.00"
    assert data["custo_amostras"] == "0.00"
    assert data["acrescimo_urgencia"] == "270.00"  # 30% de 900
    assert data["total"] == "1170.00"
    assert data["tempo_estimado"] == "2-3 dias (urgente)"


def test_calcular_custo_completo():
    """Testa cálculo completo com urgência e amostras extras"""
    request_data = {
        "tipo_exame": "DNA",
        "complexidade": "alta",
        "amostras": 3,
        "urgente": True,
        "numero_processo": "PCDF-2024-12345"
    }
    response = client.post("/calcular", json=request_data)
    assert response.status_code == 200
    data = response.json()
    assert data["custo_base"] == "3200.00"
    assert data["custo_amostras"] == "300.00"
    assert data["acrescimo_urgencia"] == "1050.00"  # 30% de 3500
    assert data["total"] == "4550.00"


def test_validar_processo_valido():
    """Testa validação de processo válido"""
    request_data = {"numero_processo": "PCDF-2024-12345"}
    response = client.post("/validar", json=request_data)
    assert response.status_code == 200
    data = response.json()
    assert data["valido"] is True
    assert data["mensagem"] == "Número de processo válido"


def test_validar_processo_invalido_prefixo():
    """Testa validação de processo com prefixo inválido"""
    request_data = {"numero_processo": "PCSP-2024-12345"}
    response = client.post("/validar", json=request_data)
    assert response.status_code == 200
    data = response.json()
    assert data["valido"] is False
    assert "Prefixo inválido" in data["mensagem"]


def test_validar_processo_invalido_formato():
    """Testa validação de processo com formato inválido"""
    request_data = {"numero_processo": "PCDF-2024"}
    response = client.post("/validar", json=request_data)
    assert response.status_code == 200
    data = response.json()
    assert data["valido"] is False


def test_calcular_tipo_exame_invalido():
    """Testa erro com tipo de exame inválido"""
    request_data = {
        "tipo_exame": "invalido",
        "complexidade": "baixa",
        "amostras": 1,
        "urgente": False,
        "numero_processo": "PCDF-2024-12345"
    }
    response = client.post("/calcular", json=request_data)
    assert response.status_code == 422  # Validation error


def test_calcular_amostras_invalidas():
    """Testa erro com quantidade de amostras inválida"""
    request_data = {
        "tipo_exame": "toxicológico",
        "complexidade": "baixa",
        "amostras": 15,  # Máximo é 10
        "urgente": False,
        "numero_processo": "PCDF-2024-12345"
    }
    response = client.post("/calcular", json=request_data)
    assert response.status_code == 422  # Validation error


def test_calcular_numero_processo_invalido():
    """Testa erro com número de processo sem prefixo PCDF"""
    request_data = {
        "tipo_exame": "toxicológico",
        "complexidade": "baixa",
        "amostras": 1,
        "urgente": False,
        "numero_processo": "2024-12345"
    }
    response = client.post("/calcular", json=request_data)
    assert response.status_code == 422  # Validation error
