class Pessoa:
    def __init__(self, *filhos, nome=None, idade=27):
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
    print(jardson.__dict__)
    print(jessica.__dict__)