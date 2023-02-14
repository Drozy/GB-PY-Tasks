# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1


def changeMaxToMin(rating: list):
    new_rating = []
    mx = max(rating)
    mn = min(rating)
    for i in range(len(rating)):
        if rating[i] == mx:
            new_rating.append(mn)
        else:
            new_rating.append(rating[i])
    return new_rating


rating = [1, 3, 3, 3, 4]
new_rating = changeMaxToMin(rating)
print(rating)
print(new_rating)
