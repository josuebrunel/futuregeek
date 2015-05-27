Title: Introduction aux Makefiles
Date: 2013-02-05
Satus: draft
Tags: makefile, c, c++,
Category: Programming
Author: Josue Kouka
Summary: Introduction au Makefile

###Makefile

Un **makefile** est tout simplement un fichier de configuration (script) contenant des instructions qui sont lus et executées par un programme de type **make** (gmake,...). 

####A quoi sert il ?

Il permet de construire automatiquement des ___executable___ (tres souvent) , des ___libraries___, des ___architectures___ de dossier ou des actions ___diverses___ . En gros , enormement de choses .

	:::irc
	Guillaume> Pourquoi ne pas juste ecrire un script shell, python pour le faire ?

La principale difference entre une **makefile** et un **script normal** est que les instructions d'un **makefile** ne sont executées que si **necessaires**, c.a.d qu'une action (règle) qui a deja été accomplie, ne sera plus reexecutée.

####Comment fonctionne t-il ?
Il fonctionne tout simplement par verification de statisfactions de dépendances. Je m'explique par l'algorithme qui suit :
Pour faire mon __tea__ (avec l'accent british s'il vous plait!!) j'ai généralement besoin d'une __cup__ , de l'eau 
et un __tea bag__ (twisted mind, get away!!!). On supposera qu'on a déja notre tasse.

1. Ai-je de l'eau chaude ?
	
	O : on passe a l'étape 2
	
	N : Sais-je comment me procurer de l'eau ?
		
		O : Satisfait -> étape 2
		
		N : impossible de creer de l'eau, je renvoie une erreur et je sors

2.  Ai-je du thé ?
	
	O : alors  étape 3
	
	N : Sais-je comment me procurer du thé ?
		
		O : je me procure du thé puis je vais à l'étape suivante
		
		N : jre renvoie une erreur

3. 	Je fais mon thé grace à mon eau et mon sac de thé


A la prochaine execution, on n'aura plus besoin de se procurer de l'eau par exemple, dans le cas ou la dependance
est toujours satisfaite .

####Comment ecrire un Makefile ?

Context : 

[Jimmy Mcmillan](http://www.youtube.com/watch?v=kcsNbQRU5TI) veut écrire 2 fonctions d'affichage pour son party. Etant le super programmeur de son party, il se lance :  

un fichier my_putchar.h

	:::c
	#ifndef __my_putchar__
	#define __my_putchar__
	void	my_putchar(char c);
	#endif

un fichier my_putchar.c

	:::c
	#include <my_putchar.h>

	void	my_putchar(char c){
		write(1,&c,1);
	}

un fichier my_putstr.h

	:::c
	#ifndef __my_putstr__
	#define __my_putstr__
	void	my_putstr(char *s);
	#endif

un fichier my_putstr.c

	:::c
	#include <my_putchar.h>
	#include <my_putstr.h>

	void	my_putstr(char *s){
		while(*s){
			my_putchar(*s);
			*s++ ;
		}
	}

un fichier main.c

	:::c
	#include<my_putchar.h>
	#incluce<my_putstr.h>

	int main(int argc, char **argv){
		my_putchar('O');
		my_putchar('m');
		my_putchar('g');
		my_putchar('!');
		my_putchar('\n');

		my_putstr("The Rent Is Damn Too High !!!\n");
		return 0 ;
	}


####complilation separee en ligne de commande

	:::console
	jimmy@mcmillan:~$cc -Wall -c main.c my_putchar.c my_putstr.c
	jimmy@mcmillan:~$ls *.o # pour lister les .o generes
	jimmy@mcmillan:~$cc main.o my_putchar.o my_putstr.o -o my_exe #generation de l'executable
	jimmy@mcmillan:~$./test
	Omg!
	The Rent Is Damn Too High !!!
	jimmy@mcmillan:~$

Faut avouer que si son projet a plus de 10 fichiers sources, ça devient tres vite fastidieux de tout taper a la main. 
Alors pour palier à cela, il decide d'ecrire un makefile bien commenté.

notre **makefile**

	:::makefile
	CC = cc  # le compliteur (e.g: g++, gcc, gccsense,...)

	#Les sources ou fichiers cibles
	SRC = my_putchar.c\
	      	my_putstr.c\
	     	main.c

	CFLAGS = -Wall -W -I./

	OBJ = $(SRC:.c=.o) # infference, les .o sont generés à partir des .c de manière implicite

	EXE = my_exe

	#Les differentes regles
	#La 1ere regles est la premiere appelee, donc il est vivement conseille de definir **all** comme etant la premiere

	all:$(EXE)
	#On peut definir une regle avec le nom d'une variable
	$(EXE):$($OBJ) #la regle $(EXE) depend de ($OBJ)
		$(CC) $(OBJ) -o $(EXE) $(CFLAGS)

	clean:
		rm -rf *.o *~

	fclean:clean 
		rm -rf $(EXE)

	re:fclean all

__NB__: Respecter l'**indentation**, sinon make renverra une erreur.

	:::console
	jimmy@mcmillan:~$make 
Appelle la regle __all__ et genere tous les fichiers de dependances
	
	:::console
	jimmy@mcmillan:~$make my_exe
	make: `my_exe' is up to date.
Appelle la regle __my_exe__ qui dans notre makefile correspond a 
	
	:::makefile
	$(EXE):$($OBJ) #la regle $(EXE) depend de ($OBJ)
		$(CC) $(OBJ) -o $(EXE) $(CFLAGS)

Et oui !! Une regle peut avoir nom du contenu d'une variable.
Vous avez surement remarque le message qui indique que la regle est deja satisfaite (^_~) .

Pour resumer, mcmillan a les dependances suivantes dans son makefile :

* __all__ depend de __exe__
* __exe__ depend de __obj__
* __fclean__ depend de __clean__
* __re__ depend de __fclean__ puis __all__ 

Je vous conseille de lire [ceci](http://gl.developpez.com/tutoriel/outil/makefile/) pour vous documenter sur les regles __d'inference__ .

Voila, j'espere que ca vous aura permet d'ecrire des makefiles simplistes mais utiles.