# API IML/PCDF - Sistema de Cálculo de Custos de Perícia

## 📋 Sobre o Projeto

API desenvolvida para cálculo de custos de exames periciais do Instituto Médico Legal da Polícia Civil do Distrito Federal (IML/PCDF). O sistema calcula custos com base no tipo de exame, complexidade, quantidade de amostras e urgência.

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/profgonzagas/MBA_IA_Trabalho1_ImlApi
cd ApiIML
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Execute a API:**
```bash
python run.py
```
Ou diretamente com uvicorn:
```bash
uvicorn src.api.app:app --reload --host 0.0.0.0 --port 8000
```

4. **Acesse a documentação:**
- Swagger UI: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

## 🧪 Executando os Testes

```bash
# Testes da nova arquitetura
pytest tests/test_api.py -v

# Testes de compatibilidade
pytest test_main.py -v

# Todos os testes
pytest -v
```

## 📊 Endpoints

### GET /
Retorna informações básicas da API.

### GET /health
Health check da aplicação.

**Response:**
```json
{
  "status": "healthy",
  "service": "IML/PCDF API"
}
```

### POST /calcular
Calcula o custo total de um exame pericial.

**Exemplo de Request:**
```json
{
  "tipo_exame": "DNA",
  "complexidade": "alta",
  "amostras": 3,
  "urgente": true,
  "numero_processo": "PCDF-2024-12345"
}
```

**Exemplo de Response:**
```json
{
  "tipo_exame": "DNA",
  "complexidade": "alta",
  "amostras": 3,
  "urgente": true,
  "numero_processo": "PCDF-2024-12345",
  "custo_base": "3200.00",
  "custo_amostras": "300.00",
  "acrescimo_urgencia": "1050.00",
  "total": "4550.00",
  "tempo_estimado": "2-3 dias (urgente)"
}
```

### POST /validar
Valida o formato do número do processo PCDF.

**Exemplo de Request:**
```json
{
  "numero_processo": "PCDF-2023-12345"
}
```

**Exemplo de Response:**
```json
{
  "numero_processo": "PCDF-2023-12345",
  "valido": true,
  "mensagem": "Número de processo válido"
}
```

## 🏗️ Estrutura do Código

```
src/
├── api/                      # Camada de API REST
│   ├── app.py               # Aplicação FastAPI principal
│   └── routes/              # Endpoints organizados
│       ├── health.py        # Health check
│       ├── calculo.py       # Cálculo de custos
│       └── validacao.py     # Validação de processos
├── models/                   # Modelos de dados
│   └── schemas.py           # Schemas Pydantic
├── services/                 # Lógica de negócio
│   ├── calculo_service.py   # Serviço de cálculo
│   └── validacao_service.py # Serviço de validação
└── core/                     # Configurações
    └── config.py            # Constantes e tabelas

tests/                        # Testes organizados
├── test_api.py              # Testes da API

Arquivos raiz:
├── run.py                   # Script para executar
├── requirements.txt         # Dependências
├── README.md                # Esta documentação

```

## 📈 Regras de Negócio

### Tipos de Exame Suportados
- toxicológico
- lesão corporal
- DNA
- sexologia
- antropologia

### Complexidades
- baixa
- média
- alta

### Cálculos

**Custo Base:** Define por tipo de exame e complexidade

| Tipo de Exame | Baixa | Média | Alta |
|---------------|-------|-------|------|
| toxicológico  | R$ 800,00 | R$ 1.200,00 | R$ 1.800,00 |
| lesão corporal | R$ 600,00 | R$ 900,00 | R$ 1.400,00 |
| DNA           | R$ 1.500,00 | R$ 2.200,00 | R$ 3.200,00 |
| sexologia     | R$ 400,00 | R$ 600,00 | R$ 900,00 |
| antropologia  | R$ 1.000,00 | R$ 1.500,00 | R$ 2.200,00 |

**Amostras Extras:** R$ 150,00 por amostra adicional (acima da primeira)

**Urgência:** Acréscimo de 30% sobre o subtotal (custo base + amostras)

**Tempo Estimado:**
- Baixa: 5-7 dias
- Média: 10-15 dias
- Alta: 20-30 dias
- Urgente: 2-3 dias

### Validação de Processo
Formato esperado: `PCDF-AAAA-NNNNN`
- Prefixo: PCDF
- Ano: 4 dígitos
- Sequência: 5 dígitos

Exemplo: `PCDF-2024-12345`

## ✅ Requisitos Atendidos

- ✅ Repositório GitHub (público)
- ✅ README.md completo com instruções
- ✅ API FastAPI com pelo menos 2 endpoints (`/calcular` e `/validar`)
- ✅ Validação com Pydantic (modelos de entrada e saída claros)
- ✅ Testes com Pytest (health-check e lógica principal)
- ✅ Histórico de commits descritivo

## 🧪 Cobertura de Testes

Os testes cobrem:
- Health check endpoint
- Cálculo de custos com diferentes tipos de exame
- Cálculo com urgência
- Validação de processos válidos e inválidos
- Validação de entrada (Pydantic)
- Casos de erro

## 📝 Exemplo de Uso

```python
import requests

# Calcular custo de exame
response = requests.post(
    "http://localhost:8000/calcular",
    json={
        "tipo_exame": "toxicológico",
        "complexidade": "alta",
        "amostras": 3,
        "urgente": True,
        "numero_processo": "PCDF-2024-12345"
    }
)
print(response.json())

# Validar processo
response = requests.post(
    "http://localhost:8000/validar",
    json={
        "numero_processo": "PCDF-2024-12345"
    }
)
print(response.json())
```

## 👨‍💻 Desenvolvido por Wellington Alves Gonzaga

Projeto desenvolvido para o trabalho 1 do MBA em IA.

