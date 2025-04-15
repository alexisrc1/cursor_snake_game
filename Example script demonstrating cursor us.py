# Example script demonstrating cursor usage
text = "Hello, World!"
cursor_position = 0

# Moving cursor forward
print("Moving cursor forward:")
while cursor_position < len(text):
    # Print the text with cursor indicator (^)
    print(text)
    print(" " * cursor_position + "^")
    cursor_position += 1
    
# Moving cursor backward
print("\nMoving cursor backward:")
while cursor_position > 0:
    cursor_position -= 1
    # Print the text with cursor indicator (^)
    print(text)
    print(" " * cursor_position + "^")

# Example of cursor insertion
text_list = list(text)
cursor_position = 5
text_list.insert(cursor_position, "|")
modified_text = "".join(text_list)
print("\nInserting at cursor position 5:")
print(modified_text)
