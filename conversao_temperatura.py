print("===============================================================")
print("================== CONVERSOR PLUS 5000 ========================")
print("===============================================================")

print("Conversor de temperatura:  Celsius em Fahrenheit(°F)/Kelvin(K)")


#variaveis 
celsius = float(input("Digite a temperatura em graus Celsius: "))


#parametros de conversão
fahrenheit = (celsius * 1.8) + 32
kelvin = celsius + 273.15


#saída
print(f"A temperatura de {celsius}°c em °F {fahrenheit}")
print(f"A temperatura de {celsius}°c em K {kelvin}")


print("===============================================================")