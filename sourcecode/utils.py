import os


def get_input_data(filename):
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../input_data/{filename}'))
    print(file_path)
    with open(file_path, 'r') as content:
        return content.readlines() or ''
