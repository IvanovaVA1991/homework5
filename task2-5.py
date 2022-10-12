# 2. Создайте программу для игры с конфетами человек против человека
n = int(input("Ввести общее количество конфет "))
m = int(input("Ввести максимальное количество за 1 ход "))
# print("Ход игрока 1: введите количество конфет ")
# k = n%(m+1)
# n = n-k
# print(k)
import random
player = random.randint(1, 2)
print(f"Первым ходит игрок {player}")
# while n>m+1:
while n>m:
    if player == 1:
        if n > m:
            k = int(input("Ход игрока 1: введите количество конфет "))
    # k = random.randint(1, 29)
            n = n-k
            print(f"Осталось {n} конфет")
        # if n>m:
            
        else:
            k = n
            break
        player += 1
    else:
    # if player == 2:
        if n > m:
            k = int(input("Ход игрока 2: введите количество конфет "))
    # k = m+1-k
            n = n-k
            print(f"Осталось {n} конфет")
        
            
        else:
            k = n
            break
        player -= 1
print(f"Игрок {player} забирает {n} конфет и выигрывает!")