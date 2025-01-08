def get_digits(number):
    
    digits = []
    while(number > 0):
        digits.append(number % 10)
        number = number // 10
    
    return digits

def is_armstrong_number(number):
    digits = get_digits(number)
    
    pow = len(digits)
    
    sum_of_powers = 0
    for digit in digits:
        sum_of_powers += digit ** pow
    
    return number == sum_of_powers
    
    
