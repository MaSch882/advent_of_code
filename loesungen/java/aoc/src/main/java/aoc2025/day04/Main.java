package aoc2025.day04;

import aocUtils.InputReader;

import java.util.List;

public class Main {

    public static void main(String[] args) {
        String filepath = "E:\\git\\advent_of_code\\input_2025\\04.txt";
        InputReader reader = new InputReader();
        List<String> lines = reader.readInput(filepath);

        System.out.println("Part 1: " + countAccessiblePaperRolls(lines));
        System.out.println("Part 2: ");
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
