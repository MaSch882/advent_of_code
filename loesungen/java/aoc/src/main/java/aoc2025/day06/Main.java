package aoc2025.day06;

import aocUtils.InputReader;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        String filepath = "E:\\git\\advent_of_code\\input_2025\\06.txt";
        InputReader reader = new InputReader();
        List<String> lines = reader.readInput(filepath);
        System.out.println("Part 1: " + calculateGrandTotal(lines));
        System.out.println("Part 2: ");
    }

    private static BigInteger calculateGrandTotal(List<String> lines) {
        List<List<Long>> numbers = extractNumbers(lines);
        List<String> operatorsList = getOperatorsList(lines);

        BigInteger total = BigInteger.ZERO;

        for (int i = 0; i < operatorsList.size(); i++) {
            BigInteger step = null;
            if (operatorsList.get(i).equals("+")) {
                step = BigInteger.ZERO;
                for (List<Long> numberLine : numbers) {
                    step = step.add(BigInteger.valueOf(numberLine.get(i)));
                }
            }
            if (operatorsList.get(i).equals("*")) {
                step = BigInteger.ONE;
                for (List<Long> numberLine : numbers) {
                    step = step.multiply(BigInteger.valueOf(numberLine.get(i)));
                }
            }
            total = total.add(step);
        }

        return total;
    }

    private static List<String> getOperatorsList(List<String> lines) {
        String[] operators = lines.getLast().split(" ");
        List<String> operatorsList = new ArrayList<>();
        for (String operator : operators) {
            if ("".equals(operator)) {
                continue;
            }
            operatorsList.add(operator);
        }
        return operatorsList;
    }

    private static List<List<Long>> extractNumbers(List<String> lines) {
        List<List<Long>> numbers = new ArrayList<>();
        for (String line : lines) {
            if (line.equals(lines.getLast())) {
                continue;
            }
            String[] numbersAsStrings = line.split(" ");
            List<Long> numbersList = new ArrayList<>();
            for (String number : numbersAsStrings) {
                if ("".equals(number)) {
                    continue;
                }
                numbersList.add(Long.parseLong(number.trim()));
            }
            numbers.add(numbersList);
        }
        return numbers;
    }


}
