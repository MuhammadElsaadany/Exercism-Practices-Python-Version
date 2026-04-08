def response(hey_bob):
    hey_bob_stripped = hey_bob.strip()
    
    is_question = hey_bob_stripped.endswith("?")
    is_yelling = hey_bob_stripped.isupper() and not hey_bob_stripped.islower()
    is_silence = not hey_bob_stripped

    if is_silence:
        return "Fine. Be that way!"
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    if is_yelling:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."
    return "Whatever." 
    #I USED AI TO REWRITE MY CODE IT WAS SO SPAGHET