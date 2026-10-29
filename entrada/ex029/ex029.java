package ex029;

import java.util.Arrays;

public class ex029 {
    public static void main(String[] args) {
        
        int num[] = {3,5,1,8,4};

        int pos = Arrays.binarySearch(num, 1);
        System.out.println(pos);
    }
}
