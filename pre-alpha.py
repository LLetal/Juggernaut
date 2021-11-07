from bleak import BleakScanner
from time import sleep
import asyncio
import random
from pylgbst import *
from pylgbst.hub import MoveHub
from pylgbst.peripherals import EncodedMotor, TiltSensor, Current, Voltage, COLORS, COLOR_BLACK
import sys

import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

"""InfluxDB implementation part"""
bucket = "your bucket's name"
org = "your org"
token = "your token"
url = "your url"

client = influxdb_client.InfluxDBClient(
   url=url,
   token=token,
   org=org
)
write_api = client.write_api(write_options=SYNCHRONOUS)
"""Data logging phase"""
from bleak import BleakScanner
import asyncio

async def auto_search():

    devices = await BleakScanner.discover(timeout=20)
    possible_devices = []
    for d in devices:
        if d.name == "Move Hub":
            possible_devices.append(d)
        #print(f'${d.address} - ${d.name} - {d.metada}')

    if len(str(possible_devices[1].metadata)) > len(str(possible_devices[0].metadata)):
        return(possible_devices[1].name, possible_devices[1].address)
    else:
        return(possible_devices[0].name, possible_devices[0].address)

def led_random(mhub):
    for x in range(20):
        mhub.led.set_color(random.randrange(0,10))

def motor_loop1(mhub):

    mhub.motor_A.timed(2, 1)
    mhub.motor_B.timed(2,0.1)
    mhub.motor_B.timed(1, 1)
    mhub.motor_AB.timed(2, 1)
    # mhub.motor_external.timed(5,1)
    mhub.motor_A.timed(5,-0.5)
    mhub.motor_B.timed(1, -0.5)
    mhub.motor_B.timed(2,0.2)

def motor_loop2(mhub):
    mhub.moto_AB.timed(2,1,0)
    mhub.moto_AB.timed(5,-0.5,0.7)
    mhub.moto_AB.timed(3,0,-1)
    mhub.external_motor.timed(2,-0.5)
    mhub.moto_AB.timed(2,1,0.5)
    mhub.moto_AB.timed(4,0.2,0.5)
    mhub.moto_AB.timed(3, 1,1)

def motor_loop3(mhub):
    mhub.external_motor(1,0.7)
    mhub.external_motor(1,-1)
    mhub.external_motor(5,-0.1)
    mhub.external_motor(1,0.8)

def sequence(mhub):
    # t1 = time.time()
    # while time.time() - t1 != time_length:
    motor_loop1(mhub)
    # motor_loop2(mhub)
    # motor_loop3(mhub)
    for x in range(12):
        led_random(mhub)


def main3(mhub):
    main3.states = {mhub.motor_A: 0, mhub.motor_B: 0, mhub.motor_external: 0}
    def callback_a(param1):
        main3.states[mhub.motor_A] = param1
        #sys.stdout.write("Motor_A" + str(main3.states[mhub.motor_A]))
        p = influxdb_client.Point("Lego motor_A").tag("location", "Přerov").field("motor_value", int(main3.states[mhub.motor_A]))
        write_api.write(bucket=bucket, org=org, record=p)

    def callback_b(param1):
        main3.states[mhub.motor_B] = param1
        #sys.stdout.write(str(main3.states))
        p = influxdb_client.Point("Lego motor_B").tag("location", "Přerov").field("motor_value", int(main3.states[mhub.motor_B]))
        write_api.write(bucket=bucket, org=org, record=p)

    def motor_callback(values):
        sys.stdout.write("motor speed: " + values)  # motor_file.write(values)

    def rgb_callback(values):
        # motor_file.write(values)
        sys.stdout.write("rgb: " + str(values))
        #p = influxdb_client.Point("Lego rgb").tag("location", "Přerov").field("rgb_value", str(values))
        #write_api.write(bucket=bucket, org=org, record=p)

    def axis_callback(x, y, z):
        #values = x, y, z
        # Axis_file.write(values)
        #sys.stdout.write("axis: " + str(values))
        p = influxdb_client.Point("Lego axis x").tag("location", "Přerov").field("x_values", x)
        write_api.write(bucket=bucket, org=org, record=p)
        p2 = influxdb_client.Point("Lego axis y").tag("location", "Přerov").field("y_values", y)
        write_api.write(bucket=bucket, org=org, record=p2)
        p3 = influxdb_client.Point("Lego axis y").tag("location", "Přerov").field("z_values", z)
        write_api.write(bucket=bucket, org=org, record=p3)


    def color_callback(values):
        # color_file.write(values)
        sys.stdout.write("color : " + str(values))

    def battery_callback(values):
        # battery_file.write(values)
        sys.stdout.write(str(values))
        #p = influxdb_client.Point("Lego battery_value").tag("location", "Prague").field("battery_voltage", values)
        #write_api.write(bucket=bucket, org=org, record=p)

    mhub.motor_A.subscribe(callback_a, mode=EncodedMotor.SENSOR_SPEED)
    mhub.motor_B.subscribe(callback_b, mode=EncodedMotor.SENSOR_SPEED)
    mhub.led.subscribe(rgb_callback)
    mhub.tilt_sensor.subscribe(axis_callback, mode=TiltSensor.MODE_3AXIS_ACCEL)
    # mhub.vision_sensor.subscribe(color_callback, mode=VisionSensor.COLOR_ONLY) Někde chyba v knihovně????
    print(mhub.voltage.get_sensor_data(Voltage.VOLTAGE_L))

    sequence(mhub)


    # mhub.motor_AB.unsubscribe(motor_callback)
    mhub.led.unsubscribe(rgb_callback)
    mhub.tilt_sensor.unsubscribe(axis_callback)
    mhub.voltage.unsubscribe(battery_callback)


async def main2():
    devices = await BleakScanner.discover(timeout=20)

    for d in devices:
        print(f'{d.address} - {d.name} - {d.details} - {d.metadata}')

name, UUID = asyncio.run(auto_search())

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(relativeCreated)d\t%(levelname)s\t%(name)s\t%(message)s')

    parameters = {}
    try:
        connection = get_connection_bleak(hub_mac=str(UUID), hub_name=str(name)) 
        parameters['connection'] = connection
    except ValueError as err:
        parser.error(err.args[0])
    hub = MoveHub(**parameters)
    try:
        main3(hub)
    finally:
        hub.disconnect()
