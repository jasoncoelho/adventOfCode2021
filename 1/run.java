import java.io.File; // Import the File class
import java.io.FileNotFoundException; // Import this class to handle errors
import java.util.ArrayDeque;
import java.util.Scanner;

class Run {

    static final String inputFile = "input.txt";

    static private void partOne() {

        Integer prev = null;
        Integer counter = 0;

        try {
            File myObj = new File(inputFile);
            Scanner reader = new Scanner(myObj);
            while (reader.hasNextLine()) {
                Integer depth = Integer.parseInt(reader.nextLine());
                if (prev != null && depth > prev)
                    counter++;
                prev = depth;
            }
            reader.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        System.out.println("Part one counter " + counter);
    }

    static private void partTwo(int slidingWindowSize) {

        Integer prev = null;
        Integer counter = 0;

        Integer slidingWindowSum = 0;
        ArrayDeque<Integer> slidingWindow = new ArrayDeque<>();

        try {
            File myObj = new File(inputFile);
            Scanner reader = new Scanner(myObj);
            while (reader.hasNextLine()) {
                Integer depth = Integer.parseInt(reader.nextLine());

                // track the depth in the sliding window queue and also track sliding window sum
                slidingWindow.add(depth);
                slidingWindowSum += depth;

                if (slidingWindow.size() > slidingWindowSize) {
                    // if we are tracking enough depths we can start comparing the prev sliding sum
                    slidingWindowSum -= slidingWindow.pop();
                    if (prev < slidingWindowSum)
                        counter++;
                }
                prev = slidingWindowSum;
            }
            reader.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        System.out.println("Sliding Window = " + slidingWindowSize + " Part two Counter = " + counter);
    }

    public static void main(String[] args) {
        partOne();
        partTwo(1);
        partTwo(3);
    }

}