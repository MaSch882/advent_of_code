from structure_day_10_2016 import FactorySimulation, InstructionParser

test_instructions = ["value 5 goes to bot 2",
                     "bot 2 gives low to bot 1 and high to bot 0",
                     "value 3 goes to bot 1",
                     "bot 1 gives low to output 1 and high to bot 0",
                     "bot 0 gives low to output 2 and high to output 0",
                     "value 2 goes to bot 2"]


def main():
    sim = FactorySimulation(test_instructions)

    test_instructions_sim = ["value 5 goes to bot 2", "value 3 goes to bot 2"]
    parsed_instructions_sim = InstructionParser.parse_commands(test_instructions_sim)

    sim.execute_value_command(parsed_instructions_sim[0])
    sim.execute_value_command(parsed_instructions_sim[1])

    print(sim)


if __name__ == "__main__":
    main()
