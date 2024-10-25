def write_file(filename, content):
    print("This function of write")
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Content written to {filename}")
    print("Success")
    print("Good luck")

def read_file(filename):
    print('This function of read')
    print("Hello world")
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"File {filename} not found."
