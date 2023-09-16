##4. Cálculo de Bônus Salarial
##Peça ao usuário para inserir seu salário e o tempo de serviço. Se o tempo de serviço
##for superior a 5 anos, conceda um bônus de 5% ao salário.


print('========================================================')
print('===============Cáuculo de Bônos Salarial================')
print('===============-----MEGA START 7000-----================')
print('========================================================')


salario = float(input("Digite o salário: "))
tempoServico = float(input("Digite o tempo trabalho em Anos: "))


if tempoServico >= 5:
    bonusSalario = salario * .05
    novoSalario = salario * 1.05
    print(f'Bônus de de 5% sobre o salario R${salario} é igual R${bonusSalario}')
    print(f'Seu novo salário com bônus é de R${novoSalario} ') 
else:
    print('Tempo de serviço')    
