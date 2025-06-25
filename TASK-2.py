user_input = input("Enter text to write to the file: ")

with open('output.txt', 'w') as file2:
    file2.write(user_input + '\n')
    print("Date successfully written to 'output.txt'.")


additional_input = input("Enter additional text to append: ")

with open('output.txt', 'a') as file2:
    file2.write(additional_input + '\n')
    print("Data successfully appended")

print("\nFinal content of 'output.txt':")
with open('output.txt', 'r') as file2:
    file_content = file2.read()
    print(file_content)