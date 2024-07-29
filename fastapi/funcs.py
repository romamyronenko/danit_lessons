"""

гра "бики та корови"

2345
2243
0229  1К
2199  1Б 1К

"""


def cows_and_bulls(secret: str, guess: str):
    if len(secret) != len(guess):
        raise ValueError("different lengths")
    bulls = 0
    cows = 0
    secret_without_bulls = []
    guess_without_bulls = []
    for secret_digit, guess_digit in zip(secret, guess):
        if secret_digit == guess_digit:
            bulls += 1
        else:
            secret_without_bulls.append(secret_digit)
            guess_without_bulls.append(guess_digit)

    for digit in guess_without_bulls:
        if digit in secret_without_bulls:
            cows += 1
            secret_without_bulls.remove(digit)

    return {"cows": cows, "bulls": bulls}


def cows_and_bulls_(secret: str, guess: str):
    if len(secret) != len(guess):
        raise ValueError("different lengths")
    bulls = 0
    cows = 0

    secret_counter = {}
    guess_counter = {}

    for secret_digit, guess_digit in zip(secret, guess):
        if secret_digit == guess_digit:
            bulls += 1
        else:
            if secret_digit in secret_counter:
                secret_counter[secret_digit] += 1
            else:
                secret_counter[secret_digit] = 1

            if guess_digit in guess_counter:
                guess_counter[guess_digit] += 1
            else:
                guess_counter[guess_digit] = 1

    for key in guess_counter:
        cows += min(guess_counter[key], secret_counter.get(key, 0))

    return {"cows": cows, "bulls": bulls}


"""
())


stack: 
"""

brackets = {
    "(": ")",
    "[": "]",
    "{": "}",
}


def check_brackets(s: str):
    stack = []

    for char in s:
        if char in brackets.keys():
            stack.append(char)

        elif char in brackets.values():
            if not stack:
                return False

            last = stack.pop()
            if brackets[last] != char:
                return False
    return not stack
