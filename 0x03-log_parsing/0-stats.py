#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''

import sys


# Initialize variables
cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0


try:
    # Iterate over each line from standard input
    for line in sys.stdin:
        # Split the line into a list of strings
        line_list = line.split(" ")

        # Check if the line is in the expected format
        if len(line_list) > 4:
            # Extract status code and file size
            code = line_list[-2]
            size = int(line_list[-1])

            # Update cache with status code counts
            if code in cache.keys():
                cache[code] += 1

            # Accumulate total file size
            total_size += size
            # Increment line counter
            counter += 1

        # Check if we've processed 10 lines
        if counter == 10:
            counter = 0
            # Print total file size
            print('File size: {}'.format(total_size))
            # Print status code counts
            for key, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))


# Handle exceptions
except Exception as err:
    pass


# Print final total file size and status code counts
finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))