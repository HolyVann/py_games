from random import randint

print(
    """\n Правила игры:
 Играть может 1 и более человек, каждый по очереди.
 Выпадает случайня карта от 2 до 11, далее вы отвечаете \"да\" если хотите взять еще карту,
 либо \"стоп\", тогда набирает карты банкир. Для победы необходимо набрать в общей сумме 21, либо набрать больше банкира.
 Если вы набрали больше 21 вы автоматичсеки проигрываете.
"""
)


def players_count():
    global players
    try:
        players = int(input("\n Количество игроков: "))
        if players < 1:
            print("\n Введите число больше нуля!")
            players_count()
    except ValueError:
        print("\n Некорректный ответ!\t Введите целое число!")
        players_count()


def card_bank_16():
    global bank
    global counter_bank
    bank = randint(2, 11)
    bank_cards.append(bank)
    counter_bank += bank


def card_bank_17():
    global counter_player
    global counter_bank
    if counter_bank > 21:
        print("\n Карты банкира:", *bank_cards, "\t Сумма карт банкира:", counter_bank)
        print("\n\n\t Вы выиграли!")
    else:
        if counter_bank >= counter_player:
            print(
                "\n Карты банкира:", *bank_cards, "\t Сумма карт банкира:", counter_bank
            )
            print("\n\n\t Вы проиграли!")
        elif counter_bank < counter_player:
            print(
                "\n Карты банкира:", *bank_cards, "\t Сумма карт банкира:", counter_bank
            )
            print("\n\n\t Вы выиграли!")


def bank_play():
    global bank
    global counter_bank
    if counter_bank <= 16:
        card_bank_16()
        bank_play()
    elif counter_bank >= 17:
        card_bank_17()


def stop_answer():
    print("\n\n\t Играет банкир")
    card_bank_16()
    bank_play()


def answer_player():
    global answer
    if answer == "да":
        positive_answer()
    elif answer == "стоп":
        stop_answer()
    else:
        not_correct_answer()


def not_correct_answer():
    global answer
    answer = input("\n Некорректный ответ!\t Ваш ответ: ")
    answer_player()


def positive_answer():
    global counter_player
    global answer
    player_card = randint(2, 11)
    print(
        "\n\n Ваша карта:", player_card, "\t Сумма карт:", counter_player + player_card
    )
    counter_player += player_card
    if counter_player == 21:
        print("\n\n Победа! Вы набрали 21 очко")
    elif counter_player > 21:
        print("\n\n Перебор карт. Вы проиграли!")
    else:
        answer = input("\n Берете карту? \t Ваш ответ: ")
        answer_player()


if __name__ == "__main__":
    players_count()
    for player in range(players):
        bank_cards = []
        counter_bank = 0
        counter_player = 0
        print(f"\n\n\n\t {player + 1}-й игрок")
        positive_answer()

    print("\n\n\t Игра окончена!\n")
