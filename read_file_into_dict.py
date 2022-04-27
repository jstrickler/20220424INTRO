from pprint import pprint

FILE_PATH = 'DATA/knights.txt'

def main():
    kdata = read_info(FILE_PATH)
    print(get_field(kdata, 'Arthur', 2))
    print()
    print_titles(kdata)
    print()
    pretty_print(kdata)

def read_info(file_path):
    knight_info = {}

    with open(file_path) as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            knight_info[name] = title, color, quest, comment
    return knight_info

def get_field(data, knight, field_number):
    return data[knight][field_number]

def print_titles(data):
    for knight_name, knight_data in data.items():
        print(knight_data[0].upper(), knight_name)

def pretty_print(data):
    pprint(data)


if __name__ == '__main__':
    main()

