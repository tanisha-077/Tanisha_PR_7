def create_file(filename):
    try:
        with open(filename, "x") as file:
            pass
        print("File created successfully!")
    except FileExistsError:
        print("File already exists!")


def write_file(filename, data):
    try:
        with open(filename, "w") as file:
            file.write(data)
        print("Data written successfully!")
    except Exception as e:
        print("Error:", e)


def read_file(filename):
    try:
        with open(filename, "r") as file:
            data = file.read()

        print("File Content:")
        print(data)

    except FileNotFoundError:
        print("File not found!")


def append_file(filename, data):
    try:
        with open(filename, "a") as file:
            file.write(data)

        print("Data appended successfully!")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    print("File Operations Module")