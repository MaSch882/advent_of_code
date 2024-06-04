package aoc2018.day02;

import aocUtils.InputReader;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {

    public static void main(String[] args) {
        String filepath = "C:\\_Python\\advent_of_code\\input_data\\2018\\2018_02.txt";
        InputReader reader = new InputReader();
        List<String> lines = reader.readInput(filepath);

        System.out.println("Part 1: " + calculateChecksum(lines));
        System.out.println("Part 2: " + calculateCommonBoxLetters(lines));
    }

    public static int calculateChecksum(List<String> lines) {
        int numberStringsDouble = 0;
        int numberStringsTriple = 0;

        for (String line : lines) {
            Map<Character, Integer> charCount = new HashMap<>();
            for (char c : line.toCharArray()) {
                if (charCount.containsKey(c)) {
                    charCount.put(c, charCount.get(c) + 1);
                } else {
                    charCount.put(c, 1);
                }
            }

            boolean doubleFound = false;
            boolean tripleFound = false;

            for (Map.Entry<Character, Integer> entry : charCount.entrySet()) {
                if (entry.getValue() == 2) {
                    doubleFound = true;
                }
                if (entry.getValue() == 3) {
                    tripleFound = true;
                }
            }

            if (doubleFound) {
                numberStringsDouble++;
            }
            if (tripleFound) {
                numberStringsTriple++;
            }
        }
        return numberStringsDouble * numberStringsTriple;
    }

    public static String calculateCommonBoxLetters(List<String> lines) {
        for (int i = 0; i < lines.size(); i++) {
            String currentLine = lines.get(i);
            for (int j = i + 1; j < lines.size(); j++) {
                String compareLine = lines.get(j);
                int numberPosDiff = countNumberOfDifferentChars(currentLine, compareLine);

                if (numberPosDiff == 1) {
                    int position = getPositionOfDiffChar(currentLine, compareLine);
                    return currentLine.substring(0, position) + currentLine.substring(position + 1);
                }
            }
        }
        throw new IllegalStateException("There is no common box letters in this line.");
    }

    private static int countNumberOfDifferentChars(String a, String b) {
        int count = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) {
                count++;
            }
        }
        return count;
    }

    private static int getPositionOfDiffChar(String currentLine, String compareLine) {
        int position = -1;
        for (int k = 0; k < currentLine.length(); k++) {
            if (currentLine.charAt(k) != compareLine.charAt(k)) {
                position = k;
                break;
            }
        }
        return position;
    }


}
