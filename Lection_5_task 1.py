def user_input():
    inputed_value = input('Enter an integer ')
    return (inputed_value)

def convertion(user_input):
    try:
        converted_value=int(user_input())
        print(converted_value)
    except ValueError:
        print('enter an integer again')
        convertion(user_input)

number=convertion(user_input)