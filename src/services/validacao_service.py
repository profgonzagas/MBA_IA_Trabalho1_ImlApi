from src.models.schemas import ValidacaoProcessoRequest, ValidacaoProcessoResponse


class ValidacaoService:
    """Serviço para validação de processos"""
    
    @staticmethod
    def validar_processo(request: ValidacaoProcessoRequest) -> ValidacaoProcessoResponse:
        """
        Valida o formato do número do processo PCDF.
        Formato esperado: PCDF-AAAA-NNNNN (ex: PCDF-2023-12345)
        """
        numero_processo = request.numero_processo.strip()

        # Validação básica do formato
        partes = numero_processo.split('-')

        if len(partes) != 3:
            return ValidacaoProcessoResponse(
                numero_processo=numero_processo,
                valido=False,
                mensagem="Formato inválido. Use: PCDF-AAAA-NNNNN"
            )

        prefixo, ano, sequencia = partes

        if prefixo != "PCDF":
            return ValidacaoProcessoResponse(
                numero_processo=numero_processo,
                valido=False,
                mensagem="Prefixo inválido. Deve ser 'PCDF'"
            )

        if not ano.isdigit() or len(ano) != 4:
            return ValidacaoProcessoResponse(
                numero_processo=numero_processo,
                valido=False,
                mensagem="Ano inválido. Deve ter 4 dígitos"
            )

        if not sequencia.isdigit() or len(sequencia) != 5:
            return ValidacaoProcessoResponse(
                numero_processo=numero_processo,
                valido=False,
                mensagem="Sequência inválida. Deve ter 5 dígitos"
            )

        return ValidacaoProcessoResponse(
            numero_processo=numero_processo,
            valido=True,
            mensagem="Número de processo válido"
        )
