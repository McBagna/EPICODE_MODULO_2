#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>

void presentazioneGioco()
{
    printf("\n");
    printf("Ciao e Benvenuto o Benvenuta agli EPICODE GAMES.......... \n");
    printf("Viene estratto un candidato da ogni distretto o regione Italiana e solo il migliore sopravivvera'........ \n");
    printf("Se te la senti di giocare fai un bel respiro, deglutisci e poi premi il tasto A \n");
    printf("Se non hai abbastanza fegato invece premi B \n");
    printf("Non schiacciare altro, non funzionera'....... \n");
    printf("\n");
}

void giocaPartita()
{
    char nome[20];
    //char buffer[80];
    int contatore = 0;
    int risposta = 0;
    printf("\n");
    fflush(stdin);
    printf("Inserisci il tuo nome..... \n");
    fgets(nome,20,stdin);
    printf("Ciao %s partiamo con le domande",nome);
    printf("\n");
    /*
    snprintf(buffer,sizeof(buffer),"%s%s%s","Ciao ",nome," partiamo con le domande \n");

    Tentativo, miseramente fallito, di concatenare le stringhe in quanto dopo il %s va a capo a scrivere il resto
    */
    printf("Il router è un apparecchio di livello fisico >> 1 << oppure di livello sessione >> 2 << oppure di livello rete >> 3 << ? \n");
    scanf("%d",&risposta);
    if (risposta == 3)
    {
        contatore++;
    }
    printf("\n");
    printf("Nel linguaggio di programmazione C un numero senza virgola e' di tipo char >> 1 << oppure int >> 2 << oppure bool >> 3 <<");
    scanf("%d",&risposta);
    if (risposta == 2)
    {
        contatore++;
    }
    printf("Complimenti %s hai totalizzato %d punti \n",nome,contatore);
}

int main()
{
    char scelta = {'\0'};
    bool stopGame = false;
    presentazioneGioco();
    scanf("%c", &scelta);
    scelta = toupper(scelta);
    while ((scelta != 'A') || (scelta != 'B'))
    {
        if (scelta == 'A')
        {
            while (scelta == 'A')
            {
                giocaPartita();
                printf("\n");
                fflush(stdin);
                printf("Vuoi Giocare Ancora ? \n");
                scanf("%c",&scelta);
                scelta = toupper(scelta);
                if (scelta != 'A')
                {
                    stopGame = true;
                    break;
                }
                
            }
        }
        if (scelta == 'B')
        {
            printf("Addios...... \n");
            stopGame = true;
            break;
        }
        if (stopGame == true)
        {
            break;
        }
        presentazioneGioco();
        scanf("%c", &scelta);
        scelta = toupper(scelta);
    }
    return 0;
}
