object kotlin_sort {
    @JvmStatic
    fun main(args: Array<String>) {
        val ob = sorting()
        val arr = intArrayOf(12, 11, 13, 5, 6, 7)
        println("Given Array")
        sorting.printArray(arr)
        ob.sort(arr, 0, arr.size - 1)
        println("\nSorted array")
        sorting.printArray(arr)
    }
}