import csv, sys


def read_path(path_to_file):

    requests_list = []

    with open(path_to_file, 'r') as file:
        reader = csv.reader(file)
        try:
            for line in reader:
                requests_list.append(line)
        except csv.Error as err:
            sys.exit('file %s, linha %d: %s' % (file, reader.line_num, err))
    return requests_list


def turns_into_dict(path_to_file):

    list_dict_custumers = []
    requests_list = read_path(path_to_file)

    for request in requests_list:
        dict_customers = {
            "name": request[0],
            "dish": request[1],
            "day": request[2]
        }
        list_dict_custumers.append(dict_customers)
    return list_dict_custumers


def analyze_log(path_to_file):
    requests_list_dict = turns_into_dict(path_to_file)



analyze_log('data/orders_1.csv')