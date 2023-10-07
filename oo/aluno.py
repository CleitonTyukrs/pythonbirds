class Aluno():
    def __init__(self, nome, nota_1,nota_2,):
        self.nome = nome
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.media = 0

    def gerar_media(self):
        self.media = (nota_1 + nota_2)/2
        return self.media

    def imprimir(self):
        return print(f'{self.nome} sua primeira nota foi {self.nota_1} e sua segunda nota foi {self.nota_2} e sua media foi {self.gerar_media}')

    def resultado(self):
        if self.gerar_media >= 6.0:
            print("Voçê foi aprovado")
        else:
            print('Voçê foi reprovado')


nome = str(input('Qual seu nome? '))
nota_1 = float(input('Qual foi sua primeira nota? '))
nota_2 = float(input('Qual foi sua segunda nota? '))
geral_aluno = Aluno(nome,nota_1, nota_2)
geral_aluno.imprimir()




