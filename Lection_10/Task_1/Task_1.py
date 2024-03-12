import random

def generate_random_number():
    return random.randint(1, 100)

def generate_text_files():
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        filename = f"{char}.txt"
        with open(filename, 'a') as file:
            random_number = generate_random_number()
            file.write(str(random_number))

def create_summary_file():
    with open("summary.txt", 'w') as summary_file:
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            filename = f"{char}.txt"
            with open(filename, 'r') as file:
                content = file.read().strip()
                summary_file.write(f"{filename}: {content}\n")
generate_text_files()
create_summary_file()