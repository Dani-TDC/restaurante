from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de laranja', 2.50, 'Grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Pãozinho', 1.00, 'Pão Francês')
prato_paozinho.aplicar_desconto()
sobremesa_pave = Sobremesa('Pavê', 4.99, 'O melhor!!!!!!!!!!')
sobremesa_pave.aplicar_desconto()

restaurante_praca.adicionar_item_cardapio(bebida_suco)
restaurante_praca.adicionar_item_cardapio(prato_paozinho)
restaurante_praca.adicionar_item_cardapio(sobremesa_pave)

def main():
    restaurante_praca.listar_cardapio

if __name__ == '__main__':
    main()
