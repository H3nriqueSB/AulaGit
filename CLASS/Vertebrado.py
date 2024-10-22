class Animal:
    def __init__(self, nomesci, filo, som, reproducao, alimentacao):
        self.nome = nomesci
        self.filo = filo
        self.som = som
        self.repro = reproducao
        self.alimen = alimentacao

    def info(self):
        print(f"Nome: {self.nome}")
        print(f"Filo: {self.filo}")
        print(f"Som: {self.som}")
        print(f"Reprodução: {self.repro}")
        print(f"Alimentação: {self.alimen}")

class vertebrado(Animal):
    def __init__(self, nomesci, filo, som, reproducao, alimentacao):
        super().__init__(nomesci, filo, som, reproducao, alimentacao)
        self.coluna_vertebral = True

class invertebrado(Animal):
    def __init__(self, nomesci, filo, som, reproducao, alimentacao):
        super().__init__(nomesci, filo, som, reproducao, alimentacao)
        self.coluna_invertebral = False

# ornitorrinco = vertebrado("Ornitorrinco", "Chordata", "Grunhido", "Ovíparo", "Carnívoro")

# if(ornitorrinco.coluna_vertebral == True):
#     print(f'Possuí coluna vertebral: {ornitorrinco.coluna_vertebral}')

class Mamifero(vertebrado):
    def __init__(self, nomesci, filo, som, reproducao, alimentacao):
        super().__init__(nomesci, filo, som, reproducao, alimentacao)

    def Amamentar(self):
        print("Mamifero")

class morcego(Mamifero):
    def voar(self):
        print("voar")
class baleia(Mamifero):
    def esguicho(self):
        print("esguichou")
class ornitorrinco(Mamifero):
    def envenanar(self):
        print("Vc foi envenenado")

bat = morcego("Morcego", "Urbano", "Grunido", "Sexuado", "Frutifero")
print(vars (bat))

bale = baleia("Baleia", "Oceano", "Eco", "Sexuado", "Carnivoro")
print(vars (bale))


# Exemplo de uso


# #Aves
# class Ave(Animal):
#     def __init__(self, nome, filo, classe, ordem, familia, genero, especie):
#         super().__init__(nome, "Animalia", filo, classe, ordem, familia, genero)
#         self.especie = especie

#     def info_taxonomica(self):
#         super().info_taxonomica()
#         print(f"Espécie: {self.especie}")
# #Amphibios
# class Amphibia(Animal):
#     def __init__(self, nome, filo, classe, ordem, familia, genero, especie):
#         super().__init__(nome, "Animalia", filo, classe, ordem, familia, genero)
#         self.especie = especie

#     def info_taxonomica(self):
#         super().info_taxonomica()
#         print(f"Espécie: {self.especie}")
# #Roedores
# class Roedores(Animal):
#     def __init__(self, nome, filo, classe, ordem, familia, genero, especie):
#         super().__init__(nome, "Animalia", filo, classe, ordem, familia, genero)
#         self.especie = especie

#     def info_taxonomica(self):
#         super().info_taxonomica()
#         print(f"Espécie: {self.especie}")
# #Canidios
# class Canideos(Animal):
#     def __init__(self, nome, filo, classe, ordem, familia, genero, especie):
#         super().__init__(nome, "Animalia", filo, classe, ordem, familia, genero)
#         self.especie = especie

#     def info_taxonomica(self):
#         super().info_taxonomica()
#         print(f"Espécie: {self.especie}")

# #Print das classes
# mamifero1 = Mamifero("Leão", "Chordata", "Mammalia", "Carnivora", "Felidae", "Panthera", "leo")
# print("Informações taxonômicas do Leão:")
# mamifero1.info_taxonomica()

# print()

# mamifero1 = Mamifero("Sphynx", "Chordata", "Mammalia", "Carnivora", "Felidae", "Felis", "Felis catus")
# print("Informações taxonômicas do Sphynx:")
# mamifero1.info_taxonomica()

# print()

# mamifero1 = Mamifero("Gato-persa", "Chordata", "Mammalia", "Carnivora", "Felidae", "Felis", "Felis catus")
# print("Informações taxonômicas do Gato-persa:")
# mamifero1.info_taxonomica()

# print()

# mamifero1 = Mamifero("Gato-siames", "Chordata", "Mammalia", "Carnivora", "Felidae", "Felis", "Felis catus")
# print("Informações taxonômicas do Gato-siames:")
# mamifero1.info_taxonomica()

# print()

# mamifero1 = Mamifero("Angorá", "Chordata", "Mammalia", "Carnivora", "Felidae", "Felis", "Felis catus")
# print("Informações taxonômicas do Angorá:")
# mamifero1.info_taxonomica()

# print()

# #Aves
# ave1 = Ave("Águia", "Chordata", "Aves", "Accipitriformes", "Accipitridae", "Aquila", "chrysaetos")
# print("\nInformações taxonômicas da Águia:")
# ave1.info_taxonomica()

# print()

# ave1 = Ave("Pinguim", "Chordata", "Aves", "Accipitriformes", "Accipitridae", "Spheniscidae", "Spheniscidae")
# print("\nInformações taxonômicas do Pinguim:")
# ave1.info_taxonomica()

