#!/usr/bin/python3

import sys


def print_statistics(status_dict, total_file_size):
    """
    Print the statistics of the log file.

    Args:
        status_dict (dict): A dictionary containing the count
        of each status code.
        file_size (int): The total file size.

    Returns:
        None
    """
    print("File size:", total_file_size)
    for code, count in sorted(status_dict.items()):
        if count != 0:
            print("{}: {}".format(code, count))


total_file_size = 0
counter = 0
status_dict = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}

try:
    for line in sys.stdin:
        parsed_line = line.strip().split()

        counter += 1

        # Extract file size and status code
        file_size = int(parsed_line[-1])
        # Second last element is status code
        status_code = parsed_line[-2]

        if status_code in status_dict:
            total_file_size += file_size
            status_dict[status_code] += 1

        if counter == 10:
            print_statistics(status_dict, total_file_size)
            counter = 0

finally:
    print_statistics(status_dict, total_file_size)