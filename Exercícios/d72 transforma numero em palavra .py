num = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
escolha = int(input('escolha um número entre 0  e 20: '))
confirmacao = False

while confirmacao == False:  
    if escolha > 20  or escolha <0:
        escolha = int(input('número invalido,tente novamente '))
    else:
        confirmacao = True
        print (num [escolha])