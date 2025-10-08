#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main()
{
    srand(time(NULL));
    int random_n = 0;
    int difficult = 40;
    int choice = 0;
    int n_bombs = 0;
    int bombs_found = 0;
    printf("Enter the size of your minefield: ");
    scanf("%d", &choice);
    char map [choice][choice];
    char hidden_map [choice][choice];

    for (int c = 0; c < choice;c++)
        {
            for(int i = 0; i < choice; i++)
            {   
                random_n = rand()%100;

                if (random_n >= difficult) 
                {
                    map[c][i] = '1';
                    hidden_map[c][i] = '#';
                    n_bombs++;
                }

                else if (random_n < difficult)
                {
                    map[c][i] = '0';
                    hidden_map[c][i] = '#';
                }
                
            }
        }


    while (1)
    {

        for (int c = 0; c < choice;c++)
        {
            for(int i = 0; i < choice; i++)
            {   
                if (hidden_map[c][i] == '0')
                {
                    printf("\033[32m%c\033[0m  ", hidden_map[c][i]);
                }
                else
                {
                    printf("%c  ", hidden_map[c][i]);
                }
            }
            printf("\n");
        }

        int counter = 0;
        
        int row, column;
        printf("\nEnter the row (0-%d): ", choice-1);
        scanf("%d", &row);
        printf("\nEnter the column (0-%d): ", choice-1);
        scanf("%d", &column);

        if (map[row][column] == '0')
        {
            bombs_found++;
            hidden_map[row][column] = map[row][column];
            for (int x = row-1; x <= row+1; x++)
            {
                for (int y = column-1; y <= column+1; y++)
                {
                    if (x < 0 || x >= choice || y < 0 || y >= choice)
                        continue;
                    if (x == row && y == column)
                        continue;
                    if (map[x][y] == '1')
                        counter++;
                    else {
                        hidden_map[x][y] = map[x][y];
                        bombs_found++;
                    }
                        
                }
            }
            
            system("cls");
            printf("\nThere are %d bombs around the coordinate (%d, %d)\n", counter, row, column);
            printf("number of bombs found: %d\n", bombs_found);

            if (n_bombs == bombs_found){
                printf("\nYou win!");
                return 1;
            }

        }
        else
        {
            printf("You lose!\n");



            return 0;
        }


    }
}