from random import randint
print('Nesse jogo quando aparecer a opção [s/n], responda "s" para sim e "n" para não')
print('Vamos começar o jogo de Craps. Você tem 42 fichas.')
fichas = 42
continua_jogando = 's'
while continua_jogando =='s':
    print('Fase de Come Out')
    pass_line_bet = str(input('Você gostaria de fazer uma aposta Pass Line Bet? [s/n]\n'))
    while pass_line_bet not in 'sn':
        pass_line_bet = str(input('Você gostaria de fazer uma aposta Pass Line Bet? [s/n]\n'))
    if pass_line_bet == 's':
        fichas_pass_line_bet = int(input('Quantas fichas gostaria de apostar em Pass Line Bet?\n'))
        fichas = fichas - fichas_pass_line_bet
    while fichas < 0:
        fichas = fichas + fichas_pass_line_bet
        fichas_pass_line_bet = int(input('Você não tem fichas suficientes. Tente novamente.\n'))
        fichas = fichas - fichas_pass_line_bet
        print('Suas fichas: {}'.format(fichas))
    field = str(input('Você gostaria de fazer uma aposta em Field? [s/n]\n'))
    while field not in 'sn':
        field = str(input('Você gostaria de fazer uma aposta Field? [s/n]\n'))
    if field == 's':
        fichas_field = int(input('Quantas fichas gostaria de apostar em Field?\n'))
        fichas = fichas - fichas_field
    while fichas < 0:
        fichas = fichas + fichas_field
        fichas_field = int(input('Você não tem fichas suficientes. Tente novamente.\n'))
        fichas = fichas - fichas_field
        print('Suas fichas: {}'.format(fichas))
    any_craps = str(input('Você gostaria de fazer uma aposta Any Craps? [s/n]\n'))
    while any_craps not in 'sn':
        any_craps = str(input('Você gostaria de fazer uma aposta Any Craps? [s/n]\n'))
    if any_craps == 's':
        fichas_any_craps = int(input('Quantas fichas você quer apostar em Any Craps?\n'))
        fichas = fichas - fichas_any_craps
    while fichas < 0:
        fichas = fichas + fichas_any_craps
        fichas_any_craps = int(input('Você não tem fichas suficiente, tente novamente.\n'))
        fichas = fichas - fichas_any_craps
        print('Suas fichas: {}'.format(fichas))
    twelve = str(input('Você gostaria de fazer uma aposta em Twelve? [s/n]\n '))
    while twelve not in 'ns':
        twelve = str(input('Você gostaria de fazer uma aposta em Twelve? [s/n]\n '))
    if twelve == 's':
        fichas_twelve = int(input('Quantas fichas você quer apostar em Twelve?\n'))
        fichas = fichas - fichas_twelve
    while fichas < 0:
        fichas = fichas + fichas_twelve
        fichas_twelve = int(input('Você não tem fichas suficiente, tente novamente.\n'))
        fichas = fichas - fichas_twelve
        print('Suas fichas: {}'.format(fichas))

    d1 = randint(1, 6)
    d2 = randint(1, 6)
    sd = d1 + d2
    print('Rolagem de dados:\nPrimeiro dado - {}\nSegundo dado - {}\nSoma - {}'.format(d1, d2, sd))

    if field == 's':
        if sd == 3 or sd == 4 or sd == 9 or sd == 10 or sd == 11:
            fichas = fichas + 2 * fichas_field
            print('Você venceu no Field, recuperou suas {} fichas e ganhou a mais a mesma quantidade.'.format(fichas_field))
            print('Suas fichas: {}'.format(fichas))
        elif sd == 2:
            fichas = fichas + 3 * fichas_field
            print('Você venceu no Field, recuperou suas {} fichas e ganhou a mais o dobro dessa quantidade.'.format(fichas_field))
            print('Suas fichas: {}'.format(fichas))
        elif sd == 12:
            fichas = fichas + 4 * fichas_field
            print('Você venceu no Field, recuperou suas {} fichas e ganhou a mais o triplo dessa quantidade.'.format(fichas_field))
            print('Suas fichas: {}'.format(fichas))
        else:
            print('Você perdeu no Field.')
    if any_craps == 's':
        if sd == 3 or sd == 2 or sd == 12:
            fichas = fichas + 8 * fichas_any_craps
            print('Você venceu no Any Craps, recuperou suas {} fichas e ganhou a mais sete vezes a mesma quantidade.'.format(fichas_any_craps))
            print('Suas fichas: {}'.format(fichas))
        else:
            print('Você perdeu no Any Craps.')

    if twelve == 's':
        if sd == 12:
            fichas = fichas + 31 * fichas_twelve
            print('Você venceu no Twelve, recuperou suas {} fichas e ganhou a mais trinta vezes a mesma quantidade.'.format(fichas_twelve))
            print('Suas fichas: {}'.format(fichas))
        else:
            print('Você perdeu no Twelve.')
    if pass_line_bet == 's':
        if sd == 7 or sd == 11:
            fichas = fichas + 2 * fichas_pass_line_bet
            print('Você venceu no Pass Line Bet, recuperou suas {} fichas e ganhou a mais a mesma quantidade.'.format(fichas_pass_line_bet))
            print('Suas fichas: {}'.format(fichas))
        elif sd != 2 and sd != 3 and sd != 12:
            p = sd
            sd = 0
            while sd != p:
                print('Fase de Point.\nVocê não venceu e nem perdeu ainda no Pass Line Bet, seu valor de Point é {}.'.format(p))
                print('Suas fichas: {}'.format(fichas))
                field = str(input('Você gostaria de fazer uma aposta Field? [s/n]\n'))
                while field not in 'ns':
                    field = str(input('Você gostaria de fazer uma aposta Field? [s/n]\n'))
                if field == 's':
                    fichas_field = int(input('Quantas fichas você quer apostar em Field?\n'))
                    fichas = fichas - fichas_field
                while fichas < 0:
                    fichas = fichas + fichas_field
                    fichas_field = int(input('Você não tem fichas suficiente, tente novamente.\n'))
                    fichas = fichas - fichas_field
                    print('Suas fichas: {}'.format(fichas))
                any_craps = str(input('Você gostaria de fazer uma aposta Any Craps? [s/n]\n'))
                while any_craps not in 'ns':
                    any_craps = str(input('Você gostaria de fazer uma aposta Any Craps? [s/n]\n'))
                if any_craps == 's':
                    fichas_any_craps = int(input('Quantas fichas você quer apostar em Any Craps?\n'))
                    fichas = fichas - fichas_any_craps
                while fichas < 0:
                    fichas = fichas + fichas_any_craps
                    fichas_any_craps = int(input('Você não tem fichas suficiente, tente novamente.\n'))
                    fichas = fichas - fichas_any_craps
                    print('Suas fichas: {}'.format(fichas))
                twelve = str(input('Você gostaria de fazer uma aposta Twelve? [s/n]\n'))
                while twelve not in 'ns':
                    twelve = str(input('Você gostaria de fazer uma aposta Twelve? [s/n]\n'))
                if twelve == 's':
                    fichas_twelve = int(input('Quantas fichas você quer apostar em Twelve?\n'))
                    fichas = fichas - fichas_twelve
                while fichas < 0:
                    fichas = fichas + fichas_twelve
                    fichas_twelve = int(input('Você não tem fichas suficiente, tente novamente.\n'))
                    fichas = fichas - fichas_twelve
                    print('Suas fichas: {}'.format(fichas))

                d1 = randint(1, 6)
                d2 = randint(1, 6)
                sd = d1 + d2
                print('Rolagem de dados:\nPrimeiro dado - {}\nSegundo dado - {}\nSoma - {}'.format(d1, d2, sd))

                if field == 's':
                    if sd == 3 or sd == 4 or sd == 9 or sd == 10 or sd == 11:
                        fichas = fichas + 2 * fichas_field
                        print('Você venceu no Field, recuperou suas {} fichas e ganhou a mais a mesma quantidade.'.format(fichas_field))
                        print('Suas fichas: {}'.format(fichas))
                    elif sd == 2:
                        fichas = fichas + 3 * fichas_field
                        print('Você venceu no Field, recuperou suas {} fichas e ganhou a mais o dobro dessa quantidade.'.format(fichas_field))
                        print('Suas fichas: {}'.format(fichas))
                    elif sd == 12:
                        fichas = fichas + 4 * fichas_field
                        print('Você venceu no Field, recuperou suas {} fichas e ganhou a mais o triplo dessa quantidade.'.format(fichas_field))
                        print('Suas fichas: {}'.format(fichas))
                    else:
                        print('Você perdeu no Field.')

                if any_craps == 's':
                    if sd == 3 or sd == 2 or sd == 12:
                        fichas = fichas + 8 * fichas_any_craps
                        print('Você venceu no Any Craps, recuperou suas {} fichas e ganhou a mais sete vezes a mesma quantidade.'.format(fichas_any_craps))
                        print('Suas fichas: {}'.format(fichas))
                    else:
                        print('Você perdeu no Any Craps.')

                if twelve == 's':
                    if sd == 12:
                        fichas = fichas + 31 * fichas_twelve
                        print('Você venceu no Twelve, recuperou suas {} fichas e ganhou a mais trinta vezes a mesma quantidade.'.format(fichas_twelve))
                        print('Suas fichas: {}'.format(fichas))
                    else:
                        print('Você perdeu no Twelve.')

                if sd == 7:
                    p = 7

            if sd == 7:
                print('Você perdeu no Pass Line Bet.')
            else:
                fichas = fichas + 2 * fichas_pass_line_bet
                print('Você venceu no Pass Line Bet, recuperou suas {} fichas e ganhou a mais a mesma quantidade.'.format(fichas_pass_line_bet))
                print('Suas fichas: {}'.format(fichas))
        else:
            print('Você perdeu no Pass Line Bet.')
            print('Suas fichas: {}'.format(fichas))
    continua_jogando = str(input('Você quer continuar a jogar? [s/n]\n'))
    if fichas == 0:
        print('Infelizmente você não tem mais fichas, por isso estamos encerrando o jogo.')
        continua_jogando = 'n'

print('Obrigado por jogar, seu total de fichas ao final é: {}'.format(fichas))