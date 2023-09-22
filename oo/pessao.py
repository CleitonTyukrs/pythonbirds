class Pessoa:
    def __init__(self,*filhos,nome=None, idade=30):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
       return 'Ola'
if __name__ == '__main__':
    cleyton =Pessoa(nome='Cleyton')
    luciano = Pessoa(cleyton, nome='Luciano')

    for filho in luciano.filhos:
        print(filho.nome)



