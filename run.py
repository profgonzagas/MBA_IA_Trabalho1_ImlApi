"""
Script para executar a API
"""
import uvicorn
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente
load_dotenv()

if __name__ == "__main__":
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", "8000"))
    reload = os.getenv("API_RELOAD", "True").lower() == "true"
    
    uvicorn.run(
        "src.api.app:app",
        host=host,
        port=port,
        reload=reload
    )
