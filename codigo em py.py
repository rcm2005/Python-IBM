
#antes disso é necessário uma estrutura que ative o leitor de composição do ar e receba o output dele, fornecendo o índice de poluição do ar
#a media deve se encontrar em uma escala de 1 a 10 sendo 1 o ar mais limpo e 10 o ar mais poluido
#a escala funciona classificando os valores de 1 a 3.33 o ar pouco poluído, de 3.33 a 6.66 o ar com poluição média, e entre 6.66 a 10 o ar muito poluído


print('__')
print('_ AXION GREEN ')
print('__')
print('\nAQUI ESTA NOSSO CODIGO EM VERSÃO PITHON')
print('\nUTILIZAMOS FERRAMENTAS VISTAS EM AULA')

contador = 0
while contador < 1000:
    contador += 1
    
    ar = int(input('Media da qualidade do ar fornecida pelo sensor: '))

    #console no arduino é o LCD mas qui pode ser o propio console



    if 1 <= ar < 3:
        ar = 3
        led = 'VERDE'
        buzzer = 'Notone'
    elif  3 <= ar < 6:     #estrutura que nomeia as classes
        ar = 6              # e define qual é o comportamento das leds e do buzzer
        led = 'AMARELO'
        buzzer = 'Notone'      
    elif 6 <= ar <= 10:
        ar = 9
        led = 'VERMELHO'
        buzzer = 'Tone'
    else:
        print("digite um numero entre 1 e 10")

    if ar == 3:
        print('Ar com poluição baixa')
        print(f'cor do led: {led}')           #verificando a variável ar e exibindo o comportamento dos componenes
        print(f'Buzzer: {buzzer}')             
    elif ar == 6:
        print('Ar com poluição média')
        print(f'cor do led: {led}')
        print(f'Buzzer: {buzzer}')
    elif ar == 9:
        print('Ar com poluição crítica!')
        print(f'cor do led: {led}')
        print(f'Buzzer: {buzzer}')
    else:
        print('erro')
    opcao = int(input('escolha uma opção \n (1) continuar \n (2) sair \n'))
    if opcao == 2:
        print('sair do codigo')          #oferecendo ao usuário a opção de continuar rodando o programa ou sair caso já esteja satisfeito
        break      
    

#A partir daqui é necessária uma estrutura que seja capaz de ativar os diferentes LEDs da protoboard, seguindo a escala de índice de poluição
