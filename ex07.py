valorDuplicata = float(input('Informe o valor da duplicata: '))
diasAtraso = int(input('Informe os dias de atraso: '))

multaPorDia = 0.05 * valorDuplicata
totalMulta = multaPorDia * diasAtraso

total = valorDuplicata + totalMulta

print(f'O total a pagar é R$ {total:.2f}')
