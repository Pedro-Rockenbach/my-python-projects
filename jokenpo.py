from random import choice
import emoji
from time import sleep

def jokenpo():

    options = [pedra, papel, tesoura]
    pc_choice = choice(options)

    player_choice = int(input(emoji.emojize('1 - :pedra:\n'
                                            '2 - :rolo_de_papel:\n'
                                            '3 - :tesoura:\n'
                                            '* \033[34mSua escolha:'
                                            ' \033[m', language='pt')))

    if player_choice == 1:
        player_choice = pedra

    if player_choice == 2:
        player_choice = papel

    if player_choice == 3:
        player_choice = tesoura

    sleep(1)
    print('Escolha registrada.\n')
    sleep(1)
    print('\033[32mJO\033[m\n')
    sleep(1)
    print('\033[31mKEN\033[m\n')
    sleep(1)
    print('\033[36mPO\033[m\n')
    sleep(1)

    print(f'Sua escolha -> {player_choice} x {pc_choice} <- Escolha do '
          f'computador\n')
    sleep(2)

    if player_choice == pc_choice:
        print('DEU EMPATE !')
    elif player_choice == pedra and pc_choice == tesoura:
        print('VOCÊ VENCEUUU {}\n'.format(confetti * 6))
    elif player_choice == papel and pc_choice == pedra:
        print('VOCÊ VENCEUUU {}\n'.format(confetti * 6))
    elif player_choice == tesoura and pc_choice == papel:
        print('VOCÊ VENCEUUU {}\n'.format(confetti * 6))
    else:
        print('VOCÊ PERDEU !\n\n')

    sleep(3)


pedra = emoji.emojize(':pedra:', language='pt')
papel = emoji.emojize(':rolo_de_papel:', language='pt')
tesoura = emoji.emojize(':tesoura:', language='pt')
confetti = emoji.emojize(':confetti_ball:', language='en')

print('-=' * 15)
print('\033[33mVAMOS JOGAR JOKENPO ?!\033[m'.center(35))
print('-=' * 15)

while True:
    jokenpo()
    if str(input('Deseja jogar novamente ? [s/n]')).lower() == 'n':
        print(emoji.emojize('\nOBRIGADO POR JOGAR :red_heart:'
                            ,language='en'))
        sleep(2)
        break
