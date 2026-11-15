from rich import print
from rich.panel import Panel

class mensagem():
    def __init__(self,msg,tipo="aviso",icone=":speech_balloon:"):
        self._mensagem= msg
        self._tipo= tipo
        self._icone=icone
          
    def mostrar(self):
        msg=Panel(self._mensagem,title=f"{self._icone} {self._tipo.upper()} {self._icone}")
        print(msg)
        
class Alerta(mensagem):
    def __init__(self, msg, tipo="aviso", icone=":speech_balloon:"):
         super().__init__(msg, tipo, icone)
    
    
    def mostrar(self):
            msg=Panel(self._mensagem,title=f"{self._icone} {self._tipo.upper()} {self._icone}")
            print(msg)
            
class erro(mensagem):
    def __init__(self, msg, tipo="aviso", icone=":speech_balloon:"):
         super().__init__(msg, tipo, icone)
    
    
    def mostrar(self):
        msg=Panel(self._mensagem,title=f"{self._icone} {self._tipo.upper()} {self._icone}")
        print(msg)

