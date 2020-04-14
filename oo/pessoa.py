class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=27, olhos=2):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    pass


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    jessica = Mutante(nome='Jessica')
    jardson = Homem(jessica, nome='Jardson')
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
    print(Pessoa.olhos)
    print(jardson.olhos)
    print(jessica.olhos)
    print(id(Pessoa.olhos), id(jardson.olhos), id(jessica.olhos))
    print(Pessoa.metodo_estatico(), jardson.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), jardson.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(jessica, Pessoa))
    print(isinstance(jessica, Homem))
    print(jessica.olhos)