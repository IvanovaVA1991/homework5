# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв""
text = ['валоии', 'ыдклкполабвмл', 'абв', 'щлыват', 'зщоа', 'ывдслот', 'до']
elem = input('Введите искомую комбинацию ')
print(elem)
result = []
for i in range(len(text)):
    if elem not in text[i]:
        result.append(text[i])
print(result)

