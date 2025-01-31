def convert(number):

    sounds = {3: "Pling", 5: "Plang", 7: "Plong"}

    results = "".join(
        sounds[divisor] for divisor in sounds.keys() if number % divisor == 0
    )

    return results or str(number)
