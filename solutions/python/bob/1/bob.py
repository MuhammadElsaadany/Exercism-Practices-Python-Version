def response(hey_bob):
    if str(hey_bob).endswith("?") or "  " in hey_bob and "?" in hey_bob:
        if str(hey_bob).isupper() and not str(hey_bob).islower():
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    if str(hey_bob).isupper() and not str(hey_bob).islower():
        return "Whoa, chill out!"
    if hey_bob == "" or "\t" in hey_bob or "  " in hey_bob and not str(hey_bob).isalpha or hey_bob == "          ":
        return "Fine. Be that way!"
    else:
        return "Whatever."
