#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MALLOC(p, s)\
if(!(p = malloc(s))){\
fprintf(stderr, "Insufficient Memory.\n");\
exit(EXIT_FAILURE);\
}

#define MAX_FILE_NAME 20
#define MAX_LINE 100
#define TRUE 1
#define FALSE 0

// Functions 
void input_data(FILE *fp, int *list, int *idx);
void search_number(FILE *fp, int *list, int data, int size); 

int main(void)
{
    FILE *fp; 
    char file_name[MAX_FILE_NAME];
    char line[MAX_LINE];
    char *token; 
    int search_n, num_n; 
    int i, j, search_idx = 0, num_idx = 0;
    int *search_list, *num_list; 

    printf("Input File Name? "); 
    scanf("%s", file_name);

    fp = fopen(file_name, "r");

    // 찾고자 하는 숫자 갯수, 전체 표본의 갯수 
    fgets(line, MAX_LINE, fp);
    token = strtok(line, " ");
    search_n = atoi(token); 
    token = strtok(NULL, " ");
    num_n = atoi(token); 

    // init search_list, num_list
    MALLOC(search_list, sizeof(*search_list) * search_n);
    MALLOC(num_list, sizeof(*num_list) * num_n);

    input_data(fp, search_list, &search_idx);     // 찾고자 하는 숫자들 목록 input
    input_data(fp, num_list, &num_idx);    // 표본의 자료들 input 

    // find search num 
    for(i = 0; i < search_idx; i ++) 
        search_number(fp, num_list, search_list[i], num_idx);
    printf("\n");

    fclose(fp);
}

void search_number(FILE *fp, int *list, int data, int size)
{
    int i; 
    int flag = FALSE;
    
    fp = fopen("output.txt", "w");
 
    for(i = 0; i < size; i ++) {
        if(list[i] == data) {
            printf("Yes ");
            // fprintf(fp, "Yes "); 
            return; 
        }
    }
    
    printf("NO "); 
    // fprintf(fp, "No "); 
}


void input_data(FILE *fp, int *list, int *idx)
{
    char line[MAX_LINE];
    char *token; 
    int i; 

    fgets(line, MAX_LINE, fp);
    token = strtok(line, " ");
    while(token) {
        list[(*idx)++] = atoi(token); 
        token = strtok(NULL, " ");  
    }

}