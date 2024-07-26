from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, descricao) -> None:
        super().__init__(nome, preco)
        self._descricao = descricao\

    def __str__(self) -> str:
        return super().__str__()

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.03)
