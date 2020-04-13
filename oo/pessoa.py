class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=27, olhos=2):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    jessica = Pessoa(nome='Jessica')
    jardson = Pessoa(jessica, nome='Jardson')
    print(Pessoa.cumprimentar(jardson))
    print(id(jardson))
    print(jardson.cumprimentar())
    print(jardson.nome)
    print(jardson.idade)
    for filho in jardson.filhos:
        print(filho.nome)
    jardson.sobrenome = 'Lima'
    del jardson.filhos
    jardson.olhos = 1
    del jardson.olhos
    print(jardson.__dict__)
    print(jessica.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(jardson.olhos)
    print(jessica.olhos)
    print(id(Pessoa.olhos), id(jardson.olhos), id(jessica.olhos))