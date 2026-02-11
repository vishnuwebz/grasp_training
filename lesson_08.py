# using context manager to read a file

with open('greetings.txt', 'r') as file:
    # read the entire file content into one string
    content = file.read()
    print("--- Reading entire file: ---")
    print(content)

# The file is automatically closed here

# A more memory-efficient way for large files is to iterate line by line
print("\n--- Reading file line by line: ---")
with open('greetings.txt', 'r') as file:
    for line in file:
        # .strip() removes leading/trailing whitespace, includig the newline character
        print(line.strip())


# using 'w' mode will create 'app.log' and write to it.
# if 'app.log' already exists, it will be completely overwritten.

with open('app.log', 'w') as file:
    file.write("Application started.\n")
    file.write("Processing data...\n")

# using 'a' mode to append to the same file without erasing it

with open('app.log', 'a') as file:
    file.write("Data processing complete. \n")
    file.write("Application shutting down. \n")


# let's verify the content
print("\n--- Content of app.log: ---")
with open('app.log', 'r') as file:
    print(file.read())


# try - except method on files

def safe_read(filepath):
    """
    Reads content from a file and handles common errors.
    Returns the file content or an error message string.
    :param filepath:
    :return:
    """
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file '{filepath}' was not found."
    except PermissionError:
        return f"Error: You don't have permission to read '{filepath}'."
    except Exception as e:
        # A general catch-all for any other unexpected errors
        return f"An unexpected error occurred: {e}"

# --- Testing our safe_read function ---

# 1. Test with a file that exists
print("\n--- Testing safe_read with existing file: ---")
content = safe_read('greetings.txt')
print(content)

# 2: Test with a file that does not exist

print("\n--- Testing safe_read with non-existing file: ---")
content = safe_read('ghost_file.txt')
print(content)