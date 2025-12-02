package aoc2025.day02;

import aocUtils.InputReader;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        String filepath = "E:\\git\\advent_of_code\\input_2025\\02.txt";
        InputReader reader = new InputReader();
        List<String> lines = reader.readInput(filepath);
        List<Range> ranges = getRanges(lines);

        System.out.println("Part 1: ");
        System.out.println("Part 2: ");
    }

    private static List<Range> getRanges(List<String> lines) {
        List<String> ids = List.of(lines.getFirst().split(","));

        List<Range> ranges = new ArrayList<>();
        for (String id : ids) {
            String[] splitted_id = id.split("-");
            long lowerBound = Long.parseLong(splitted_id[0]);
            long upperBound = Long.parseLong(splitted_id[1]);
            ranges.add(new Range(lowerBound, upperBound));
        }

        return ranges;
    }
}
