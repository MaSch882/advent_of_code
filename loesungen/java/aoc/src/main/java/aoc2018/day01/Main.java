package aoc2018.day01;

import aocUtils.InputReader;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Main {

    public static void main(String[] args) {
        String filepath = "C:\\_Python\\advent_of_code\\input_data\\2018\\2018_01.txt";
        InputReader reader = new InputReader();
        List<String> lines = reader.readInput(filepath);
        System.out.println("Part 1: " + sumAllFrequencies(lines));
        System.out.println("Part 2: " + calculateFirstFrequencyReachedTwice(lines));
    }

    public static int sumAllFrequencies(List<String> lines) {
        return lines.stream().mapToInt(Integer::parseInt).sum();
    }

    public static int calculateFirstFrequencyReachedTwice(List<String> lines) {
        List<Integer> frequencies = lines.stream().map(Integer::parseInt).toList();
        Set<Integer> frequenciesReached = new HashSet<Integer>();

        int index = 0;
        int sum = 0;

        while (true) {
            sum += frequencies.get(index);

            if (frequenciesReached.contains(sum)) {
                return sum;
            } else {
                frequenciesReached.add(sum);
            }

            index++;
            if (index >= frequencies.size()) {
                index = 0;
            }
        }

    }

}
