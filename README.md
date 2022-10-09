# Froeling to Influxdb

## Description

Fetch data from Froeling PE1 Pellet 25 via Modbus Lambdatronic 3200 and save it to InfluxDB.

## Table of Contents

* [Description](#description)
* [Installation](#installation)
* [Usage](#usage)
* [Author](#author)

## Installation

**Before the serial interface of the Froeling PE1 Pellet 25 can be used for communication via modbus, various settings must be made.** See Modbus Lambdatronic 3200 manual for details.

**What do you need?**
- Null Modem Cable
- RS232-To-USB-Adapter

**Prerequisites**
Connect the Raspberry Pi to the Froeling PE1 Pellet 25 via a serial cable and a RS232-To-USB-Adapter.

**Requirements**
- Python 3.10.4
- [python-dotenv 0.21.0](https://pypi.org/project/python-dotenv/)
- [influxdb-client 1.32.0](https://pypi.org/project/influxdb-client/)
- [pyserial 3.5](https://pypi.org/project/pyserial/)
- [minimalmodbus 2.0.1](https://pypi.org/project/minimalmodbus/)

Clone this repo and run the following from the root folder:
```bash
pip install -r requirements.txt
mv modbuslambdatronic.env.example modbuslambdatronic.env
mv influxdb.env.example influxdb.env
```

Adjust `modbuslambdatronic.env` (see Modbus Lambdatronic 3200 manual for details).

To identify the port used, the following steps can be performed:
1. before plugging in
```bash
ls -1 /dev > dev_temp0.txt
```
2. after plugging in
```bash
ls -1 /dev > dev_temp1.txt
diff dev_temp0.txt dev_temp1.txt
```
3. when done
```bash
rm dev_temp*.txt
```

The slave address can be taken from the settings of the Froeling PE1 Pellet 25.

UART settings like baudrate, bytesize, ... can be taken from the Modbus Lambdatronic 3200 manual.

Adjust `influxdb.env`.

## Usage

Add addresses to be read to following files:
- `modbus_lambdatronic/aktuelle_werte.csv`
- `modbus_lambdatronic/anlagenzustand_kesselzustand.csv`
- `modbus_lambdatronic/fehlerpuffer.csv`

Test Froeling:
```bash
python test_froeling.py
```

Read data and save it to InfluxDB:
```bash
python read.py
```

## Author

- Jonathan Tschanter [GitLab](https://gitlab.com/jmtw) [LinkedIn](https://de.linkedin.com/in/jonathan-tschanter)
