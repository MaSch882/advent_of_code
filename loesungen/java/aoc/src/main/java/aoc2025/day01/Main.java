package aoc2025.day01;

import aocUtils.InputReader;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Main {

    public static void main(String[] args) {
        String filepath = "E:\\git\\advent_of_code\\input_2025\\01.txt";
        InputReader reader = new InputReader();
        List<String> lines = reader.readInput(filepath);
        System.out.println("Part 1: " + crack_code(lines));
        System.out.println("Part 2: " + crack_code_complicated(lines));
    }

    public static int crack_code(List<String> lines) {
        int position = 50;
        int number_of_zeroes = 0;

        for (String line : lines) {
            String direction = line.substring(0, 1);
            int value = Integer.parseInt(line.substring(1));

            if (direction.equals("L")) {
                position -= value;
            }
            else {
                position += value;
            }
            position %= 100;

            if (position == 0) {
                number_of_zeroes++;
            }
        }


        return number_of_zeroes;
    }

    public static int crack_code_complicated(List<String> lines) {
        int position = 50;
        int number_of_zeroes = 0;

        for (String line : lines) {
            String direction = line.substring(0, 1);
            int value = Integer.parseInt(line.substring(1));

            for (int i = 0; i < value; i++) {
                if (direction.equals("L")) {
                    position -= 1;
                }
                else {
                    position += 1;
                }

                position %= 100;

                if (position == 0) {
                    number_of_zeroes++;
                }
            }
        }

        return number_of_zeroes;
    }



}
