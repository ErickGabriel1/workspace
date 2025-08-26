name = input("Enter your name:").strip()

print(f"your name in uppercase is:{name.upper()}")
print(f"your name in lowercase is:{name.lower()}")
print(f"your name has {len(name.replace(" ", ""))} characters")
print("--------------------------------")
print(f"your first name is {name.split()[0]} and it has {len(name.split()[0])} characters")