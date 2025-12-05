package aoc2025.day05;

import aocUtils.InputReader;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        String filepathLists = "E:\\git\\advent_of_code\\input_2025\\05_lists.txt";
        String filepathIngredients = "E:\\git\\advent_of_code\\input_2025\\05_ingredients.txt";
        InputReader reader = new InputReader();
        List<String> ranges = reader.readInput(filepathLists);
        List<String> ingredients = reader.readInput(filepathIngredients);

        List<String> testRanges = List.of("3-5", "10-14", "16-20", "12-18");
        List<String> testIngredients = List.of("1", "5", "8", "11", "17", "32");

        System.out.println("Part 1: " + countFreshIngredients(ranges, ingredients));
        System.out.println("Part 2: ");
    }

    private static int countFreshIngredients(List<String> ranges, List<String> ingredients) {
        int count = 0;

        List<List<Long>> allFreshIds = collectAllFreshIdRanges(ranges);

        for (String ingredient : ingredients) {
            long ingredientId = Long.parseLong(ingredient);

            for (List<Long> idRange : allFreshIds) {
                long lowerBound = idRange.getFirst();
                long upperBound = idRange.getLast();

                if (lowerBound <= ingredientId && ingredientId <= upperBound) {
                    count++;
                    break;
                }
            }

        }

        return count;
    }

    private static List<List<Long>> collectAllFreshIdRanges(List<String> ranges) {
        List<List<Long>> allFreshIdRanges = new ArrayList<>();

        for (String range : ranges) {
            String[] split = range.split("-");
            long lowerBound = Long.parseLong(split[0]);
            long upperBound = Long.parseLong(split[1]);

            allFreshIdRanges.add(List.of(lowerBound, upperBound));
        }

        return allFreshIdRanges;
    }

}
