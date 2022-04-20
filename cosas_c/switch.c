#include<stdio.h>
int main() {
	char ch;

	printf("Introduzca una vocal: "); 
	ch=getchar();  	
	switch(ch) {
		case 'a': puts("Se ha pulsado una a.");
			break;
		
		case 'e': puts("Se ha pulsado una e.");
			break;

		case 'i': puts("Se ha pulsado una i.");
			break;

		case 'o': puts("Se ha pulsado una o.");
			break;

		case 'u': puts("Se ha pulsado una u.");
			break;

		default: puts("Error Ingrese una vocal");

		}
	return 0;
}
