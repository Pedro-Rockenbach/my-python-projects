def cinema(assentos):
    """Cria um sistema de reserva de assentos de um cinema"""

    #Cria uma variavel para valor presente na chave do dicionario
    disponiveis = assentos['disponiveis']
    indisponiveis = assentos['indisponiveis']
    reservados = assentos['reservados']

    #informa ao usuario os assentos que estao disponiveis
    print(f'Assentos disponiveis: {disponiveis}\n')

    #loop permite escolher mais de um assento
    while True:
        escolha_assento = str(input('Digite sua escolha de assento: ')).upper().strip()
        #verifica a disponibilidade do assento
        if escolha_assento in disponiveis:
            disponiveis.remove(escolha_assento)
            indisponiveis.append(escolha_assento)
            reservados.append(escolha_assento)
            print(f'Assento {escolha_assento} reservado com sucesso!')
        elif escolha_assento in reservados:
            print('Você já reservou esse assento.')
        else:
            print('Esse assento esta indisponivel :(')
        cont = str(input('\nDeseja reservar mais algum assento? [s/n] ')).lower().strip()
        if cont == 'n':
            break

    #atualiza o dicionario a partir da escolha do usuario
    assentos['disponiveis'] = disponiveis
    assentos['indisponiveis'] = indisponiveis
    assentos['reservados'] = reservados

    #informa o usuario a escolha dos assentos e uma mensagem de despedida
    print('Assentos reservados: ', end='')
    for r in assentos['reservados']:
        print(f'{r}', end=' ')
    print('\nObrigado pela reserva. Bom filme !')

    return assentos


#dicionario contendo o status dos assentos
assentos = {'disponiveis': ['A1', 'A2', 'B3', 'B4', 'B5'],
            'indisponiveis': ['B1', 'B2', 'A3', 'A4', 'A5'],
            'reservados': []}

#chama a funcao cinema
sistema = cinema(assentos)

print('\n\n\n')

print('status final do sistema: ')
for k, v in assentos.items():
    print(f'{k} : {v}')
