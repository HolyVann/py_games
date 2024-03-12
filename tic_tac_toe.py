def win(number):       
    print(f'\n\n Выиграл игрок "{number.replace(" ","")}" \n\n\n\t Игра окончена!')
        
def num():
    global i 
    global player
    try:
        if i%2 == 0:
            name = '"O"'
        else:
            name = '"X"'  
        player = int(input(f'\n\n Игрок {name}, номер ячейки: '))
        if 1 > player or player > 9:
            print("\n Некорректный ответ!")
            num()
        if lst[player-1] == " O " or lst[player-1] == " X ":
            print("\n Ячейка занята!")
            num() 
    except ValueError:
        print("\n Некорректный ответ!")
        num() 
        
        
def player_selection():
    global lst
    global flag
    if lst[0] == lst[1] == lst[2]:
        win(lst[0])       
        flag = True
    elif lst[3] == lst[4] == lst[5]:
        win(lst[3])        
        flag = True
    elif lst[6] == lst[7] == lst[8]:
        win(lst[6])
        flag = True
    elif lst[0] == lst[3] == lst[6]:
        win(lst[0])
        flag = True
    elif lst[1] == lst[4] == lst[7]:
        win(lst[1])
        flag = True
    elif lst[2] == lst[5] == lst[8]:
        win(lst[2])
        flag = True
    elif lst[0] == lst[4] == lst[8]:
        win(lst[0])
        flag = True
    elif lst[2] == lst[4] == lst[6]:
        win(lst[2])
        flag = True


if __name__=='__main__':
    lst = ["[1]","[2]","[3]","[4]","[5]","[6]","[7]","[8]","[9]"]
    print("\n\n\t", *lst[:3], "\n\t", *lst[3:6], "\n\t", *lst[6:])
    flag = False
    counter = 0
    for i in range(10):
        if flag:
            break
        if counter == 9:
            print("\n Ничья! \n\n\n\t Игра окончена!\n")
            break
        num()
        if lst[player-1] == " O " or lst[player-1] == " X ":
            print("\n Ячейка занята!")
            num()  
        if i%2 == 0:
            lst[player-1] = " O "
        else:
            lst[player-1] = " X "
        counter += 1
        print("\n\n\t", *lst[:3], "\n\t", *lst[3:6], "\n\t", *lst[6:])
        player_selection()