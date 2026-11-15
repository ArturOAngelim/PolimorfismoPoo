from abc import ABC,abstractmethod
import re

class Validador(ABC):
    
    @abstractmethod
    def validar(self,valor):
        pass
    
    @abstractmethod
    def validar_condicoes(self, valor):
        pass

class Usuario(Validador):

    def validar(self,valor):
        regex=r"^[a-zA-Z0-9_]{5,20}$"
        if bool(re.fullmatch(regex, valor)):
            return   True
        else:
            return False
    def validar_condicoes(self,valor):
        if not valor:
            return False,f"O Usuario não pode estar vazio"
        if not 5<=len(valor)<=20:
            return False,f"O usuario precisa ter entre 5 a 20 caracteres"
        
        if not isinstance(valor, str):
            return False, "O email precisa ser texto."
        
        if not self.validar(valor):
            return False,f"Use apenas letras minusculas,maisculas e _"
        
        return True,"Usuario Valido"
            
        
        
class Email(Validador):
        
    def validar(self,valor):
        regex= r"^[a-zA-Z0-9_%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if bool(re.fullmatch(regex,valor)):
            return True
        else:
            return False
    
    def validar_condicoes(self,valor):
        if not valor:
            return False,f"O Email não pode estar vazio"
        
        if not isinstance(valor,str):
            return False,f"O Email precisa ser texto"
        
        if not self.validar(valor):
            return False,f"Formato de texto invalido"
        
        return True,"Email Valido"
            
    
        
class Senha(Validador):

    def validar(self,valor):
        regex=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@!#$%?])[A-Za-z\d@!#$%?]{8,}$"
        if bool(re.fullmatch(regex,valor)):
            return True
        else:
            return False
        
    def validar_condicoes(self,valor):
        if not valor:
            return False,f"Senha não pode estar vazia"
        
        if len(valor) < 8:
            return False,f"A senha precisa de ter pelo menos 8 caracteres"
        
        if not re.search(r"[a-z]", valor):
            return False, "Adicione pelo menos uma letra minúscula."
            
        if not re.search(r"[A-Z]",valor):
            return False,f"A senha precisa ter no minimo um caracter maisculo"
        
        if not re.search(r"[@!#$%?]",valor):
            return False,f"A senha precisa ter no minimo um caracter especial"
        
        if not re.search(r"\d", valor):
            return False, "Adicione pelo menos um número."
        
        if not re.fullmatch(r"[A-Za-z\d@!#$%?]+", valor):
            return False, "A senha contém caracteres não permitidos."
        return True,"Senha Valida"
    
def validar_dado(validador, valor):
    resultado, mensagem = validador.validar_condicoes(valor)
    print(f"{mensagem}")