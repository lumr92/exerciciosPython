'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o IMC e mostre seu status,
de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida'''

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / altura ** 2
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25:
    print('Você está no PESO IDEAL!')
elif imc >= 25 and imc < 30:
    print('Você está em SOBREPESO!')
elif imc >= 30 and imc < 40:
    print('Você está com OBESIDADE!')
else:
    print('Você está com OBESIDADE MÓRBIDA!')
