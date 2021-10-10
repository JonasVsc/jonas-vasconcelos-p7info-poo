"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
import datetime
from cliente        import Cliente
from produto        import Produto
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal():         
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo=codigo
        self._cliente=cliente 
        self._data=datetime.datetime.now()   
        self._itens=[]
        self._valorNota=0.0



        
    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente=cliente    
            
    def adicionarItem(self, item): 
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)
        
    def calcularNotaFiscal(self):
        valor=0.0
        for item in self._itens:
            valor = valor + item.get_valorItem
        self._valorNota=valor

    @property
    def get_valorNota(self):
        return self._valorNota


    def imprimirNotaFiscal(self):
        lista_itens = " "
        for item in self._itens:
            lista_itens += ('''
\n00{}{:>20s}{:>44d}{:>10.2f}{:>15.2f}
''').format(item.get_sequencial, item.get_descricao, item.get_quantidade, item.get_valorUnitario, item.get_valorItem)

        print('''+
{0}
NOTA FISCAL{1}{2}
Cliente: {3}\tNome: {4}
CPF/CPNJ: {5}
{0}
ITENS
{0}
Seq  Descrição                                                 QTD   Valor Unit        Preço
---- -------------------------------------------------------- ----- ------------ ------------------
{6}{0}
Valor Total: {7}
        '''.format('-'*111, ' '*90, self._data.strftime("%d/%m/%Y"), self._cliente.get_codigo, self._cliente.get_nome, self._cliente.get_cnpjcpf, lista_itens, str(self.get_valorNota)))
