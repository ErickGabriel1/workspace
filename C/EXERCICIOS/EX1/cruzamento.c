#include <stdio.h>
#include <unistd.h>

int main(){

int c = 0;
int choice = 0;
int time = 40;
int timer;

while(1){

    system("cls");
    timer = time - c;
    if (timer < 0) timer = 0;
    printf("Timer: %ds\n", timer);

    if (timer <= 0){
        choice++;
        c = -1;
        if (choice == 3){
            time = 20;
        }
        if (choice > 3){
            choice = 0;
            time = 40;
        }
        
    }

if (choice == 0){
    
    printf("Carros: \n");
    printf("Semaforo de Cima: \033[1;32mCOR\033[0m\n"); //VERDE
    printf("Semaforo de Baixo: \033[1;31mCOR\033[0m\n"); //VERMELHO
    printf("Semaforo da Esquerda: \033[1;31mCOR\033[0m\n"); //VERMELHO
    printf("\n");
    printf("Pedestres: \n");
    printf("Semaforo de Cima: \033[1;31mCOR\033[0m\n"); //VERMELHO
    printf("Semaforo de Baixo: \033[1;31mCOR\033[0m\n"); //VERMELHO
    printf("Semaforo de Esquerda: \033[1;32mCOR\033[0m\n"); //VERDE
    printf("Semaforo de Direira: \033[1;31mCOR\033[0m\n"); //VERMELHO

}

else if (choice == 1){

    printf("Carros: \n");
    printf("Semaforo de Cima: \033[1;31mCOR\033[0m\n"); //VERMELHO
    printf("Semaforo de Baixo: \033[1;32mCOR\033[0m\n"); //VERDE
    printf("Semaforo da Esquerda: \033[1;31mCOR\033[0m\n"); //VERMELHO
    printf("\n");
    printf("Pedestres: \n");
    printf("Semaforo de Cima: \033[1;32mCOR\033[0m\n"); //VERDE
    printf("Semaforo de Baixo: \033[1;31mCOR\033[0m\n"); //VERMELHO
    printf("Semaforo de Esquerda: \033[1;32mCOR\033[0m\n"); //VERDE
    printf("Semaforo de Direira: \033[1;31mCOR\033[0m\n"); //VERMELHO

}

else if (choice == 2){

    printf("Carros: \n");
    printf("Semaforo de Cima: \033[1;31mCOR\033[0m\n"); //VERMELHO
    printf("Semaforo de Baixo: \033[1;31mCOR\033[0m\n"); //VERMELHO
    printf("Semaforo da Esquerda: \033[1;32mCOR\033[0m\n"); //VERDE
    printf("\n");
    printf("Pedestres: \n");
    printf("Semaforo de Cima: \033[1;32mCOR\033[0m\n"); //VERDE
    printf("Semaforo de Baixo: \033[1;31mCOR\033[0m\n"); //VERMELHO
    printf("Semaforo de Esquerda: \033[1;31mCOR\033[0m\n"); //VERMELHO
    printf("Semaforo de Direira: \033[1;31mCOR\033[0m\n"); //VERMELHO


}

else if (choice == 3){

    printf("Carros: \n");
    printf("Semaforo de Cima: \033[1;31mCOR\033[0m\n"); //VERMELHO
    printf("Semaforo de Baixo: \033[1;31mCOR\033[0m\n"); //VERMELHO
    printf("Semaforo da Esquerda: \033[1;31mCOR\033[0m\n"); //VERMELHO
    printf("\n");
    printf("Pedestres: \n");
    printf("Semaforo de Cima: \033[1;32mCOR\033[0m\n"); //VERDE
    printf("Semaforo de Baixo: \033[1;32mCOR\033[0m\n"); //VERDE
    printf("Semaforo de Esquerda: \033[1;32mCOR\033[0m\n"); //VERDE
    printf("Semaforo de Direira: \033[1;32mCOR\033[0m\n"); //VERDE


}


    c++;
    sleep(1);

}

}