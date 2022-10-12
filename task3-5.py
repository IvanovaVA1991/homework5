# 3. Создайте программу для игры в 'Крестики-нолики'
position = []
for i in range(1,10):
    position.append(i)
sign = 'O'
while True:
    if sign == 'O':
        sign = 'X'
    else:
        sign = 'O'
        
    print(f'{position[0]:^5}|{position[1]:^5}|{position[2]:^5}')
    print('------------------')
    print(f'{position[3]:^5}|{position[4]:^5}|{position[5]:^5}')
    print('------------------')
    print(f'{position[6]:^5}|{position[7]:^5}|{position[8]:^5}')
    print('------------------')

    index = int(input(f'\nХод {"игрока" if sign == "X" else "противника"}: '))
    if position[index - 1] == 'X' or position[index - 1] == 'O':
        print('Клетка занята, выберите другую!')
        if sign == 'O':
            sign = 'X'
        else:
            sign = 'O'
    else:
        position[index - 1] = sign
    if \
    position[0] == sign and position[4]== sign and position[8]== sign or\
    position[0] == sign and position[1] == sign and position[2] == sign or\
    position[0] == sign and position[3] == sign and position[6] == sign or \
    position[1] == sign and position[4] == sign and position[7] == sign or \
    position[2] == sign and position[5] == sign and position[8] == sign or \
    position[3] == sign and position[4] == sign and position[5] == sign or \
    position[6] == sign and position[7] == sign and position[8] == sign or \
    position[2] == sign and position[4] == sign and position[6] == sign:
        break
print(f'\nИгра окончена, победил {"игрок" if sign == "X" else "противник"}!')