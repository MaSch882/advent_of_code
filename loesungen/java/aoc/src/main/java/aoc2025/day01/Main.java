package aoc2025.day01;

import aocUtils.InputReader;

import java.util.List;

public class Main {

    public static void main(String[] args) {
        String filepath = "E:\\git\\advent_of_code\\input_2025\\01.txt";
        InputReader reader = new InputReader();
        List<String> lines = reader.readInput(filepath);
        System.out.println("Part 1: " + crackCode(lines));
        System.out.println("Part 2: " + crackCodeComplicated(lines));
    }

    public static int crackCode(List<String> lines) {
        int position = 50;
        int numberOfHits = 0;

        for (String line : lines) {
            String direction = line.substring(0, 1);
            int value = Integer.parseInt(line.substring(1));

            position = adjustPositionBasedOnNextValue(direction, position, value);
            numberOfHits = increaseNumberOfHits(position, numberOfHits);
        }


        return numberOfHits;
    }

    public static int crackCodeComplicated(List<String> lines) {
        int position = 50;
        int numberOfHits = 0;

        for (String line : lines) {
            String direction = line.substring(0, 1);
            int value = Integer.parseInt(line.substring(1));

            for (int i = 0; i < value; i++) {
                position = adjustPositionBasedOnNextValue(direction, position, 1);

                numberOfHits = increaseNumberOfHits(position, numberOfHits);
            }
        }

        return numberOfHits;
    }

    private static int adjustPositionBasedOnNextValue(String direction, int position, int value) {
        if (direction.equals("L")) {
            position -= value;
        } else {
            position += value;
        }
        position %= 100;
        return position;
    }

    private static int increaseNumberOfHits(int position, int number_of_zeroes) {
        if (position == 0) {
            number_of_zeroes++;
        }
        return number_of_zeroes;
    }

}
