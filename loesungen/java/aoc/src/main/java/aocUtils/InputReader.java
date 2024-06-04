package aocUtils;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class InputReader {
    public List<String> readInput(String path) {
        List<String> lines = new ArrayList<>();

        try (Scanner scanner = new Scanner(new FileReader(path))) {
            while (scanner.hasNext()) {
                lines.add(scanner.nextLine());
            }
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }

        return lines;
    }
}
