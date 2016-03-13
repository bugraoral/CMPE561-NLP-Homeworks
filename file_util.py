import json


def write_dic(filename, tokens, f_encoding='windows-1254'):
    with open(filename, 'w', encoding=f_encoding) as file:
        json.dump(tokens, file, ensure_ascii=False)

        # with open(filename, 'wb') as handle:
        #    pickle.dump(tokens, handle)


def read_dic(filename, f_encoding='windows-1254'):
    with open(filename, 'r', encoding=f_encoding) as file:
        return json.load(file)

        # with open(filename, 'rb') as handle:
        #    return pickle.load(handle)


def read_line_list(filename, f_encoding='windows-1254'):
    with open(filename, 'r', encoding=f_encoding) as file:
        return file.read().splitlines()
