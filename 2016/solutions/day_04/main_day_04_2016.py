from Utils import input_processing
from structure_day_04_2016 import Room
from structure_day_04_2016 import RoomDecryptor
from structure_day_04_2016 import RoomIDSummator

filename = r"..\..\input_data\input_day_04_2016.txt"

testdata = ["aaaaa-bbb-z-y-x-123[abxyz]", "a-b-c-d-e-f-g-h-987[abcde]", "not-a-real-room-404[oarel]",
            "totally-real-room-200[decoy]"]


def main():
    print_test_data()
    input_strings = read_input(filename)
    rooms = build_list_of_rooms(input_strings)

    # print_solution_part_1(rooms)  # 361724
    print_solution_part_2()  #


def read_input(file: str):
    return input_processing.read_input(file)


def build_list_of_rooms(list_of_room_string: list[str]) -> list[Room]:
    return [Room(i) for i in list_of_room_string]


def print_test_data():
    room = Room("qzmt-zixmtkozy-ivhz-343[zimth]")
    decryptor = RoomDecryptor(room)

    decrypt = decryptor.decrypt_room_name()
    print(decrypt)


def print_solution_part_1(rooms: list[Room]):
    id_summator = RoomIDSummator(rooms)
    id_summator.calculate_id_sum_of_valid_rooms()
    print(f"The sum of sector IDs of the real rooms is {id_summator.id_sum}.")


def print_solution_part_2():
    pass


if __name__ == "__main__":
    main()
