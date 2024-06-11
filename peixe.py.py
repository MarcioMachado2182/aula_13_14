class Animal:
    def __init__(self, nome: str, tipo: str, idade: int, cor_do_pelo: str, raca: str):
        self.nome = nome
        self.tipo = tipo
        self.idade = idade
        self.cor_do_pelo = cor_do_pelo
        self.raca = raca

class Peixe(Animal):
    def __init__(self, nome: str, tipo: str, idade: int, cor_do_pelo: str, raca: str, habitat: str):
        super().__init__(nome=nome, tipo = tipo, idade = idade, cor_do_pelo = cor_do_pelo, raca = raca)
        self.habitat = habitat



peixe = Peixe(nome = "Nemo" ,tipo = 'Comestivel', idade = 3, cor_do_pelo = "N/A", raca = "Salmão", habitat = "Mar")
print(f"\nPeixe: {peixe.nome};\n Tipo: {peixe.tipo};\n Idade: {peixe.idade};\n Cor do Pelo: {peixe.cor_do_pelo};\n Raça: {peixe.raca};\n Habitat: {peixe.habitat}")
