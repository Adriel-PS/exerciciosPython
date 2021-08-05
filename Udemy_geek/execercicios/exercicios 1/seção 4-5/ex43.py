valor_produto=float(input("informe o valor do produto"))
valor_desconto=valor_produto-((valor_produto/100)*10)
valor_parcelado=valor_produto/3
comissao=(valor_desconto/100)*5
comissao2=(valor_produto/100)*5
print("o valor com desconto",valor_desconto)
print("o valor de cada parcela , caso parcelado em 3 vezes",string(valor_parcelado))
print("o valor da comissao caso seja pago avista ",comissao)
print("o valor da comissao caso seja pago em 3 vezes",comissao2)