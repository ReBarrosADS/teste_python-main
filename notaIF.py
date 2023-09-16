##Classificação de Notas
##Peça ao usuário para inserir uma nota de 0 a 100 e, em seguida, classifique-a como
##"A" (90-100), "B" (80-89), "C" (70-79), "D" (60-69) ou "F" (abaixo de 60).


nota = float(input("Digite a nota que deseja classificar: "))

if nota >= 90 and nota <=100:
    print(f"Sua nota {nota} é classificação = 'A'")
elif nota < 90 and nota >= 80:
    print(f"Sua nota {nota} é classificação = 'B'")
elif nota < 80 and nota >= 69:
    print(f"Sua nota {nota} é classificação = 'C'")
elif nota < 70 and nota >= 59:
    print(f"Sua nota {nota} é classicação = 'D'")
elif nota < 60 and nota >= 0:
    print(f"Sua nota {nota} é classificação = 'F'")
else:
    print("Nota invalida")
