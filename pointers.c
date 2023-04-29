// ===================================================
// Understanding pointers in python from C
// Author : 34zY
// Github : https://github.com/34zY
// Doc : https://devdocs.io/c/
// ===================================================
// Compile : gcc -o pointers.exe pointers.c

#include <stdio.h>

int main(void)
{
	// ===============================
	// Declaring variable & Data types
	int a = 333;
	printf("[*] Type of A : %s\n", sizeof(a) == sizeof(int) ? "int" : "unknown");
	printf("[*] Value of A : %d\n", a);
	// ===============================

	// ===============================
	// pointers
	int *ptr = &a;
	printf("[*] Variable Type (LP Pointer) : %s\n", sizeof(ptr) == sizeof(double *) ? "double" : "unknown");
	printf("[*] Pointer Value : %d\n", *ptr);
	printf("[*] Pointer Address : %d\n", &ptr);


	*ptr = 777; // changing the pointer value dynamically
	printf("[*] Value of A changed dynamically with pointer : %d\n", a);
	*ptr = 1234; // changing the pointer value dynamically
	printf("[*] Value of A changed dynamically with pointer : %d\n", a);
	*ptr = 159; // changing the pointer value dynamically
	printf("[*] Value of A changed dynamically with pointer : %d\n", a);
	// ===============================


	// ===============================
	// Casting on existing pointer
	int *new_ptr = ptr;
	printf("[*] Value of A changed pointer : %d\n", *new_ptr);
	// ===============================
	
	return 0;

}