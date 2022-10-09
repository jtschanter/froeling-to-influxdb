#!/usr/bin/env python3

import csv
#from modbuslambdatronic import ModbusLambdatronic
from influxdb import InfluxDB, get_sequence

influxdb = InfluxDB()
sequences = []

#modbus = ModbusLambdatronic()

# aktuelle werte
with open("modbus_lambdatronic/aktuelle_werte.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=";")
    line = 0
    for row in csv_reader:
        if line != 0:
            measurement = row["measurement"]
            tags = row["tags"]
            field = row["field"]
            address = int(row["id"][1:])
            decimals = row["dez"]
            scale = row["skal"]

            '''
            value = modbus.read_register_address(
                registeraddress=address,
                number_of_decimals=decimals,
                functioncode=4,
                scale=scale
            )
            '''
            value = 999
            sequence = get_sequence(
                measurement=measurement,
                tags=tags.split(","),
                field_value_pairs=[f"{field}={value}"]
            )
            sequences.append(sequence)
        line += 1

# anlagen-/kesselzustand
with open("modbus_lambdatronic/anlagenzustand_kesselzustand.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=";")
    line = 0
    for row in csv_reader:
        if line != 0:
            measurement = row["measurement"]
            tags = row["tags"]
            field = row["field"]
            address = int(row["id"][1:])

            '''
            value = modbus.read_register_address(
                registeraddress=address,
                number_of_decimals=0,
                functioncode=4,
                scale=1
            )
            '''
            value = 999
            sequence = get_sequence(
                measurement=measurement,
                tags=tags.split(","),
                field_value_pairs=[f"{field}={value}"]
            )
            sequences.append(sequence)
        line += 1

# fehlerpuffer
with open("modbus_lambdatronic/fehlerpuffer.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=";")
    line = 0
    for row in csv_reader:
        if line != 0:
            measurement = row["measurement"]
            tags = row["tags"]
            field = row["field"]
            address = int(row["id"][1:])

            '''
            value = modbus.read_register_address(
                registeraddress=address,
                number_of_decimals=0,
                functioncode=4,
                scale=1
            )
            '''
            value = 999
            sequence = get_sequence(
                measurement=measurement,
                tags=tags.split(","),
                field_value_pairs=[f"{field}={value}"]
            )
            sequences.append(sequence)
        line += 1

# parameter
with open("modbus_lambdatronic/parameter.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=";")
    line = 0
    for row in csv_reader:
        if line != 0:
            measurement = row["measurement"]
            tags = row["tags"]
            field = row["field"]
            address = int(row["id"][1:])
            decimals = row["dez"]
            scale = row["skal"]

            '''
            value = modbus.read_register_address(
                registeraddress=address,
                number_of_decimals=decimals,
                functioncode=3,
                scale=scale
            )
            '''
            value = 999
            sequence = get_sequence(
                measurement=measurement,
                tags=tags.split(","),
                field_value_pairs=[f"{field}={value}"]
            )
            sequences.append(sequence)
        line += 1

influxdb.write(sequences)

