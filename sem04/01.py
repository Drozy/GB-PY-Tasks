# Пользователь вводит текст (строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в тексте.

# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure. So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

text = ("She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. " + 
        "So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells")
text = text.replace('.', '').replace(',', '').lower()
my_list = text.split()
print(my_list)
my_set = set(my_list)
print(my_set)
print(len(my_set))

print(len(set(text.replace('.' and ',', '').lower().split())))