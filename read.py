#!/usr/bin/env python3

import csv
from modbuslambdatronic import ModbusLambdatronic
from influxdb import InfluxDB, get_sequence

influxdb = InfluxDB()
sequences = []

modbus = ModbusLambdatronic()

# aktuelle werte
with open("modbus_lambdatronic/aktuelle_werte.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=";")
    for row in csv_reader:
        measurement = row["measurement"]
        tags = row["tags"]
        field = row["field"]
        address = int(row["id"][1:]) - 1
        decimals = int(row["dez"])
        scale = int(row["skal"])

        value = modbus.read_register_address(
            registeraddress=address,
            number_of_decimals=decimals,
            functioncode=4,
            scale=scale
        )
        sequence = get_sequence(
            measurement=measurement,
            tags=tags.split(","),
            field_value_pairs=[f"{field}={value}"]
        )
        sequences.append(sequence)

# anlagen-/kesselzustand
with open("modbus_lambdatronic/anlagenzustand_kesselzustand.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=";")
    for row in csv_reader:
        measurement = row["measurement"]
        tags = row["tags"]
        field = row["field"]
        address = int(row["id"][1:]) - 1

        value = modbus.read_register_address(
            registeraddress=address,
            number_of_decimals=0,
            functioncode=4,
            scale=1
        )
        sequence = get_sequence(
            measurement=measurement,
            tags=tags.split(","),
            field_value_pairs=[f"{field}={value}"]
        )
        sequences.append(sequence)

# fehlerpuffer
with open("modbus_lambdatronic/fehlerpuffer.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=";")
    for row in csv_reader:
        measurement = row["measurement"]
        tags = row["tags"]
        field = row["field"]
        address = int(row["id"][1:]) - 1

        value = modbus.read_register_address(
            registeraddress=address,
            number_of_decimals=0,
            functioncode=4,
            scale=1
        )
        sequence = get_sequence(
            measurement=measurement,
            tags=tags.split(","),
            field_value_pairs=[f"{field}={value}"]
        )
        sequences.append(sequence)

# parameter
with open("modbus_lambdatronic/parameter.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=";")
    for row in csv_reader:
        measurement = row["measurement"]
        tags = row["tags"]
        field = row["field"]
        address = int(row["id"][1:]) - 1
        decimals = int(row["dez"])
        scale = int(row["skal"])

        value = modbus.read_register_address(
            registeraddress=address,
            number_of_decimals=decimals,
            functioncode=3,
            scale=scale
        )
        sequence = get_sequence(
            measurement=measurement,
            tags=tags.split(","),
            field_value_pairs=[f"{field}={value}"]
        )
        sequences.append(sequence)

influxdb.write(sequences)

