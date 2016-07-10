#include <stdio.h>
#include <math.h>

/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

long largestPrimeFactor(long n) {

	long number = ceil(sqrt(n));
	
	while (1) {
		if ((number % 2 == 0 && number != 2) || (number % 3 == 0 && number != 3)) {
			number --;
			continue;
		}
		int aux = number;
		// Check prime
		for (long i = ceil(sqrt(number)); i > 1; i--) {
			if (number % i == 0) {
				aux = -1;
				break;
			}
		}

		if (aux == -1) {
			number--;
		} else {
			if (n % number == 0) {
				break;
			}
			number--;
		}
	}
	
	return number;
}

int main() {

	long lpf = largestPrimeFactor(600851475143);

	printf("Largest prime factor: %ld", lpf);

	return 0;
}
