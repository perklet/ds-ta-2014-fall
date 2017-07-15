#include <stdio.h>
#include <stdlib.h>

void insertion_sort (int* numbers, int n) 
{
    int i, j;
    int temp;

    for (i = 0; i < n; i++) {
        temp = numbers[i];
        for (j = i; j > 0 && numbers[j-1] > temp; j--) {
            numbers[j] = numbers[j-1];
        }
        numbers[j] = temp;
    }

}

