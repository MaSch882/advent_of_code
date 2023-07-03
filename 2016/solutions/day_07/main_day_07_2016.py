from Utils import input_processing
from structure_day_07_2016 import TLSCounter

filename = r"..\..\input_data\input_day_07_2016.txt"

test_data = ["abba[mnop]qrst", "abcd[bddb]xyyx", "aaaa[qwer]tyui", "ioxxoj[asdfgh]zxcvbn", ]


def main():
    ips = read_input()
    print_solution_part_1(ips)


def print_solution_part_1(ips: list[str]):
    counter = TLSCounter()
    ips_with_tls = counter.count_ips_with_tls(ips)
    print(f"{ips_with_tls} IPs support TLS.")


def read_input():
    return input_processing.read_input(filename)


if __name__ == "__main__":
    main()
