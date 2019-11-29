public class java_sort{
    public static void main(String args[])
    {
        MergeSort ob = new MergeSort();
        int arr[] = {12, 11, 13, 5, 6, 7};

        System.out.println("Given Array");
        ob.printArray(arr);
        ob.sort(arr, 0, arr.length-1);

        System.out.println("\nSorted array");
        ob.printArray(arr);
    }
}