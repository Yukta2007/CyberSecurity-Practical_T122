def encrypt(text, key):
    rail = [['\n' for i in range(len(text))]
            for j in range(key)]

    direction_down = False
    row, col = 0, 0

    for char in text:
        if row == 0 or row == key - 1:
            direction_down = not direction_down

        rail[row][col] = char
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    result = ""
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result += rail[i][j]

    return result


def decrypt(cipher, key):
    rail = [['\n' for i in range(len(cipher))]
            for j in range(key)]

    direction_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        rail[row][col] = '*'
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    result = ""
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        result += rail[row][col]
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    return result


text = input("Enter Message: ")
key = int(input("Enter Number of Rails: "))

cipher = encrypt(text, key)
print("Encrypted Message:", cipher)

plain = decrypt(cipher, key)
print("Decrypted Message:", plain)
