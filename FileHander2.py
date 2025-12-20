print("=== File Handler Program ===\n")

user_text = input("Enter text to write to file: ")

file = open("output.txt", "w")
file.write(user_text)
file.close()

print("✓ Text written to output.txt\n")

add_text = input("Enter more text to add: ")

file = open("output.txt", "a")
file.write("\n" + add_text)
file.close()

print("✓ Text added to output.txt\n")

# Step 3: Read and display the file content
print("=== File Contents ===")
file = open("output.txt", "r")
content = file.read()
file.close()

print(content)