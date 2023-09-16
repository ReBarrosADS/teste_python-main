print("=================================================")
print("=============Vamos caucular seu IMC?=============")
print("=================================================")


nome = input("Digite seu nome: ")
idade = float(input("Digite a sua idade: "))
peso = float(input("Digite seu peso:" ))
altura = float(input("Digite a sua altura: "))


calcImc = peso / (altura * altura)




print("=================================================")

print(f"Olá {nome}, sua idade é {idade} anos, seu IMC é: {calcImc:.2f}")
print(classificar_imc)
