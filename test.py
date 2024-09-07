

# 1. Create a file --> with open(file_name, mode):
# 2. Write
# 3. Read
# 4. Renaming
# 5. Deleting

# Delete File
#============================================
# import os
# os.remove("example.txt")


# Rename file
#=============================================
# import os
# os.rename("demo_file.txt", "example.txt")


# Read from file
#==============================================
# with open("demo_file.txt", "r") as file:
#     content = file.read()
#     print(content)


# Write in a file
#==============================================
# with open("demo_file.txt", "w") as file:
#     file.write("Bangladesh")


# Create a file inside a folder
#==============================================
# with open('my_dir/example.txt', 'w') as file:
#     print("Created")