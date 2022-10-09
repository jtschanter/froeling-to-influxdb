#!/usr/bin/env python3

from dotenv import dotenv_values
import json
import serial
import minimalmodbus

class ModbusLambdatronic:

    def __init__(self):
        config = dotenv_values("modbus_lambdatronic.env")        
        self.instrument = minimalmodbus.Instrument(
            port=config["PORT_NAME"],
            slaveaddress=config["SLAVE_ADDRESS"],
            mode=config["MODE"],
            debug=config["DEBUG"]
        )
        self.instrument.serial.baudrate = config["BAUDRATE"]
        self.instrument.serial.bytesize = config["BYTESIZE"]
        self.instrument.serial.parity = serial.PARITY_NONE
        self.instrument.serial.stopbits = config["STOPBITS"]

    def read_register_address(self, registeraddress, number_of_decimals, functioncode, scale):
        res = self.instrument.read_register(
            registeraddress=registeraddress,
            number_of_decimals=number_of_decimals,
            functioncode=functioncode,
            signed=False
        )
        res = res / scale
        return res
