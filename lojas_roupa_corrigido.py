print('==========Cauculadora de valor de VENDA==========')
print('================A VISTA || A PRAZO===============')
print('==================MASTER GOLD PRO================')

formaPagamento = int(input('Qual será a forma de pagamento(1=avista/2=aprazo):  '))
valorVenda = int(input('Digite o valor total da venda: '))



0

if formaPagamento == 1:

    if valorVenda <= 500:
        aplicaDesconto = valorVenda * .10
        print(f'Novo valor é de {aplicaDesconto}')

    elif valorVenda > 500 and valorVenda < 1000:
        aplicaDesconto = valorVenda * .15
        print(f'{valorVenda} com desconto de 15% = {aplicaDesconto}')

else:
        aplicaDesconto = valorVenda * .20
