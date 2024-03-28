import re
import sys

total_size = 0
status_code_counts = {}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1

        match = re.search(r"(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] \"GET \/projects\/260 HTTP\/1.1\" (\d+) (\d+)", line)
        if match:
            file_size = int(match.group(4))
            total_size += file_size
            status_code = int(match.group(3))
            status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

        if line_count % 10 == 0:
            print("File size:", total_size)
            for code in sorted(status_code_counts):
                print(f"{code}: {status_code_counts[code]}")
            status_code_counts = {}  # Reset for next 10 lines

except KeyboardInterrupt:
    print("File size:", total_size)
    for code in sorted(status_code_counts):
        print(f"{code}: {status_code_counts[code]}")
