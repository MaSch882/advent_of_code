from structure_day_04_2016 import Room
from structure_day_04_2016 import RoomTester

filename = r"..\..\input_data\input_day_04_2016.txt"

testdata = ["aaaaa-bbb-z-y-x-123[abxyz]", "a-b-c-d-e-f-g-h-987[abcde]", "not-a-real-room-404[oarel]",
            "totally-real-room-200[decoy]"]


def main():
    room1 = Room(testdata[0])
    room2 = Room(testdata[1])
    room3 = Room(testdata[2])
    room4 = Room(testdata[3])
    rooms = [room1, room2, room3, room4]

    for room in rooms:
        print_room_data(room)

    roomtester = RoomTester(room3)
    print(roomtester.symbol_counter)

    print_solution_part_1()  #
    print_solution_part_2()  #


def print_room_data(room: Room):
    name = room.encrypted_name
    id = room.sector_id
    checksum = room.checksum
    print(f"Name: {name}; ID: {id}; Checksum: {checksum}.")


def print_solution_part_1():
    pass


def print_solution_part_2():
    pass


if __name__ == "__main__":
    main()
