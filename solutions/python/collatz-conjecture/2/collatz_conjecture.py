def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    ans = 0;
    # while(number != 1):
    #     if(number % 2 == 0):
    #         number = number / 2
    #     else:
    #         number = number * 3 + 1
    #     ans += 1
    
    while(number != 1):
        number = number / 2 if number % 2 == 0 else number * 3 + 1
        ans += 1
    
    return ans
