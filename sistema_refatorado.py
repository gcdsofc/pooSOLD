# sistema_pedidos_refatorado.py

from abc import ABC, abstractmethod

# ====================================================
# 1️⃣ Abstrações (Interfaces)
# ====================================================

class MetodoDePagamento(ABC):
    @abstractmethod
    def pagar(self, pedido):
        pass


class MetodoDeNotificacao(ABC):
    @abstractmethod
    def notificar(self, pedido):
        pass


# ====================================================
# 2️⃣ Implementações concretas
# ====================================================

# --- Pagamentos ---
class PagamentoCartaoCredito(MetodoDePagamento):
    def pagar(self, pedido):
        print(f"Pagando R$ {pedido['valor']:.2f} com cartão de crédito...")


class PagamentoBoleto(MetodoDePagamento):
    def pagar(self, pedido):
        print(f"Gerando boleto no valor de R$ {pedido['valor']:.2f}...")


# BÔNUS: novo método de pagamento — Pix
class PagamentoPix(MetodoDePagamento):
    def pagar(self, pedido):
        print(f"Pagando R$ {pedido['valor']:.2f} via PIX...")


# --- Notificações ---
class NotificacaoEmail(MetodoDeNotificacao):
    def notificar(self, pedido):
        print(f"Enviando e-mail de confirmação para {pedido['cliente_email']}...")


# BÔNUS: novo método de notificação — SMS
class NotificacaoSMS(MetodoDeNotificacao):
    def notificar(self, pedido):
        print(f"Enviando SMS para o cliente confirmando o pedido #{pedido['id']}...")


# ====================================================
# 3️⃣ Classe principal (agora com SRP e DIP)
# ====================================================

class ProcessadorDePedidos:
    def __init__(self, metodo_pagamento: MetodoDePagamento, metodo_notificacao: MetodoDeNotificacao):
        # DIP: depende de abstrações, não de implementações concretas
        self.metodo_pagamento = metodo_pagamento
        self.metodo_notificacao = metodo_notificacao

    def processar(self, pedido):
        # SRP: responsabilidade apenas de orquestrar o processo
        print(f"Processando o pedido #{pedido['id']} no valor de R$ {pedido['valor']:.2f}...")
        self.metodo_pagamento.pagar(pedido)
        self.metodo_notificacao.notificar(pedido)
        pedido['status'] = 'concluido'
        print("Pedido concluído!")


# ====================================================
# 4️⃣ Execução (cliente)
# ====================================================

if __name__ == "__main__":
    pedido1 = {
        'id': 123,
        'valor': 150.75,
        'cliente_email': 'cliente@exemplo.com',
        'status': 'pendente'
    }

    # Pagamento com Cartão + Notificação por E-mail
    processador1 = ProcessadorDePedidos(PagamentoCartaoCredito(), NotificacaoEmail())
    processador1.processar(pedido1)

    print("-" * 30)

    # Pagamento com Boleto + Notificação por SMS (novo método)
    pedido2 = pedido1.copy()
    pedido2['id'] = 456
    processador2 = ProcessadorDePedidos(PagamentoBoleto(), NotificacaoSMS())
    processador2.processar(pedido2)

    print("-" * 30)

    # BÔNUS: Pagamento com PIX + Notificação por E-mail
    pedido3 = pedido1.copy()
    pedido3['id'] = 789
    processador3 = ProcessadorDePedidos(PagamentoPix(), NotificacaoEmail())
    processador3.processar(pedido3)
