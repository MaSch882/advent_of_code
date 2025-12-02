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

        System.out.println("Part 1: " + calculateSumOfInvalidIds(ranges));
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

    private static Long calculateSumOfInvalidIds(List<Range> ranges) {
        long sum = 0L;
        for (Range range : ranges) {
            sum += calculateInvalidIds(range).stream().mapToLong(Long::longValue).sum();
        }
        return sum;
    }

    private static List<Long> calculateInvalidIds(Range range) {
        List<Long> invalidIds = new ArrayList<>();

        for (long i = range.getLowerBound(); i <= range.getUpperBound(); i++) {
            if (isInvalidId(i)) {
                invalidIds.add(i);
            }
        }

        return invalidIds;
    }

    private static boolean isInvalidId(long id) {
        String idAsString = ((Long) id).toString();
        int length = idAsString.length();
        if (length % 2 == 1) {
            return false;
        }

        // Ab hier ist die Laenge der Zahl gerade.
        char[] digits = idAsString.toCharArray();
        for (int i = 0; i < length / 2; i++) {
            if (digits[i] != digits[length / 2 + i]) {
                return false;
            }
        }

        return true;
    }
}