# print()

# ave1 = Ave("Pardal", "Chordata", "Aves", "Accipitriformes", "Accipitridae", "Spheniscidae", "Spheniscidae")
# print("\nInformações taxonômicas do Pardal:")
# ave1.info_taxonomica()

# print()

# ave1 = Ave("Pavo", "Chordata", "Aves", "Accipitriformes", "Accipitridae", "Spheniscidae", "Spheniscidae")
# print("\nInformações taxonômicas do Pavo:")
# ave1.info_taxonomica()

# print()

# ave1 = Ave("Urutau", "Chordata", "Aves", "Nyctibiiformes", "Nyctibiidae", "Nyctibius", "N. griseus")
# print("\nInformações taxonômicas do Urutau:")
# ave1.info_taxonomica()

# print()

# #Amphibios
# Amphibia1 = Amphibia("Sapo-cururu", "Chordata", "Amphibia", "Anura", "Bufonidae", "Rhinella", "Rhinella marina")
# print("\nInformações taxonômicas do Sapo-cururu:")
# Amphibia1.info_taxonomica()

# print()

# Amphibia1 = Amphibia("Sapo-parteiro", "Chordata", "Amphibia", "Anura", "Bufonidae", "Rhinella", "Rhinella marina")
# print("\nInformações taxonômicas do Sapo-parteiro:")
# Amphibia1.info_taxonomica()

# print()

# Amphibia1 = Amphibia("Bufo bufo", "Chordata", "Amphibia", "Anura", "Bufonidae", "Bufotes", "Bufotes bufo")
# print("\nInformações taxonômicas do Bufo bufo:")
# Amphibia1.info_taxonomica()

# print()

# Amphibia1 = Amphibia("Rã-leopardo", "Chordata", "Amphibia", "Anura", "Ranidae", "Lithobates", "Lithobates pipiens")
# print("\nInformações taxonômicas da Rã-leopardo:")
# Amphibia1.info_taxonomica()

# print()

# Amphibia1 = Amphibia("Axolote", "Chordata", "Amphibia", "Urodela", "Ambystomatidae", "Ambystoma", "Ambystoma mexicanum")
# print("\nInformações taxonômicas do Axolote:")
# Amphibia1.info_taxonomica()

# print()

# #Roedores
# Roedores1 = Roedores("Capivara", "Chordata", "Mammalia", "Rodentia", "Caviidae", "Hydrochoerus", "Hydrochoerus hydrochaeris")
# print("\nInformações taxonômicas da Capivara:")
# Roedores1.info_taxonomica()

# print()

# Roedores1 = Roedores("Castor canadensis", "Chordata", "Mammalia", "Rodentia", "Castoridae", "Castor", "Castor canadensis")
# print("\nInformações taxonômicas do Castor canadensis:")
# Roedores1.info_taxonomica()

# print()

# Roedores1 = Roedores("Esquilo vermelho europeu", "Chordata", "Mammalia", "Rodentia", "Sciuridae", "Sciurus", "Sciurus vulgaris")
# print("\nInformações taxonômicas do Esquilo vermelho europeu:")
# Roedores1.info_taxonomica()

# print()

# Roedores1 = Roedores("Hamster", "Chordata", "Mammalia", "Rodentia", "Cricetidae", "Mesocricetus", "Mesocricetus auratus")
# print("\nInformações taxonômicas do Hamster:")
# Roedores1.info_taxonomica()

# print()

# Roedores1 = Roedores("Chinchilla", "Chordata", "Mammalia", "Rodentia", "Chinchillidae", "Chinchilla", "Chinchilla lanigera")
# print("\nInformações taxonômicas do Chinchilla:")
# Roedores1.info_taxonomica()

# print()

# #Canideos
# Canidio1 = Canideos("Coiote", "Chordata", "Mammalia", "Carnivora", "Canidae", "Canis", "Canis latrans")
# print("\nInformações taxonômicas do Coiote:")
# Canidio1.info_taxonomica()

# print()

# Canidio1 = Canideos("Feneco", "Chordata", "Mammalia", "Carnivora", "Canidae", "Vulpes", "Vulpes zerda")
# print("\nInformações taxonômicas do Feneco:")
# Canidio1.info_taxonomica()

# print()

# Canidio1 = Canideos("Lobo-guará", "Chordata", "Mammalia", "Carnivora", "Canidae", "Chrysocyon", "Chrysocyon brachyurus")
# print("\nInformações taxonômicas do Lobo-guará:")
# Canidio1.info_taxonomica()

# print()

# Canidio1 = Canideos("Mabeco", "Chordata", "Mammalia", "Carnivora", "Hyaenidae", "Parahyaena", "Parahyaena brunnea")
# print("\nInformações taxonômicas do Mabeco:")
# Canidio1.info_taxonomica()

# print()

# Canidio1 = Canideos("Pug", "Chordata", "Mammalia", "Carnivora", "Hyaenidae", "Canis", "Canis lupus")
# print("\nInformações taxonômicas do Pug:")
# Canidio1.info_taxonomica()