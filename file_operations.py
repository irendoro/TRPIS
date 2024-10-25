def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Content written to {filename}")
    print("Success")

def read_file(filename):
    print('This function of read')
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"File {filename} not found."
