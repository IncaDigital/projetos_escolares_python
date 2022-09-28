import opeaB
num1 = int(input('Digite primer valor: '))
num2 = int(input('Digite segundo valor: '))

resultadoSuma = opeaB.suma(num1, num2)
resultadoResta = opeaB.resta(num1, num2)
resultadoMultiplica = opeaB.multiplica(num1, num2)
resultadoDivide = opeaB.divide(num1, num2)
print(f'O resultado de la suma es: {resultadoSuma}')
print(f'O resultado de la resta es: {resultadoResta}')
print(f'O resultado de la multiplicacíon es: {resultadoMultiplica}')
print(f'O resultado de la división es: {resultadoDivide}')