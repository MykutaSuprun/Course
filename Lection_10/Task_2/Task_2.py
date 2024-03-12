with open("first_file.txt", 'w') as first_file:
    content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
 sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
 minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex
 ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate 
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat 
cupidatat non proident, sunt in culpaqui officia deserunt mollit anim id est laborum."""
    first_file.write(content)

with open("first_file.txt", 'r') as first_file, open("second_file.txt", 'w') as second_file:
    content_uppercase = first_file.read().upper()
    second_file.write(content_uppercase)