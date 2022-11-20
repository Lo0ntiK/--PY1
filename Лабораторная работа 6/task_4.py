
import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str, delimiter: str = ',', new_line: str = '\n') -> list[dict]:
    with open(filename) as fi:
        first_line = True
        rows = []
        headers = []
        for line in fi:
            if first_line:
                headers += str(line[:len(line)-1]).split(',')
            else:
                if line == '':
                    continue    # пустые строки не нужны
                row = str(line[:len(line)-1]).split(',')
                rows.append(row)
            first_line = False
    
    list_of_dicts = []
    length = len(headers)
    for row in rows:
        dict_ = {headers[i]: row[i] for i in range(length)}
        list_of_dicts.append(dict_)
        
    return list_of_dicts


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

