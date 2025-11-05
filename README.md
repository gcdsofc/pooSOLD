# Análise dos Princípios SOLID e Refatoração

## Violações encontradas

**SRP (Single Responsibility Principle):**
A classe `ProcessadorDePedidos` possuía múltiplas responsabilidades (processamento, pagamento e notificação).

**OCP (Open/Closed Principle):**
Era necessário modificar o código da classe principal para adicionar novos métodos de pagamento ou notificação.

**DIP (Dependency Inversion Principle):**
A classe dependia diretamente de implementações concretas, em vez de abstrações.

---

## Refatoração aplicada

- Criação de interfaces (`MetodoDePagamento`, `MetodoDeNotificacao`) usando classes abstratas.
- Cada método de pagamento e notificação agora é uma classe separada.
- A classe `ProcessadorDePedidos` foi simplificada, delegando tarefas às abstrações.
- O sistema agora é extensível sem necessidade de modificar código existente (respeitando OCP e DIP).

---

## Extensões adicionadas (Bônus)

- Novo método de pagamento: **Pix**  
- Novo método de notificação: **SMS**

Essas novas funcionalidades foram adicionadas sem alterar nenhuma linha da classe `ProcessadorDePedidos`.
