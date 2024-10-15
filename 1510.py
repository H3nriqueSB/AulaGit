#ATV 01 Calcular Fatorial

# numero = int(input("Digite um número para calcular o fatorial: "))

# if numero < 0:
#     resultado = "Fatorial não definido para números negativos."
# else:
#     resultado = 1
#     for i in range(2, numero + 1):
#         resultado *= i

# print(f"O fatorial de {numero} é {resultado}.")

#-------------------------------------------------------------------

#ATV 02 Criar Tabuada

# numero = int(input("Digite um número: "))
# print(f"Tabuada do {numero}:")

# for i in range(1, 11):
#     print(f"{numero} x {i} = {numero * i}")

#-------------------------------------------------------------------
#ATV 03 Verificar se um palavra é um palindromo
#-------------------------------------------------------------------

#ATV 04 Receber 10 numeros e somar os pares

# soma = 0

# for i in range(10):
#     numero = int(input(f"Digite o {i + 1}º número: "))
#     if numero % 2 == 0:
#         soma += numero

# print(f"A soma dos números pares é: {soma}")


#-------------------------------------------------------------------

#ATV 05 Verificar numero primo

# entrada = int(input("Digite um número: "))

# if entrada <= 1:
#     print(f"{entrada} não é um número primo.")
# else:
#     primo = True
#     for i in range(2, int(entrada**0.5) + 1):
#         if entrada % i == 0:
#             primo = False
#             break

#     if primo:
#         print(f"{entrada} é um número primo.")
#     else:
#         print(f"{entrada} não é um número primo.")

#-------------------------------------------------------------------

#ATV 06 Ordenar de forma crescente
# entrada = input("Digite os números separados por espaço: ")
# numeros = list(map(int, entrada.split()))

# numeros.sort()

# print("Lista ordenada:", numeros)

#-------------------------------------------------------------------