print('==========Cauculadora de valor de VENDA==========')
print('================A VISTA || A PRAZO===============')
print('==================MASTER GOLD PRO================')

formaPagamento = int(input('Qual será a forma de pagamento(1=avista/2=aprazo):  '))
valorVenda = int(input('Digite o valor total da venda: '))



if formaPagamento == 1:
    if valorVenda <= 500:
        aplicaDesconto  = valorVenda * .10
        valorAvista = valorVenda - aplicaDesconto
        print(f'R${valorVenda} com 10% de desconto R${valorAvista}')
        
    elif valorVenda > 500 and valorVenda < 1000:
        aplicaDesconto = valorVenda * .15
        valorAvista = valorVenda - aplicaDesconto
        print(f'R${valorVenda} com 15% de desconto R${valorAvista}')
else:
        aplicaDesconto = valorVenda * .20
        valorAvista = valorVenda - aplicaDesconto
        print(f'R${valorVenda} com 20% de desconto R${valorAvista}')

if formaPagamento == 2:       
    if valorVenda <= 800:
        print('Parcelamento disponivel em até 5x sem juros') 
        print(f'R${valorVenda} 1 x sem juros de R$ {valorVenda}')
        print(f'R${valorVenda} 2 x sem juros de R$ {valorVenda / 2}')
        print(f'R${valorVenda} 3 x sem juros de R$ {valorVenda / 3}')
        print(f'R${valorVenda} 4 x sem juros de R$ {valorVenda / 4}')
        print(f'R${valorVenda} 5 x sem juros de R$ {valorVenda / 5}')

    elif valorVenda > 800:
        print('Parcelamento em até 10x sem juros') 
        print(f'R${valorVenda} 1 x sem juros de R$ {valorVenda}')
        print(f'R${valorVenda} 2 x sem juros de R$ {valorVenda / 2:.2f}')
        print(f'R${valorVenda} 3 x sem juros de R$ {valorVenda / 3:.2f}')
        print(f'R${valorVenda} 4 x sem juros de R$ {valorVenda / 4:.2f}')
        print(f'R${valorVenda} 5 x sem juros de R$ {valorVenda / 5:.2f}')
        print(f'R${valorVenda} 6 x sem juros de R$ {valorVenda / 6:.2f}')
        print(f'R${valorVenda} 7 x sem juros de R$ {valorVenda / 7:.2f}')
        print(f'R${valorVenda} 8 x sem juros de R$ {valorVenda / 8:.2f}')
        print(f'R${valorVenda} 9 x sem juros de R$ {valorVenda / 9:.2f}')
        print(f'R${valorVenda} 10 x sem juros de R$ {valorVenda / 10:.2f}')
##Juros aparir de 11 parcelas
        taxaJuros = 0.05
        valorTotal = valorVenda * 1.05
        valorParcela = valorTotal / 11
        print(f'11 x com juros de R${valorParcela:.2f} no valor total R${valorTotal}')
        taxaJuros = 0.065 
        valorTotal = valorVenda * 1.065
        valorParcela = valorTotal / 12
        print(f'12 x com juros de R${valorParcela:.2f} no valor total R${valorTotal}')
        taxaJuros = 0.07
        valorTotal = valorVenda * 1.07
        valorParcela = valorTotal / 13
        print(f'13 x com juros de R${valorParcela:.2f} no valor total R${valorTotal}')
        taxaJuros = 0.09
        valorTotal = valorVenda * 1.09
        valorParcela = valorTotal / 14
        print(f'14 x com juros de R${valorParcela:.2f} no valor total R${valorTotal}')
        taxaJuros = 0.095
        valorTotal = valorVenda * 1.095
        valorParcela = valorTotal / 15
        print(f'14 x com juros de R${valorParcela:.2f} no valor total R${valorTotal}')