def isValidPerfectSquare(number):
    iterator = 1

    while iterator * iterator <= number:
        if iterator * iterator == number:
            return "true"
        iterator += 1

    return "false"


if __name__ == "__main__":
    num = int(input())

    print(isValidPerfectSquare(num))
