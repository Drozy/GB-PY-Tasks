# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_encode(text):
    encoding = ''
    prev_char = ''
    count = 1
    if not text:
        return ''
    for char in text:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
    return encoding


def rle_decode(text):
    decode = ''
    count = ''
    for char in text:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


def main():
    data = 'ABBCCKKKKKEDDF'
    zipdata = rle_encode(data)
    print(zipdata)
    print(rle_decode(zipdata))


if __name__ == "__main__":
    main()
