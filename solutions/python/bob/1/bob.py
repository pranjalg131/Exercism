def is_question(txt):
    return txt[-1] == '?'

def is_yelling(txt):
    
    has_letters = False
    for char in txt:
        if char.lower().isalpha():
            has_letters = True
    
    return has_letters and txt == txt.upper()

def is_silence(txt):
    return txt.strip() == ""

def response(hey_bob):
    
    hey_bob = hey_bob.strip()
    
    if is_silence(hey_bob):
        return "Fine. Be that way!"
    elif is_question(hey_bob) and is_yelling(hey_bob):
        return "Calm down, I know what I'm doing!"
    elif is_question(hey_bob):
        return "Sure."
    elif is_yelling(hey_bob):
        return "Whoa, chill out!"
    else:
        return "Whatever."

