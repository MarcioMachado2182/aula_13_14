from datetime import datetime

class Pagamento:
    def __init__(self):
        self.vencimento = datetime(2024, 6, 30)

class PagamentoBoleto(Pagamento):
    def __init__(self, codigo_barras: str):
        self.codigo_barras = codigo_barras

# Exemplo de uso da classe PagamentoBoleto
vencimento = datetime(2024, 6, 30)
codigo_barras = "12345678901234567890"

pagamento_boleto = PagamentoBoleto(codigo_barras)

print(f"Vencimento: {pagamento_boleto,vencimento}")
print(f"Código de Barras: {pagamento_boleto.codigo_barras}")
