#!/usr/bin/python
"""
Simple timer - Main module.
"""
import argparse
from helpers import check_sudo, setup, get_ht


def main():
    """
    Simple timer.
    """
    check_sudo()
    parser = argparse.ArgumentParser(description='Simple timer.')
    parser.add_argument('--pin',
                        action='store',
                        dest='pin',
                        type=int,
                        required=True,
                        help='raspberry pins GPIO.BCM mode')
    parser.add_argument('--one_value',
                        action='store_true',
                        dest='one_value',
                        help='gets temperature and humidity one time and ends')

    args = parser.parse_args()
    # sanitizes args
    pin = args.pin
    one_value = args.one_value
    # setup GPIO
    sensor = setup(pin)

    if one_value:
        try:
            humidity, temperature = get_ht(sensor, pin)
        except Exception:
            temperature = "NULL"
            humidity = "NULL"

        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))

    # Reset GPIO settings
    # teardown()


if __name__ == "__main__":
    main()