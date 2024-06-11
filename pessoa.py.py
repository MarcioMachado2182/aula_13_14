class Pessoa:
    def __init__(self, idade, nome, sexo):
        self.idade = idade
        self.nome = nome
        self.sexo = sexo

    def print_nome(self):
       print(f"O nome do cidadão é: {self.nome}")

    def print_idade(self):
        print(f"Sua idade é: {self.idade} anos")

    def print_sexo(self):
        print(f"o sexo e: {self.sexo}")

pessoa1 = Pessoa(49,'Marcio', 'macho')
pessoa1.print_nome() 
pessoa1.print_idade()
pessoa1.print_sexo()

