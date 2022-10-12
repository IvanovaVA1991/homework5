n = int(input("Ввести общее количество конфет "))
m = int(input("Ввести максимальное количество за 1 ход "))
import random
player = random.randint(1, 2)
print(f"Первым ходит игрок {player}")  # 1 - человек, 2 - бот
while n>m:
    if player == 1:
        if n > m:
            k = int(input("Ход игрока 1: введите количество конфет "))
            n = n-k
            print(f"Осталось {n} конфет")
        else:
            k = n
            break
        player += 1
    else:
        if n > m:
            k = random.randint(1, 28)
            print(f"Игрок 2 взял {k} конфет")
            n = n-k
            print(f"Осталось {n} конфет") 
        else:
            k = n
            break
        player -= 1
print(f"Игрок {player} забирает {n} конфет и выигрывает!")