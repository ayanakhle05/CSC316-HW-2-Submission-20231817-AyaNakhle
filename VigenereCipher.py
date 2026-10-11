import math

#Vigenere encryption and decryption
def vigenere(text, key, decrypt=False):
    result = ""
    key = key.upper()
    j = 0

    for char in text:
        if char.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            # Convert letters to numbers
            p = ord(char.upper()) - ord("A")
            k = ord(key[j % len(key)]) - ord("A")

            if decrypt:
                value = (p - k) % 26
            else:
                value = (p + k) % 26

            # Convert the number back to a letter
            letter = chr(value + ord("A"))
            result += letter if char.isupper() else letter.lower()
            j += 1
        else:
            result += char

    return result

def read_order(message):
    while True:
        try:
            order = [int(x.strip()) for x in input(message).split(",")]

            if order and sorted(order) == list(range(1, len(order) + 1)):
                return order

            print("Error: Enter each number from 1 to N exactly once.")

        except ValueError:
            print("Error: Enter numbers separated by commas, like 3,1,2.")


def read_positive_number(message):
    while True:
        try:
            number = int(input(message))

            if number > 0:
                return number

            print("Error: Enter a number greater than zero.")

        except ValueError:
            print("Error: Enter a valid whole number.")

def read_round_type(round_number):
    while True:
        kind = input(
            f"Round {round_number} - choose Row or Column: "
        ).strip().lower()

        if kind in ("row", "column"):
            return kind

        print("Error: Enter Row or Column.")

def row_permutation(text, order, decrypt=False):
    if not text:
        return ""

    count = len(order)
    width = math.ceil(len(text) / count)

    rows = [text[i * width:(i + 1) * width]
            for i in range(count)]

    if not decrypt:
        return "".join(rows[i - 1] for i in order)

    lengths = [len(rows[i]) for i in range(count)]
    original = [""] * count
    position = 0

    for i in order:
        length = lengths[i - 1]
        original[i - 1] = text[position:position + length]
        position += length

    return "".join(original)

def column_permutation(text, order, decrypt=False):
    if not text:
        return ""

    width = len(order)
    row_count = math.ceil(len(text) / width)
    remainder = len(text) % width

    lengths = []
    for c in range(width):
        if remainder == 0 or c < remainder:
            lengths.append(row_count)
        else:
            lengths.append(row_count - 1)

    if not decrypt:
        grid = [text[i:i + width]
                for i in range(0, len(text), width)]

        result = ""
        for c in order:
            for row in grid:
                if c - 1 < len(row):
                    result += row[c - 1]

        return result

    columns = [""] * width
    position = 0

    for c in order:
        length = lengths[c - 1]
        columns[c - 1] = text[position:position + length]
        position += length

    result = ""
    for r in range(row_count):
        for c in range(width):
            if r < len(columns[c]):
                result += columns[c][r]

    return result


#Main program
print("***** VIGENERE CIPHER *****")

while True:
    mode = input("Choose Encrypt or Decrypt: ").strip().lower()

    if mode in ("encrypt", "decrypt"):
        break

    print("Error: Enter Encrypt or Decrypt.")

text = input("Enter your text: ")

while True:
    key = input("Enter the secret keyword: ").strip()

    if key and all(c.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                   for c in key):
        break

    print("Error: The keyword must contain English letters only.")

round_count = read_positive_number(
    "How many permutation rounds do you want? "
)

rounds = []

for i in range(1, round_count + 1):
    kind = read_round_type(i)
    order = read_order(
        f"Enter the {kind} order for round {i} (example 3,1,2): "
    )
    rounds.append((kind, order))


if mode == "encrypt":
    #First round: Vigenere encryption
    result = vigenere(text, key)
    print("\nAfter Vigenere:", result)

    #Apply each permutation round in order
    for i, (kind, order) in enumerate(rounds, start=1):
        if kind == "row":
            result = row_permutation(result, order)
        else:
            result = column_permutation(result, order)

        print(f"After round {i} ({kind}):", result)

    print("\nFinal ciphertext:", result)

else:
    #Reverse all permutation rounds in reverse order
    result = text

    for i in range(len(rounds) - 1, -1, -1):
        kind, order = rounds[i]

        if kind == "row":
            result = row_permutation(result, order, True)
        else:
            result = column_permutation(result, order, True)

        print(f"After reversing round {i + 1} ({kind}):", result)

    #Vigenere decryption
    result = vigenere(result, key, True)
    print("\nOriginal plaintext:", result)
