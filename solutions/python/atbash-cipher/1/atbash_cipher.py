alphabet =  list("abcdefghijklmnopqrstuvwxyz")
flipped_alphabet = list("zyxwvutsrqponmlkjihgfedcba")

def encode(plain_text):
    seperator = 0
    result = []
    for plain_letter in plain_text:
        for alphabet_index, alphabet_letter in enumerate(alphabet):
            if str(plain_letter).isnumeric():
                result.append(plain_letter)
                break
            if str(plain_letter).lower() == alphabet_letter: 
                result.append(flipped_alphabet[alphabet_index])
    for index, i in enumerate(result):
        seperator += 1
        if seperator == 6:
            result.insert(index, " ")
            seperator = 0
    return "".join(result)


def decode(ciphered_text):
    result = []
    for ciphered_letter in ciphered_text:
        for flipped_alphabet_index, flipped_alphabet_letter in enumerate(flipped_alphabet):
            if ciphered_letter == " ":
                result.append("")
            if str(ciphered_letter).isnumeric():
                result.append(ciphered_letter)
                break
            if str(ciphered_letter).lower() == flipped_alphabet_letter: 
                result.append(alphabet[flipped_alphabet_index])
    return "".join(result)
