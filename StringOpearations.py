text = input("Enter a string: ")

print("1. Length:", len(text))
print("2. Uppercase:", text.upper())
print("3. Lowercase:", text.lower())

substring = input("Enter a substring to search: ")
print("4. Substring position:", text.find(substring))

old = input("Enter text to replace: ")
new = input("Enter replacement text: ")
print("5. Replaced string:", text.replace(old, new))
