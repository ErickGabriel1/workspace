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
    printf("Seu IMC: %.2f\n", IMC);

    if (IMC < 18.5) {

        puts("Resultado: Abaixo do Peso");

    }
    
    else if (IMC >= 18.5 && IMC < 25) {
        
        puts("Resultado: Peso Normal");

    }
    else if (IMC >= 25 && IMC < 30){

        puts("Resultado: Sobrepeso");

    }
    else{

        puts("Resultado: Obesidade");

    }
    
    
    return 0;

}