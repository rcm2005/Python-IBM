
#antes disso é necessário uma estrutura que ative o leitor de composição do ar e receba o output dele, fornecendo o índice de poluição do ar
#a media deve se encontrar em uma escala de 1 a 10 sendo 1 o ar mais limpo e 10 o ar mais poluido
#a escala funciona classificando os valores de 1 a 3.33 o ar pouco poluído, de 3.33 a 6.66 o ar com poluição média, e entre 6.66 a 10 o ar muito poluído


print('__')
print('_ AXION GREEN ')
print('__')
print('\nAQUI ESTA NOSSO CODIGO EM VERSÃO PITHON')
print('\nUTILIZAMOS FERRAMENTAS VISTAS EM AULA')

contador = 0
while contador < 100:
    contador += 1

    ar = int(input('Media da qualidade do ar fornecida pelo sensor: '))

    #console no arduino é o LCD mas qui pode ser o propio console



    if 1 >= ar > 3:
        ar = 3
        led = 'VERMELHO'
        buzzer = 'LIGADO'
    elif  3 >= ar > 6:     #estrutura que nomeia as classes
        ar = 6
        led = 'AMARELO'
        buzzer = 'Notone'                    #para que o match case consiga interpretar
    elif 6 >= ar >= 10:
        ar = 9
        led = 'VERDE'
        buzzer = 'Tone'


    if ar == 3:
        print('Ar com poluição baixa')
        print(f'cor do led: {led}')
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




#A partir daqui é necessária uma estrutura que seja capaz de ativar os diferentes LEDs da protoboard, seguindo a escala de índice de poluição
