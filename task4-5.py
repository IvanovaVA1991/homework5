# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc
pathRead = 'text1.txt'
pathWrite = 'file2.txt'
with open(pathRead, 'r') as data:
    text1 = data.readline()
    text2 = data.readline()
print(text1)
print(text2)
result1 = ''
prev_elem = ''
count = 1
for elem in text1:
    if elem != prev_elem:
        if prev_elem:
            result1 += str(count) + prev_elem
        count = 1
        prev_elem = elem
    else:
        count += 1
else:
    result1 += str(count) + prev_elem
print(result1)
result2 = ''
count = ''
for elem in text2:
    if elem.isdigit():
        count += elem
    else:
        result2 += elem * int(count)
        count = ''
print(result2)
with open(pathWrite, 'w') as data:
    data.write(result1)
    data.write('\n')
    data.write(result2)
