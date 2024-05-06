from loesungen.python.utils.input_processing import InputReader
from structure_day_07_2016 import IPAdress
from structure_day_07_2016 import TLSCounter, SSLCounter

filename = r"..\..\..\..\input_data/2016/2016_07.txt"


def main():
    ips = read_input()
    print_solution_part_1(ips)  # 105
    print_solution_part_2(ips)  # 258


def print_solution_part_1(ips: list[IPAdress]):
    tls_counter = TLSCounter()
    ips_with_tls = tls_counter.count_ips_with_tls(ips)
    print(f"{ips_with_tls} IPs support TLS.")


def print_solution_part_2(ips: list[IPAdress]):
    ssl_counter = SSLCounter()
    ips_with_ssl = ssl_counter.count_ips_with_ssl(ips)
    print(f"{ips_with_ssl} IPs support SSL.")


def read_input() -> list[IPAdress]:
    input_strings = InputReader.read_input(filename)
    return [IPAdress(ip) for ip in input_strings]


if __name__ == "__main__":
    main()
