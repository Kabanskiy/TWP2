# написать ф-ю, которая генерирует словарь, где ключ - это буква строки, а значение - это число,
# сколько раз повторяется данная буква в этой строке. Строку пользователь видит программно

stroka = input()

def fun_generation(stroka):
    dict1 = {}
    for i in stroka:
        dict1[i] = stroka.count(i)
    return dict1
print(fun_generation(stroka))