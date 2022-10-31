import csv, sys


def read_path(path_to_file):

    requests_list = []

    with open(path_to_file, 'r') as file:
        reader = file.readlines()
        try:
            for line in reader:
                treated_line = line.replace("\n","")
                requests_list.append(treated_line)
        except csv.Error as err:
            sys.exit('file %s, linha %d: %s' % (file, reader.line_num, err))
    return requests_list


def analyze_log(path_to_file):
    requests_list = read_path(path_to_file)
    print(requests_list)




analyze_log('data/orders_1.csv')
