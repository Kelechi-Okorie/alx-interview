#!/user/bin/env python3
"""Reads the stdin and computes a given stats"""


from collections import defaultdict
import sys


def compute_metrics():
    total_size = 0
    status_counts = defaultdic(int)

    try:
        line_count = 0
        for line in sys.stdin:
            lint_count += 1

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
                print_statstics(total_size, status_counts)
        except KeyboardInterrupt:
            print_statistics(total_size, status_counts)


if __name__ == "__main__":
    compute_metrics()
