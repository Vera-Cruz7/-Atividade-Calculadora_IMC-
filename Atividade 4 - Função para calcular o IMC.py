## Solicitação de dados do usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Categorizar o IMC e fornecer recomendações
if imc < 18.5:
    categoria = "Abaixo do peso"
    recomendacao = "Você está abaixo do peso ideal. Considere buscar orientação de um nutricionista."
elif 18.5 <= imc < 25:
    categoria = "Peso normal"
    recomendacao = "Você está com um peso saudável. Continue com bons hábitos alimentares e de exercícios."
elif 25 <= imc < 30:
    categoria = "Sobrepeso"
    recomendacao = "Você está com sobrepeso. Considere melhorar seus hábitos alimentares e aumentar a atividade física."
elif 30 <= imc < 35:
    categoria = "Obesidade grau I"
    recomendacao = "Você está com obesidade grau I. É recomendado consultar um profissional de saúde."
elif 35 <= imc < 40:
    categoria = "Obesidade grau II"
    recomendacao = "Você está com obesidade grau II. É importante procurar ajuda de um profissional de saúde."
else:
    categoria = "Obesidade grau III"
    recomendacao = "Você está com obesidade grau III. Consulte um médico para orientações específicas."

# Condição adicional para idade
if idade < 18:
    recomendacao += " Como você ainda está em fase de crescimento, é importante seguir orientações adequadas para sua idade."
elif idade >= 60:
    recomendacao += " Para pessoas com 60 anos ou mais, outros fatores devem ser considerados além do IMC."

# Exibir resultados
print("\n--- Resultado ---")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")
print(f"IMC: {imc:.2f}")
print(f"Categoria: {categoria}")
print(f"Recomendação: {recomendacao}")