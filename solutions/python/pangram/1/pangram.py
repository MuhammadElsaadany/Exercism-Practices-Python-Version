def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    validator = set(str(sentence).lower())
    return alphabet.issubset(validator)