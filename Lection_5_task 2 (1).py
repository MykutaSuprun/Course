def input_info():
    try:
        string_input=input('enter a string ')
        int_input=int(input('enter an integer '))
        return string_input,int_input
    except ValueError:
            print("Wrong input. Please enter a string and an integer.")
    except IndexError:
            print("Wrong input. Please enter a string and an integer.")
        


def print_character(string_input,int_input):
    try:
        char_index=(string_input[int_input])
        print(char_index)
    except IndexError:
        print(f"Index {int_input} is out of range for the given string.")

while True:
    input_string,input_integer= input_info()
    print_character(input_string,input_integer)
    user_input = input("Do you want to try again? (y/n): ").lower()
    if user_input != 'y':
        break