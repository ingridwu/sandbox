#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char* argv[]){
    int number, fib_result;
    int i, int_flag = 1;
    printf("Total args is %d\n", argc);
    if(argc == 2){
        for(i=0;i < strlen(argv[1]); i++){
            if (!isdigit(argv[1][i])){
                int_flag = 0;
                break;
            }
        }
        if (int_flag){
            number = atoi(argv[1]);
            fib_result = Fib(number);
            printf("The result of Fib %d is %d\n", number, fib_result);
        }else{
            printf("Incorrect input, usage ./Fib [number]\n");
            return -1;
        }
    }else{
        printf("Incorrect input, usage ./Fib [number]");
        return -1;
    }
    return 0;
}
int Fib(int number){
    if (number == 0 || number == 1){
        return 1;
    }else{
        return Fib(number-1)+Fib(number-2);
    }
}
