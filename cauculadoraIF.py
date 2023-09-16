##Calculadora Simples
##Peça ao usuário para inserir dois números e uma operação (+, -, *, /).
##Realize a operação e exiba o resultado.


print("==========================================================")
print("===========CAUCULADORA ZICA VERSION PROPLUS===============")
print("==========================================================")


numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
operacao = input("Digite o simbolo da operação: (+ soma) (- subtração) (* mutiplicação) (/ divisão)")

if operacao == '+':
    resultado = numero1 + numero2
    print(f"Soma dos numero: {numero1} + {numero2} = {resultado}")
elif operacao == '-':
    resultado = numero1 - numero2
    print(f"Subtração dos numeros: {numero1} - {numero2}")
elif operacao == '*':
    resultado = numero1 * numero2
    print(f"Mutiplicação dos numeros: {numero1} * {numero2}")
elif operacao == '/':
    resultado = numero1 / numero2
    print(f"Divisão dos numeros: {numero1} * {numero2}")
else:
    print("Operação invalida")



