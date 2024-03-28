#!/usr/bin/python3
"""Reads the stdin and computes a given stats"""


from collections import defaultdict
import sys


def compute_metrics():
    total_size = 0
    status_counts = defaultdict(int)

    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1

            parts = line.split()
            if len(parts) != 10:
                continue

            status_code = parts[8]
            file_size = parts[9]

            try:
                total_size += int(file_size)
            except ValueError:
                pass

            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)
    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)


def print_statistics(total_size, status_counts):
    print("Total file size:", total_size)
    for status_code in sorted(status_counts.keys()):
        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            print(f"{status_code}: {status_counts[status_code]}")


if __name__ == "__main__":
    compute_metrics()
