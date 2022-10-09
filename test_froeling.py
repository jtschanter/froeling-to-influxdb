#!/usr/bin/env python3

from modbuslambdatronic import ModbusLambdatronic

modbus = ModbusLambdatronic()

res = modbus.read_register_address(
    registeraddress=0,
    number_of_decimals=0,
    functioncode=4,
    scale=2
)

print(f"Kesseltemperatur: {res}°C")
