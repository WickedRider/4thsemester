import java.util.*;
import java.io.*;


class Sol11 {
    public static void main(String[] args) {
        InputReader in = new InputReader(System.in);
        PrintWriter out = new PrintWriter(System.out);
        int n1 = in.nextInt();
        int[] n2 = new int[n1];
        for (int i = 0; i < n1; i++) {
            n2[i] = in.nextInt();
        }
        long startTime = System.currentTimeMillis();
        int final_value = Integer.parseInt(String.valueOf(absVal(n2, n2.length)));
        startTime = System.currentTimeMillis() - startTime;
        out.println(startTime);
        out.println(final_value);
        out.close();
    }

    public static int absVal(int[] arr, int size){
        Arrays.sort(arr);
        double a = Double.parseDouble(String.valueOf(arr[0]));
        double b = Double.parseDouble(String.valueOf(arr[size - 1]));
        return (int)Math.abs(a - b);
    }

    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream));
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }
    }
}