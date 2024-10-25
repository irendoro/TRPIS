from file_operations import read_file, write_file
from config import FILE_NAME

def main():
    write_file(FILE_NAME, "Hello, this is the content of the file.")
    print('hi!')
    content = read_file(FILE_NAME)
    print(f"File Content:\n{content}")
    print("Happy house!")
    print("Vsem privet")

if __name__ == "__main__":
    main()
# Additional temporary changes
