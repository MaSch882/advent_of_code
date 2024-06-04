package aoc2018.day02;

import aocUtils.InputReader;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {

    public static void main(String[] args) {
        String filepath = "C:\\_Python\\advent_of_code\\input_data\\2018\\2018_02.txt";
        InputReader reader = new InputReader();
        List<String> lines = reader.readInput(filepath);

        List<String> test = Arrays.asList("abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab");

        System.out.println("Part 1: " + calculateChecksum(lines));
        System.out.println("Part 2: ");
    }

    public static int calculateChecksum(List<String> lines) {
        int numberStringsDouble = 0;
        int numberStringsTriple = 0;

        for (String line : lines) {
            Map<Character, Integer> characterMultiplicity = new HashMap<>();
            for (char c : line.toCharArray()) {
                if (characterMultiplicity.containsKey(c)) {
                    characterMultiplicity.put(c, characterMultiplicity.get(c) + 1);
                } else {
                    characterMultiplicity.put(c, 1);
                }
            }

            boolean doubleFound = false;
            boolean tripleFound = false;

            for (Map.Entry<Character, Integer> entry : characterMultiplicity.entrySet()) {
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

}
