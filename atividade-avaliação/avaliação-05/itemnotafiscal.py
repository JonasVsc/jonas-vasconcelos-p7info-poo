"""
    Módulo itemnotafiscal 
    Classe ItemNotaFiscal 
    Atributos :
        id         - informado
        sequencial - informado
        quantidade - informado
        produto    - informado
        valor      - calculado.            
"""
from produto import Produto

class ItemNotaFiscal():
    
  
    def __init__(self, id, sequencial, quantidade, produto):
        self._id=id
        self._sequencial=sequencial
        self._quantidade=quantidade
        self._produto=produto
        self._descricao=self._produto.getDescricao()
        self._valorUnitario=self._produto.getValorUnitario()
        self._valorItem=float(self._quantidade * self._valorUnitario)

    @property
    def get_sequencial(self):
        return self._sequencial

    @property
    def get_quantidade(self):
        return self._quantidade

    @property
    def get_produto(self):
        return self._produto

    @property
    def get_descricao(self):
        return self._descricao

    @property
    def get_valorItem(self):
        return self._valorItem

    @property
    def get_valorUnitario(self):
        return self._valorUnitario
      
    def str(self):
        string="\nId={5} Sequencial={4} Quantidade={3} Produto={2} Valor Unitario={1} Valor Item={0}".format(self._valorItem,
                                                                                                             self._valorUnitario,
                                                                                                             self._descricao, 
                                                                                                             self._quantidade, 
                                                                                                             self._sequencial, 
                                                                                                             self._id)
        return string
    
        
if __name__ == '__main__':
    produto = Produto(1,100,'Arroz', 5.5) 
    item=ItemNotaFiscal(1, 1, 12, produto)
    print(item.str())
        
    

