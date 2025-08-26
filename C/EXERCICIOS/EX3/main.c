#include <stdio.h>

int main(void){

    char nome[31];
    int idade = 0;
    float peso, altura;

    float IMC = 0;

    puts("Digite o seu nome:"); fgets(nome, sizeof(nome), stdin);

    puts("Digite a sua idade:"); scanf("%d", &idade);

    fflush(stdin);

    puts("Digite o seu peso:"); scanf("%f", &peso);

    fflush(stdin);

    puts("Digite a sua altura"); scanf("%f", &altura);
    
    IMC = peso/(altura*altura);
    printf("Seu nome: %sSua idade: %d\n", nome, idade);
    printf("Seu IMC: %.2f", IMC);
    
    return 0;

}