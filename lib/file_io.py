def write_file(file_name, file_content):
    file_path = f"{file_name}.txt"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(file_content)


def append_file(file_name, append_content):
    file_path = f"{file_name}.txt"
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(append_content)


def read_file(file_name):
    file_path = f"{file_name}.txt"
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
