def rotate(text, key):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    ciphered = []
    for textletter in text:
        if key == 0 or key == 26:
            ciphered.append(textletter)
        elif str(textletter).lower() not in alphabet:
                ciphered.append(textletter)
        else:
            for alphaletter in alphabet:
                if str(textletter).lower() == alphaletter:
                    print(textletter)
                    #print(alphaletter)
                    index = alphabet.index(alphaletter)
                    #print(index)
                    finalindex = (index + key) % 26
                    #print(finalindex)
                    if str(textletter).isupper():
                        textletter_final = alphabet[finalindex]
                        ciphered.append(str(textletter_final).upper())
                    else:
                        textletter_final = alphabet[finalindex]
                        ciphered.append(textletter_final)
    return("".join(ciphered))