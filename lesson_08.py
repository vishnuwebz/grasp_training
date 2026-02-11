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