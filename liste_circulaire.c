#include <stdio.h>
#include <stdlib.h>

typedef struct Element
{
  int nombre;
  struct Element *suivant ;
}Element;

typedef struct Liste
{
  Element *premier;
}Liste;
void init_list(Liste *liste)
{
  liste -> premier = NULL;
}

void ajouter_en_tete(Liste* liste ,int valeur)
{
  Element *nouvel_element = (Element*)malloc(sizeof(Element));
  nouvel_element-> nombre = valeur;
  nouvel_element-> suivant = liste-> premier;
  liste-> premier = nouvel_element;
}

int rechercher(Liste* liste ,int valeur)
{
  Element *actuel = liste-> premier;
  while(actuel != actuel){
    if(actuel-> nombre == valeur )
      {
      //si la valeur est trouvée
        return 1;
      }
    actuel = actuel-> suivant;
    }
     //sinon sortir
   return 0 ;
}

void ajouter_en_fin(Liste*liste,int valeur)
{
 Element * nouvel_element = (Element*)malloc (sizeof(Element));
 
 nouvel_element -> nombre = valeur;
 Element * actuel = liste-> premier;
 while (actuel -> suivant != liste-> premier)
  {
    actuel = actuel-> suivant;
  }
  actuel-> suivant= nouvel_element;
  nouvel_element -> suivant = liste-> premier;
  
}

void ajout_en_position(Liste*liste,int valeur,int position)
{
 Element *nouvel_element= (Element*)malloc(sizeof(Element));
 Element*tmp = liste -> premier;
 
 for(int i=0;i<position;i++)
   {
     tmp = tmp->suivant  ;
   }
 nouvel_element -> suivant = tmp -> suivant;
 tmp-> suivant = nouvel_element;
 }
   
void afficher_liste(Liste*liste)
{   
  Element*actuel = liste-> premier;
  while (actuel-> suivant != liste-> premier)
  { 
    actuel = actuel->suivant;
    printf("%d ->",actuel-> nombre);
  }
  printf("\n");

}


int main()
{
Liste * maliste;
int choix,valeur;
init_list(maliste);
  printf("1. Ajouter un element en tete de la liste circulaire");
  printf("2. Ajouter un element en fin de la liste circulaire");
  printf("3. Ajouter un element en une position de la liste circulaire");
  printf("4. Rechercher un element dans la liste circulaire"); 
  printf("5. Afficher la liste circulaire");
  
  switch (choix){
    case 1: ("system cls");
       printf("entrer la valeur a inserer en tete de liste : ");
       scanf("%d",&valeur);
       ajouter_en_tete(maliste,valeur);
   






