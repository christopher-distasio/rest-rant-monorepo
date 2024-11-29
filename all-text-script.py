import os

# Function to append the contents of a file to a text file
def append_file_contents_to_text_file(file_path, output_file):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            output_file.write(f"\n---\nContents of {file_path}:\n")
            output_file.write(file.read() + "\n")
    except Exception as e:
        output_file.write(f"Could not read {file_path}: {e}\n")

# Open the output text file
with open('repo-contents-as-text.txt', 'w', encoding='utf-8') as output_file:
    # Walk through all directories and files in the repository
    for root, dirs, files in os.walk("."):
        for file in files:
            file_path = os.path.join(root, file)
            append_file_contents_to_text_file(file_path, output_file)







# import os

# # Function to print the contents of a file
# def print_file_contents(file_path):
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             print(f"\n---\nContents of {file_path}:\n")
#             print(file.read())
#     except Exception as e:
#         print(f"Could not read {file_path}: {e}")

# # Walk through all directories and files in the repository
# for root, dirs, files in os.walk("."):
#     for file in files:
#         file_path = os.path.join(root, file)
#         print_file_contents(file_path)