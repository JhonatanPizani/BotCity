class Contador:
    def __init__(self, valor_inicial):
        self.valor = valor_inicial

    def decrementar(self):
        self.valor -= 1

    def reiniciar(self, novo_valor):
        self.valor = novo_valor
