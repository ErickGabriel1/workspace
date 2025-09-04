#include <stdio.h>
#include <stdlib.h>

int main(void){

    
    while (1)
    {
        system("cls");

        float altura, mass = 0;
        int idade = 0;
        char name[31];
        int c = 0;

        char choice = 0;
        printf("a - inserir altura\nm - inserir massa corporal\ni - inserir idade\nn - inserir nome\ne - exibir informacoes\n0 - fechar programa");
        printf("Digite um variável: ");
        scanf("%c", &choice);

        switch (choice)
        {
        case 'a':
            if (altura == 0){
                printf("Digite o valor da sua altura em metros: ");
                scanf("%f", &altura);
                c++;
            }
            else{
                printf("Valor já digitado!");
            }
            break;
        
        case 'm':
            if (mass == 0){
                printf("Digite o valor do seu peso kg: ");
                scanf("%f", &mass);
                c++;
            }
            else{
                printf("Valor já digitado!");
            }
            break;
        
        case 'i':
            if (idade == 0){
                printf("Digite o valor da sua idade:: ");
                scanf("%d", &idade);
                c++;
            }
            else{

                printf("Valor já digitado!");
            }
            break;
        
        case 'n':
            if (name[0] == '\0'){
                printf("Digite o seu nome: ");
                fgets(name, sizeof(name), stdin);
                c++;
            }
            else{
                printf("Valor já digitado!");
            }
            break;

        case 'e':
            if (c == 4)
            {   
                printf("O seu nome é: %s", &name[31]);
                printf("Sua idade é: %d", &idade);
                double IMC = 0;
                IMC = mass/altura*altura;
                printf("Seu IMC é: %f.2f", &IMC);
                return IMC;
            }
            
            break;

        case '0':
            return 0;
            break;
        
        default:
            printf("Valor inválido");
            break;

        }



    }
    
    return 0;
}