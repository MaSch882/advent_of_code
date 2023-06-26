from Utils import input_processing
from structure_day_04_2016 import Room
from structure_day_04_2016 import RoomIDSummator
from structure_day_04_2016 import RoomValidator

filename = r"..\..\input_data\input_day_04_2016.txt"

testdata = ["aaaaa-bbb-z-y-x-123[abxyz]", "a-b-c-d-e-f-g-h-987[abcde]", "not-a-real-room-404[oarel]",
            "totally-real-room-200[decoy]"]


def main():
    # print_test_data()
    rooms = build_list_of_rooms(filename)

    print_solution_part_1(rooms)  #
    print_solution_part_2()  #


def build_list_of_rooms(file: str) -> list[Room]:
    input_strings = input_processing.read_input(file)
    return [Room(i) for i in input_strings]


def print_test_data():
    room1 = Room(testdata[0])
    room2 = Room(testdata[1])
    room3 = Room(testdata[2])
    room4 = Room(testdata[3])
    rooms = [room1, room2, room3, room4]
    for room in rooms:
        print_room_data(room)
    validator = RoomValidator(room3)
    print(validator.is_valid_room())
    roomcounter = RoomIDSummator(rooms)
    roomcounter.calculate_id_sum_of_valid_rooms()
    print(roomcounter.id_sum)


def print_room_data(room: Room):
    name = room.encrypted_name
    id = room.sector_id
    checksum = room.checksum
    print(f"Name: {name}; ID: {id}; Checksum: {checksum}.")


def print_solution_part_1(rooms: list[Room]):
    id_summator = RoomIDSummator(rooms)
    id_summator.calculate_id_sum_of_valid_rooms()
    print(f"The sum of sector IDs of the real rooms is {id_summator.id_sum}.")


def print_solution_part_2():
    pass


if __name__ == "__main__":
    main()
