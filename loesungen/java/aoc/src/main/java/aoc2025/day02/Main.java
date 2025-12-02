package aoc2025.day02;

import aocUtils.InputReader;
import org.apache.commons.lang3.StringUtils;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        String filepath = "E:\\git\\advent_of_code\\input_2025\\02.txt";
        InputReader reader = new InputReader();
        List<String> lines = reader.readInput(filepath);
        List<Range> ranges = getRanges(lines);

        System.out.println("Part 1: " + calculateSumOfInvalidIdsOneRepetition(ranges));
        System.out.println("Part 2: " + calculateSumOfInvalidIdsMultipleRepetition(ranges));
    }

    private static List<Range> getRanges(List<String> lines) {
        List<String> ids = List.of(lines.getFirst().split(","));

        List<Range> ranges = new ArrayList<>();
        for (String id : ids) {
            String[] split_id = id.split("-");
            long lowerBound = Long.parseLong(split_id[0]);
            long upperBound = Long.parseLong(split_id[1]);
            ranges.add(new Range(lowerBound, upperBound));
        }

        return ranges;
    }

    private static Long calculateSumOfInvalidIdsOneRepetition(List<Range> ranges) {
        long sum = 0L;
        for (Range range : ranges) {
            sum += calculateInvalidIdsOneRepetition(range).stream().mapToLong(Long::longValue).sum();
        }
        return sum;
    }

    private static List<Long> calculateInvalidIdsOneRepetition(Range range) {
        List<Long> invalidIds = new ArrayList<>();

        for (long i = range.getLowerBound(); i <= range.getUpperBound(); i++) {
            if (isInvalidIdOneRepetition(i)) {
                invalidIds.add(i);
            }
        }

        return invalidIds;
    }

    private static boolean isInvalidIdOneRepetition(long id) {
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

    private static Long calculateSumOfInvalidIdsMultipleRepetition(List<Range> ranges) {
        long sum = 0L;
        for (Range range : ranges) {
            sum += calculateInvalidIdsMultipleRepetition(range).stream().mapToLong(Long::longValue).sum();
        }
        return sum;
    }

    private static List<Long> calculateInvalidIdsMultipleRepetition(Range range) {
        List<Long> invalidIds = new ArrayList<>();

        for (long i = range.getLowerBound(); i <= range.getUpperBound(); i++) {
            if (isInvalidIdMultipleRepetition(i)) {
                invalidIds.add(i);
            }
        }

        System.out.println(range + " // " + invalidIds);

        return invalidIds;
    }

    private static boolean isInvalidIdMultipleRepetition(long id) {
        String idAsString = ((Long) id).toString();
        int length = idAsString.length();

        for (int divisor = 1; divisor <= length / 2; divisor++) {
            if (length % divisor != 0) {
                continue;
            }
            String substring = idAsString.substring(0, divisor);
            int numberOfOccurrences = StringUtils.countMatches(idAsString, substring);
            if (numberOfOccurrences == length / divisor) {
                return true;
            }
        }

        return false;
    }
}
