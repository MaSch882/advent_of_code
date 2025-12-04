package aoc2025.day04;

import aocUtils.InputReader;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {

    public static void main(String[] args) {
        String filepath = "E:\\git\\advent_of_code\\input_2025\\04.txt";
        InputReader reader = new InputReader();
        List<String> lines = reader.readInput(filepath);

        System.out.println("Part 1: " + countAccessiblePaperRolls(lines));
        System.out.println("Part 2: " + countAllRemovedPaperRolls(lines));
    }

    private static int countAccessiblePaperRolls(List<String> lines) {
        int numberOfRows = lines.size();
        int numberOfCols = lines.getFirst().length();

        int numberOfAccessiblePaperRolls = 0;
        for (int row = 0; row < numberOfRows; row++) {
            for (int col = 0; col < numberOfCols; col++) {
                if (isAccessiblePaperRoll(lines, row, col)) {
                    numberOfAccessiblePaperRolls++;
                }
            }
        }

        return numberOfAccessiblePaperRolls;
    }

    private static int countAllRemovedPaperRolls(List<String> lines) {
        int totalNumberOfRemovedPaperRolls = 0;
        int removedPaperRollsCurrentIteration = 0;
        do {
            Map<Integer, Integer> markedPaperRolls = new HashMap<>();

            markedPaperRolls = markPaperRolls(lines);
            removePaperRolls(lines, markedPaperRolls);

            removedPaperRollsCurrentIteration = markedPaperRolls.size();
            totalNumberOfRemovedPaperRolls += removedPaperRollsCurrentIteration;
        }
        while (removedPaperRollsCurrentIteration != 0);

        return totalNumberOfRemovedPaperRolls;
    }


    private static Map<Integer, Integer> markPaperRolls(List<String> lines) {
        Map<Integer, Integer> markedPaperRolls = new HashMap<>();

        for (int row = 0; row < lines.size(); row++) {
            for (int col = 0; col < lines.getFirst().length(); col++) {
                if (isAccessiblePaperRoll(lines, row, col)) {
                    markedPaperRolls.put(row, col);
                }
            }
        }

        return markedPaperRolls;
    }

    private static void removePaperRolls(List<String> lines, Map<Integer, Integer> markedPaperRolls) {
        for (Map.Entry<Integer, Integer> markedPaperRoll : markedPaperRolls.entrySet()) {
            String row = lines.get(markedPaperRoll.getKey());

            StringBuilder builder = new StringBuilder(row);
            builder.setCharAt(markedPaperRoll.getValue(), '.');

            String replaced = builder.toString();
            lines.set(markedPaperRoll.getKey(), replaced);
        }
    }

    private static boolean isAccessiblePaperRoll(List<String> lines, int row, int col) {
        if (lines.get(row).charAt(col) != '@') {
            return false;
        }
        return countNeighbours(lines, row, col) < 4;
    }

    private static int countNeighbours(List<String> lines, int row, int col) {
        int numberOfNeighbours = 0;

        int maxRowIndex = lines.size() - 1;
        int maxColIndex = lines.getFirst().length() - 1;

        char left = (col == 0) ? '.' : lines.get(row).charAt(col - 1);
        char right = (col == maxColIndex) ? '.' : lines.get(row).charAt(col + 1);
        char up = (row == 0) ? '.' : lines.get(row - 1).charAt(col);
        char down = (row == maxRowIndex) ? '.' : lines.get(row + 1).charAt(col);
        char leftUp = (row == 0 || col == 0) ? '.' : lines.get(row - 1).charAt(col - 1);
        char rightUp = (row == 0 || col == maxColIndex) ? '.' : lines.get(row - 1).charAt(col + 1);
        char leftDown = (row == maxRowIndex || col == 0) ? '.' : lines.get(row + 1).charAt(col - 1);
        char rightDown = (row == maxRowIndex || col == maxColIndex) ? '.' : lines.get(row + 1).charAt(col + 1);

        if (left == '@') {
            numberOfNeighbours++;
        }
        if (right == '@') {
            numberOfNeighbours++;
        }
        if (up == '@') {
            numberOfNeighbours++;
        }
        if (down == '@') {
            numberOfNeighbours++;
        }
        if (leftUp == '@') {
            numberOfNeighbours++;
        }
        if (rightUp == '@') {
            numberOfNeighbours++;
        }
        if (leftDown == '@') {
            numberOfNeighbours++;
        }
        if (rightDown == '@') {
            numberOfNeighbours++;
        }

        return numberOfNeighbours;
    }
}
