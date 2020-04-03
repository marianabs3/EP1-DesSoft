import random
fichas = int(input('Vamos começar o jogo de Craps. Com quantas fichas você gostaria de começar? '))
while fichas <= 0:
    fichas = int(input('Vamos começar o jogo de Craps. Com quantas fichas você gostaria de começar? '))
continua_jogando = 's'
while continua_jogando=='s':
    print('Fase de Come Out')
    pass_line_bet = srt(input('Você gostaria de fazer uma aposta Pass Line Bet? [s/n] '))
    while pass_line_bet not in 'sn':
        pass_line_bet = srt(input('Você gostaria de fazer uma aposta Pass Line Bet? [s/n] '))
        if pass_line_bet == 's':
            fichas_pass_line_bet = int(input('Quantas fichas gostaria de apostar em Pass Line Bet? '))
            fichas = fichas - fichas_pass_line_bet
        while fichas < 0:
            fichas = fichas + fichas_pass_line_bet
            fichas_pass_line_bet = int(input('Você não tem fichas suficientes. Tente novamente. '))
            fichas = fichas - fichas_pass_line_bet
            print('Suas fichas: {}'.format(fichas))
    field = srt(input('Você gostaria de fazer uma aposta em Field?[s/n] '))
    while field not in 'sn':
        field = srt(input('Você gostaria de fazer uma aposta Pass Line Bet? [s/n] '))
        if field == 's':
            fichas_field = int(input('Quantas fichas gostaria de apostar em Pass Line Bet? '))
            fichas = fichas - fichas_field
        while fichas < 0:
            fichas = fichas + fichas_field
            fichas_field = int(input('Você não tem fichas suficientes. Tente novamente. '))
            fichas = fichas - fichas_field
            print('Suas fichas: {}'.format(fichas))
    twelve = str(input('Você gostaria de fazer uma aposta em Twelve?[s/n] '))
    while twelve not in 'ns':
        twelve = str(input('Você gostaria de fazer uma aposta em Twelve?[s/n] '))
    if twelve == 's':
        fichas_twelve = int(input('Quantas fichas você quer apostar em Twelve? '))
        fichas = fichas - fichas_twelve
        
    



