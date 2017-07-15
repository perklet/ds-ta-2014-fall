#include <stdio.h>
#include <stdlib.h>






void msort (int* numbers, int* temp, int left, int right)
{
    int center;
    if (left < right) {
        center = (left + right) / 2;
        msort(numbers, temp, left, center);
        msort(numbers, temp, center+1, right);
        merge(numbers, temp, left, center+1, right);
    }
}



void merge_sort (int* numbers, int length)
{
    int* temp_array = malloc(sizeof(int)*length);
    if (temp_array != NULL) {
        msort(numbers, temp_array, 0, length-1);
        free(temp_array);
    } else {
        fprintf(stderr, "malloc error!");
    }

}
