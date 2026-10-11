# Vigenère Cipher with Multiple Permutation Rounds

## 1. Project Description

This project implements a Vigenère Cipher in Python for encrypting and decrypting text using a secret keyword. It also allows the user to apply multiple row and column permutation rounds to provide additional rearrangement of the text.

The program supports both encryption and decryption and displays the intermediate results after each round.

## 2. Features

- Vigenère encryption and decryption using a secret keyword.
- Conversion of letters into numbers and back into letters using modulo 26.
- Row permutation to rearrange text in different rows.
- Column permutation to rearrange text in different columns.
- Flexible number of permutation rounds.
- User-defined permutation orders.
- Input validation for the operation, keyword, round count, round type, and permutation order.
- Display of intermediate results and the final ciphertext.

## 3. How to Run the Program

1. Open the project in Visual Studio.
2. Open the Python source file.
3. Run the program.
4. Choose `Encrypt` or `Decrypt`.
5. Enter the text.
6. Enter the secret keyword using English letters.
7. Enter the number of permutation rounds.
8. For each round, choose `Row` or `Column`.
9. Enter the permutation order as comma-separated numbers.

For decryption, use the same keyword and the same permutation rounds and orders that were used during encryption.

## 4. Encryption Algorithm

### 4.1 Vigenère Encryption

The `vigenere()` function performs encryption by converting each letter into a number, applying the secret keyword, and converting the result back into a letter.

Each letter is represented by a number from 0 to 25:

- A = 0
- B = 1
- C = 2
- ...
- Z = 25

The encryption formula is:

**C = (P + K) mod 26**

Where:
- `P` is the plaintext letter's numerical value.
- `K` is the keyword letter's numerical value.
- `C` is the resulting ciphertext letter's numerical value.

The program uses `ord()` to convert letters into numerical values and `chr()` to convert the resulting values back into letters.

The keyword repeats when necessary. Spaces, numbers, and punctuation are preserved and do not consume keyword characters.

### 4.2 Row Permutation

The `row_permutation()` function divides the text into rows and rearranges them according to the user-defined permutation order.

For example, the order `2,1` means that the second row is placed before the first row.

### 4.3 Column Permutation

The `column_permutation()` function arranges the text into a grid and reads the columns according to the specified permutation order.

For example, the order `3,1,2` means that the third column is read first, followed by the first and second columns.

### 4.4 Multiple Permutation Rounds

The user chooses how many permutation rounds to apply. Each round can use either row or column permutation and has its own permutation order.

The program stores the selected rounds in a list and applies them sequentially after Vigenère encryption.

For example:

1. Vigenère encryption.
2. Row permutation.
3. Column permutation.
4. Another row permutation.

The user can choose a different combination of rounds for each encryption.

## 5. Decryption Algorithm

Decryption reverses the encryption process.

First, the program reverses the permutation rounds in the opposite order from which they were applied. Each round uses its corresponding permutation order.

After all permutation rounds have been reversed, the program applies Vigenère decryption using the same secret keyword.

The decryption formula is:

**P = (C - K) mod 26**

This reverses the Vigenère encryption operation.

The expected result is the original plaintext, including its spaces, punctuation, and capitalization.

## 6. Input Validation

The program checks user inputs to prevent common errors.

- The operation must be `Encrypt` or `Decrypt`.
- The keyword must contain English letters only.
- The number of permutation rounds must be a positive integer.
- Each round must be either `Row` or `Column`.
- A permutation order must contain every number from 1 to N exactly once, separated by commas.

If an invalid value is entered, the program displays an error message and asks the user to enter a valid value.

## 7. Example Test Cases

### Encryption

- **Operation:** Encrypt
- **Plaintext:** Hello World!
- **Secret Keyword:** SECURITY
- **Number of rounds:** 2
- **Round 1:** Row
- **Round 1 order:** 2,3,1
- **Round 2:** Column
- **Round 2 order:** 3,2,1

- After Vigenère: Zinff Ehpdh!
- After round 1(row): f Ehpdh!Zinf
- After round 2(column): EdZf p!nfhhi
- Final ciphertext: EdZf p!nfhhi 
  
### Decryption

- **Operation:** Decrypt
- **Text:** EdZf p!nfhhi
- **Secret Keyword:** SECURITY
- **Number of rounds:** 2
- **Round 1:** Row
- **Round 1 order:** 2,3,1
- **Round 2:** Column
- **Round 2 order:** 3,2,1

- After reversing round 2(column): Ehpdh!Zinf
- After reversing round 2(row): Zinff Ehpdh!
- Original plaintext: Hello World!

## 8. Conclusion

This project combines the Vigenère Cipher with flexible row and column permutation rounds. It demonstrates letter-to-number conversion, modulo 26 arithmetic, text rearrangement, input validation, and the importance of reversing encryption operations in the correct order.

The program is designed to allow users to experiment with different keywords and permutation configurations while recovering the original text through decryption.

