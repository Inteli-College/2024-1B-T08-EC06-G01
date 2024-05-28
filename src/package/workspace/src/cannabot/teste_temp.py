import bme280
import smbus2
from time import sleep

# port = 1
# address = 0x77 # Adafruit BME280 address. Other BME280s may be different
# bus = smbus2.SMBus(port)
# sleep(1)
# bme280.load_calibration_params(bus,address)
# print("funcionando")
# while True:
#     bme280_data = bme280.sample(bus,address)
#     humidity  = bme280_data.humidity
#     pressure  = bme280_data.pressure
#     ambient_temperature = bme280_data.temperature
#     print(humidity, pressure, ambient_temperature)
#     sleep(1)

while True:
    try:
        # Read sensor data
        data = bme280.sample(bus, address, calibration_params)

        # Extract temperature, pressure, and humidity
        temperature_celsius = data.temperature
        pressure = data.pressure
        humidity = data.humidity

        # Convert temperature to Fahrenheit
        temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)

        # Print the readings
        print("Temperature: {:.2f} °C, {:.2f} °F".format(temperature_celsius, temperature_fahrenheit))
        print("Pressure: {:.2f} hPa".format(pressure))
        print("Humidity: {:.2f} %".format(humidity))

        # Wait for a few seconds before the next reading
        time.sleep(2)

    except KeyboardInterrupt:
        print('Program stopped')
        break
    except Exception as e:
        print('An unexpected error occurred:', str(e))
        break