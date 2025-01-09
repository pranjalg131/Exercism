# def is_question(txt):
#     return txt[-1] == '?'

# def is_yelling(txt):
    
#     has_letters = False
#     for char in txt:
#         if char.lower().isalpha():
#             has_letters = True
    
#     return has_letters and txt == txt.upper()

# def is_silence(txt):
#     return txt.strip() == ""

def response(hey_bob):
    
    hey_bob = hey_bob.strip()
    
    is_shout = hey_bob.isupper()
    is_question = hey_bob.endswith('?')
    
    if not hey_bob:
        return "Fine. Be that way!"
    elif is_question and is_shout:
        return "Calm down, I know what I'm doing!"
    elif is_question:
        return "Sure."
    elif is_shout:
        return "Whoa, chill out!"
    else:
        return "Whatever."

