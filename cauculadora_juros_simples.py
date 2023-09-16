# cauculo do juros
print("=================================================")
print("============== JUROS MASTER 5000 ================")
print("=================================================")

#variaveis
principal = float(input("Digite o valor principal do investimento: "))
taxa = float(input("Digite a taxa de juros anual em porcetagem por ano: "))
tempo = float(input("Digite o período em anos: "))

#cauculo
caucular_montante = principal + (principal * taxa / 100) * tempo



print(f"O montante final do investimento é: {caucular_montante:.2f}")
