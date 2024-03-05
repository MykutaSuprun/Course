def input_info():
    try:
        string_input=input('enter a string ')
        int_input=int(input('enter an integer '))
        return string_input,int_input
    except ValueError:
            print("Wrong input. Please enter a string and an integer.")
        


def print_character_at_index():
    while True:
        try:
            user_string, user_integer = input_info()
            character = user_string[user_integer]
            print(f"Character at index {user_integer}: {character}")
            break
        except IndexError:
            print(f"IndexError: The index {user_integer} is out of range for the given string.")

print_character_at_index()