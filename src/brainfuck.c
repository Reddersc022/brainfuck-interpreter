/*
 * Pretty much the same code as brainfuck.py but in c
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define ARR_SIZE 30000
#define MAX_DEPTH 300


char *sort_file(char *fname) {
    FILE *fp = fopen(fname, "r");

    // Get size
    fseek(fp, 0, SEEK_END);
    size_t length = ftell(fp);
    fseek(fp, 0, SEEK_SET);

    // Allocate and read
    char *buffer = malloc(length);
    if (buffer) {
        fread(buffer, 1, length, fp);
    }

    return buffer;
}


void sort_error(unsigned int ins_p, char *message) {
    printf("** Error at %d\n", ins_p);
    puts(message);
}


int main(int argc, char *argv[]) {
    if (argc != 2) {
        puts("Please provide a file to interpret");
        return 1;
    }

    unsigned int array[ARR_SIZE] = {0};
    unsigned int arr_p = 0;
    unsigned int ins_p = 0;

    char ins;
    unsigned int val;
    unsigned int depth;

    char inp;

    bool in_loop = false;
    unsigned int loop_stack[MAX_DEPTH];
    unsigned int loop_s_p = 0;

    char *code = sort_file(argv[1]);
    while (code[ins_p] != '\0') {
        ins = code[ins_p];

        switch (ins) {
            case '>':
                if (arr_p < ARR_SIZE-1) {
                    arr_p++;
                } else {
                    sort_error(
                        ins_p,
                        "Array pointer should not be greater than array length"
                        );
                    return -1;
                }
                break;
            case '<':
                if (arr_p > 0) {
                    arr_p--;
                } else {
                    sort_error(
                        ins_p,
                        "Array pointer should not be less than 0"
                        );
                    return -1;
                }
                break;
            case '+':
                array[arr_p]++;
                break;
            case '-':
                array[arr_p]--;
                break;
            case '.':
                val = array[arr_p];
                printf("Output: %c (int: %d)\n", val, val);
                break;
            case ',':
                inp = getchar();
                getchar();  //  Consume newline
                array[arr_p] = (unsigned int)inp;
                break;
            case '[':
                if (array[arr_p] == 0) {
                    depth = 0;
                    while (depth >= 0) {
                        ins_p++;
                        ins = code[ins_p];
                        switch (ins) {
                            case '[':
                                depth++;
                                break;
                            case ']':
                                depth--;
                                break;
                        }
                    }
                } else {
                    in_loop = true;
                    loop_stack[loop_s_p++] = ins_p;
                }
                break;
            case ']':
                if (!in_loop) {
                    sort_error(
                        ins_p,
                        "Found `]` when not in loop"
                        );
                    return -1;
                } else if (array[arr_p] == 0) {
                    loop_s_p--;
                } else {
                    ins_p = loop_stack[loop_s_p-1];
                }
                break;
        }

        ins_p++;
    }

    return 0;
}
