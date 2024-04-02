import csv

# parsing

def get_dataset(filename):
    dataset = []

    with open(filename, encoding='utf-8') as r_file:

        file_reader = csv.reader(r_file, delimiter = ",")
        count = 0
        #Считывание данных из CSV файла
        for row in file_reader:
            if count != 0:
                dataset.append((float(row[4]) + float(row[5])) / 2)
            count += 1

    return dataset


print(get_dataset("dataset_for_training/coin_NEM.csv"))









