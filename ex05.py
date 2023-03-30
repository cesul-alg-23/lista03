area = float(input('Informe a área da casa: '))

qtdeRejunte = area / 3
qtdeArgamassa = area / 5

msgRejunte = "A quantidade de rejunte necessária é " + str(qtdeRejunte) + "kg"
print(msgRejunte)

msgArgamassa = 'A quantidade de argamassa necessária é {} kg'
print(msgArgamassa.format(qtdeArgamassa))
