#include <stdio.h>

int main(void) {

	int numero;

	printf("Escribe un numero: ");
	scanf("%d", &numero);

	if (numero % 2 == 0) {
			printf("El es par %i", numero);

	} else {
			printf("El numero no es par %i", numero);

	}

	return 0;
}
