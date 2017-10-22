import csv

def create_one_register_csv(name_file, data, header):
    """
    Creates a .csv with one records from a dictionary

    @param name_file: Name of file.
    @param data: Dict with the data to the file.
    @param header: Keys of dict.

    """
    with open(name_file, 'w') as arq:
        fieldnames = header
        fieldnames = sorted(fieldnames)
        file = csv.DictWriter(arq, fieldnames)
        file.writeheader()
        file.writerow(data)

def create_many_register_csv(name_file, data, header):
    """
    Creates a .csv with many records from a dictionary

    @param name_file: Name of file.
    @param data: Dict with the data to the file.
    @param header: Keys of dict.

    """
    with open(name_file, 'w') as arq:
        fieldnames = header
        fieldnames = sorted(fieldnames)
        file = csv.DictWriter(arq, fieldnames)
        file.writeheader()
        file.writerows(data)

def insert_one_register_csv(name_file, data, header):
    """
    Insert a records from a dictionary in a .csv.

    @param name_file: Name of file.
    @param data: Dict with the data to the file.
    @param header: Keys of dict.

    """
    with open(name_file, 'a') as arq:
        fieldnames = header
        fieldnames = sorted(fieldnames)
        file = csv.DictWriter(arq, fieldnames)
        file.writerow(data)

def insert_many_register_csv(name_file, data, header):
    """
    Insert all records from a dictionary in a .csv

    @param name_file: Name of file.
    @param data: Dict with the data to the file.
    @param header: Keys of dict.

    """
    with open(name_file, 'a') as arq:
        fieldnames = header
        fieldnames = sorted(fieldnames)
        file = csv.DictWriter(arq, fieldnames)
        file.writerows(data)
