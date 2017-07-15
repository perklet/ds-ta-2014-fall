#include <stdio.h>
#include <stdlib.h>

#include "sorting.h"

#define LEN 11


void read_array (int* array, int length)
{
    int i;
    for (i = 0; i < length; i++) {
        scanf("%d", array+i);
    }
}


void print_array (int* array, int length)
{
    int i;
    for (i = 0; i < length; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

void copy_array (int* source, int* dest, int length)
{
    int i = length;
    while (i-->0) {
        dest[i] = source[i];
    }
}


int main (int argc, char** argv)
{
    int numbers[LEN];
    int temp_numbers[LEN];

    read_array(numbers, LEN);

    puts("original array is:");
    print_array(numbers, LEN);

    copy_array(numbers, temp_numbers, LEN);
    insertion_sort(temp_numbers, LEN);

    puts("sorted array is:");
    print_array(temp_numbers, LEN);

    return 0;
}
