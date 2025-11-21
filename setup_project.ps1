# Script PowerShell para configurar o projeto

Write-Host "=== Configurando Projeto API IML/PCDF ===" -ForegroundColor Green

# Criar ambiente virtual
Write-Host "`n1. Criando ambiente virtual..." -ForegroundColor Yellow
python -m venv venv

# Ativar ambiente virtual
Write-Host "`n2. Ativando ambiente virtual..." -ForegroundColor Yellow
.\venv\Scripts\Activate.ps1

# Instalar dependências
Write-Host "`n3. Instalando dependências..." -ForegroundColor Yellow
pip install --upgrade pip
pip install -r requirements.txt

Write-Host "`n=== Configuração concluída! ===" -ForegroundColor Green
Write-Host "`nPara executar o projeto:" -ForegroundColor Cyan
Write-Host "  1. Ative o ambiente virtual: .\venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host "  2. Execute a API: python run.py" -ForegroundColor White
Write-Host "  3. Ou use: uvicorn main:app --reload" -ForegroundColor White
Write-Host "`nPara executar os testes:" -ForegroundColor Cyan
Write-Host "  pytest test_main.py -v" -ForegroundColor White
