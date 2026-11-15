from exportar import *

def main():
    u=[
        Usuario("Danoel","Dandan@gmail.com"),
        Usuario("Lucas","LucasFulano@gmail.com"),
        Usuario("Ana","AnaCiclana@gmail.com")
    ]
    
    a=[
        Aluno("Fernando","DS","8 periodo"),
        Aluno("Clara","ADS","4 periodo")
    ]
    exportar_dados(XML(),u)
    
if __name__ == "__main__":
    main()