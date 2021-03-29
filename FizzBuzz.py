def fizzbuzz():
    #{I've taken a flexable aproach to FizzBuzz in a functional style. 
    # I've done this by containing the return values and parameters in into arrays}
    tools = [3, 5]
    potential_answers = ["Fizz", "Buzz", "FizzBuzz"]
    prompt = "What number would you like to divide?"
    nums = int(input(f"{prompt}: "))
    for number in range(nums):
        if number % tools[0] == 0:
            if number % tools[1] == 0:
                print(f"{potential_answers[2]}~{number}")
            else:
                print(f"{potential_answers[0]}~{number}")
        if number % tools[1] == 0:
            if number % tools[0] != 0:
                print(f"{potential_answers[1]}~{number}")


def control():
    #{This is the interface between the code and the user. 
    # Strings are contained in veriables so as to maintain flexability and avoid hard coding.}
    welcome = 'Welcome! At the input below you may enter "RUN" or "QUIT" \nYour answer is case sensitive.'
    print(welcome)
    choice = input()
    if choice == "RUN":
        fizzbuzz()
    if choice == "QUIT":
        exit()
    else:
        control()


if __name__ == "__main__":
    control()
