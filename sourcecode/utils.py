import os


def get_input_data(filename):
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../input_data/{filename}'))
    print(file_path)
    with open(file_path, 'r') as content:
        return content.readlines() or ''


def get_sanitized_input(filename):
    input_data = get_input_data(filename)
    return list(map(lambda l: [int(s) for s in l], map(lambda i: i.split(), input_data)))
