from abc import ABC, abstractmethod
class ItemCardapio:
    def __init__(self, nome, preco) -> None:
        self._nome = nome
        self._preco = preco
    
    def __str__(self) -> str:
        print(self._nome)

    @abstractmethod
    def aplicar_desconto(self):
        pass
