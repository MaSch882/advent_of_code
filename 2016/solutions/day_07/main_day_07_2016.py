from Utils import input_processing
from structure_day_07_2016 import IPAdress
from structure_day_07_2016 import TLSCounter

filename = r"..\..\input_data\input_day_07_2016.txt"

test_data = ["abba[mnop]qrst", "abcd[bddb]xyyx", "aaaa[qwer]tyui", "ioxxoj[asdfgh]zxcvbn"]
test_ips = [IPAdress(ip) for ip in test_data]


def main():
    ips = read_input()
    print_solution_part_1(ips)  # 105


def print_solution_part_1(ips: list[IPAdress]):
    counter = TLSCounter()
    ips_with_tls = counter.count_ips_with_tls(ips)
    print(f"{ips_with_tls} IPs support TLS.")


def read_input() -> list[IPAdress]:
    input_strings = input_processing.read_input(filename)
    return [IPAdress(ip) for ip in input_strings]


if __name__ == "__main__":
    main()
