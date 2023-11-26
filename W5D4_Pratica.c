#include <stdio.h>
#include <math.h>

int main ()
{
    double lato;

    printf("Inserisci un numero reale: \n");
    if (scanf("%lf", &lato) == 1)
    {
        printf("L'area del quadrato è: %lf \n",lato*lato);
        printf("L'area del cerchio è: %lf \n",(lato/2.0) * (lato/2.0) * M_1_PI);
        printf("L'area del triangolo equilatero è: %lf \n",(sqrt(3) / 4) * lato * lato);
    }
    else
    {
        printf("Input Errato \n");
    }
}
