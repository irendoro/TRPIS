def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Content written to {filename}")
    print("Success")
    print("Aloha")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"File {filename} not found."
