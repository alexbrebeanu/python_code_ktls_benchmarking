import os

def remove_last_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    if lines[-3].startswith("LOG"):
        with open(file_path, 'w') as file:
            file.writelines(lines[:-n])

def remove_last_3_lines_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):  # You can specify the file extension here
            file_path = os.path.join(directory_path, filename)
            remove_last_n_lines(file_path, 3)

# Replace 'path_to_your_directory' with the actual path of your directory
remove_last_3_lines_in_directory('/home/alex/Desktop/benchmark_analysis/results_client')