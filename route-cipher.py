with open(r"C:\Users\ollzh\Desktop\platonus4\cryptoanaliz\lab3\data.txt", "r") as f:
    text = f.read()
    text_len = len(text)

print('Текст:', text, '\nКоличество знаков:', text_len)

n = int(input('Введите n(столбцы): '))


arr = []


def encrypt(txt):
    # добавляем звездочки для нехватки символов
    while len(txt) % n != 0:
        txt += '*'

    sub_arr = []
    for i in range(len(txt)):
        sub_arr.append(txt[i])
        if (i + 1) % n == 0:
            arr.append(sub_arr)
            sub_arr = []
    print('Таблица из текста: ')
    for i in range(len(arr)):
        print(arr[i])

    des = 'down'
    res = ''
    while len(arr[0]) > 0:
        if des == 'down':
            for i in range(len(arr)):
                res += arr[i][0]
                arr[i].pop(0)
                des = 'right'
        elif des == 'right':
            for i in range(len(arr[0])):
                res += arr[len(arr) - 1][i]
            arr.pop()
            des = 'top'
        elif des == 'top':
            for i in range(len(arr) - 1, -1, -1):
                res += arr[i][len(arr[0]) - 1]
                arr[i].pop(len(arr[0]) - 1)
                des = 'left'
        elif des == 'left':
            for i in range(len(arr[0]) - 1, - 1, -1):
                res += arr[0][i]
            arr.pop(0)
            des = 'down'
        # print(res)
        # for i in range(len(arr)):
        #     print(arr[i])
    return res


encrypted_text = encrypt(text)
print('Зашифрованный текст:', encrypted_text)


