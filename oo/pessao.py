class Pessoa:
    def __init__(self, nome='Cleyton', idade=30):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
       return 'Ola'
if __name__ == '__main__':
    p = Pessoa()
    print(p.cumprimentar())
    print(p.idade)
    print(p.nome)