from Utils.input_processing import InputReader
from structure_day_04_2016 import Room
from structure_day_04_2016 import RoomDecryptor
from structure_day_04_2016 import RoomIDSummator

filename = r"..\..\input_data\input_day_04_2016.txt"


def main():
    input_strings = read_input(filename)
    rooms = build_list_of_rooms(input_strings)

    print_solution_part_1(rooms)  # 361724
    print_solution_part_2(rooms)  # 482


def read_input(file: str):
    return InputReader.read_input(file)


def build_list_of_rooms(list_of_room_string: list[str]) -> list[Room]:
    return [Room(i) for i in list_of_room_string]


def print_solution_part_1(rooms: list[Room]):
    id_summator = RoomIDSummator(rooms)
    id_summator.calculate_id_sum_of_valid_rooms()
    print(f"The sum of sector IDs of the real rooms is {id_summator.id_sum}.")


def print_solution_part_2(rooms: list[Room]):
    northpole_objects_room_id = search_for_northpole_objects(rooms)
    print(f"The northpole objects are stored in room {northpole_objects_room_id}.")


def search_for_northpole_objects(rooms: list[Room]) -> int:
    for room in rooms:
        decryptor = RoomDecryptor(room)
        decrypted_room_name = decryptor.decrypt_room_name()
        if "northpole" in decrypted_room_name:
            return int(room.sector_id)
    return -1


if __name__ == "__main__":
    main()
