package aoc2025.day03;

import aocUtils.InputReader;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        String filepath = "E:\\git\\advent_of_code\\input_2025\\03.txt";
        InputReader reader = new InputReader();
        List<String> lines = reader.readInput(filepath);

        System.out.println("Part 1: " + calculateTotalOutputJoltage(lines));
        System.out.println("Part 2: " + calculateTotalOutputJoltageMultipleKnots(lines, 12));
    }

    private static int calculateTotalOutputJoltage(List<String> lines) {
        return lines.stream().mapToInt(Main::calculateMaximumJoltage).sum();
    }

    private static int calculateMaximumJoltage(String bank) {
        char[] digitsAsChars = bank.toCharArray();
        List<Integer> digits = new ArrayList<>();
        for (char c : digitsAsChars) {
            digits.add(Integer.valueOf(String.valueOf(c)));
        }

        int max = -1;
        int posMax = -1;
        for (int i = 0; i < digits.size(); i++) {
            if (digits.get(i) > max) {
                max = digits.get(i);
                posMax = i;
            }
        }

        int maxJoltage = 0;

        for (int i = 0; i < posMax; i++) {
            int tempJoltage = digits.get(i) * 10 + max;
            if (tempJoltage > maxJoltage) {
                maxJoltage = tempJoltage;
            }

        }
        for (int i = posMax + 1; i < digits.size(); i++) {
            int tempJoltage = max * 10 + digits.get(i);
            if (tempJoltage > maxJoltage) {
                maxJoltage = tempJoltage;
            }
        }

        return maxJoltage;
    }

    private static long calculateTotalOutputJoltageMultipleKnots(List<String> lines, int usedBatteries) {
        return lines.stream().mapToLong(line -> calculateMaximumVoltageMultipleKnots(line, usedBatteries)).sum();
    }

    private static long calculateMaximumVoltageMultipleKnots(String bank, int usedBatteries) {
        StringBuilder resultString = new StringBuilder();

        char[] digitsAsChars = bank.toCharArray();
        List<Integer> digits = new ArrayList<>();
        for (char c : digitsAsChars) {
            digits.add(Integer.valueOf(String.valueOf(c)));
        }

        int maxPos = 0;
        for (int i = 0; i < usedBatteries; i++) {
            int offset = usedBatteries - i;

            int max = -1;
            for (int j = maxPos; j < digits.size() - offset + 1; j++) {
                if (digits.get(j) > max) {
                    max = digits.get(j);
                    maxPos = j + 1;
                }
            }
            resultString.append(max);
        }

        return Long.parseLong(resultString.toString());
    }


}
