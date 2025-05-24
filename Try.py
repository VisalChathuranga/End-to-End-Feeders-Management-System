# Let's start by opening and reading the contents of the 'main.py' file to inspect the code.
file_path = 'D:/Feeders GUI/main.py'

# Reading the file contents
with open(file_path, 'r') as file:
    main_py_code = file.read()

print(main_py_code[:2000])  # Displaying the first 2000 characters to get an overview of the code.

