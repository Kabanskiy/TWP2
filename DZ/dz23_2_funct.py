# Написать функцию, которая определяет количество разрядов введённого целого числа.

chis = int(input())
def Razr(i):
    return len(str(abs(i)))
print(Razr(chis))