# Copyright (C) 2022, François-Guillaume Fernandez.

# This program is licensed under the Apache License 2.0.
# See LICENSE or go to <https://www.apache.org/licenses/LICENSE-2.0> for full license details.


import argparse

from dummy_lib import convert_fahrenheit_to_celsius



def main(args):

    # Retrieve a list of floats
    fahrenheits = list(map(float, args.fahrenheits.split(",")))
    celsius = convert_fahrenheit_to_celsius(fahrenheits)

    # Display the conversion results in the console
    for f_temp, c_temp in zip(fahrenheits, celsius):
        print(f"{f_temp:.1f}°F is {c_temp:.1f}°C")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Temperature conversion script", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("fahrenheits", type=str, help="Comma-separated temparatures in celsius")
    args = parser.parse_args()

    main(args)
