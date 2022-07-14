from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import os

if __name__ == "__main__":
    file = "phonebook_raw.csv"
    path = os.path.abspath('Text/' + file)
    with open(path, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    contacts_list_new = []
    for item in contacts_list:
        for var in item[0:2]:
            if var != '':









