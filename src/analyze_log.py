from collections import Counter
import csv
import os


def read_path(path_to_file):

    requests_list = []

    if path_to_file.split(".")[-1] != "csv":
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    if not os.path.isfile(path_to_file):
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    with open(path_to_file, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            requests_list.append(line)
    return requests_list


def turns_into_dict(path_to_file):

    list_dict_custumers = []
    requests_list = read_path(path_to_file)

    for request in requests_list:
        dict_customers = {
            "name": request[0],
            "dish": request[1],
            "order_day": request[2]
        }
        list_dict_custumers.append(dict_customers)
    return list_dict_custumers


def most_requested_dish(client_name: str, list_customers: list):

    plates = []

    for costumer in list_customers:
        if costumer['name'] == client_name:
            plates.append(costumer['dish'])

    counter_plates = Counter(plates)
    return max(counter_plates, key=counter_plates.get)


def quantity_plates(client_name: str, list_customers: list, plate: str):
    plates = []

    for costumer in list_customers:
        if costumer['name'] == client_name:
            plates.append(costumer['dish'])

    counter_plates = Counter(plates)
    return counter_plates[plate]


def dishes_never_ordered(client_name: str, list_customers: list):
    set_plates = set()
    set_plates_costumer = set()

    for costumer in list_customers:
        set_plates.add(costumer['dish'])
        if costumer['name'] == client_name:
            set_plates_costumer.add(costumer['dish'])
    return set_plates.difference(set_plates_costumer)


def days_never_visited(client_name: str, list_costumers: list):

    set_plates = set()
    set_plates_costumer = set()

    for costumer in list_costumers:
        set_plates.add(costumer['order_day'])
        if costumer['name'] == client_name:
            set_plates_costumer.add(costumer['order_day'])
    return set_plates.difference(set_plates_costumer)


def analyze_log(path_to_file):
    requests_list_dict = turns_into_dict(path_to_file)
    maria_dish = most_requested_dish('maria', requests_list_dict)
    arnaldo = quantity_plates('arnaldo', requests_list_dict, 'hamburguer')
    joao_dishes = dishes_never_ordered('joao', requests_list_dict)
    joao_days = days_never_visited('joao', requests_list_dict)

    with open("data/mkt_campaign.txt", mode="w") as new_file:
        new_file.write(f"{maria_dish}" + "\n")
        new_file.write(f"{arnaldo}\n")
        new_file.write(f"{joao_dishes}\n")
        new_file.write(f"{joao_days}\n")
