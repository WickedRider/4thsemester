/*							     *//* int_queue.h 						     *//* Example of using dynamic data structures in C    	     */
#include <stdio.h>#include <stdlib.h>
#define FALSE 0/* #define NULL 0 */
/* the list nodes type structure */typedef struct {    int     dataitem;    struct listelement *link;} listelement;
/* Function prototypes */void Menu (int *choice);listelement * AddItem (listelement * listpointer, int data);listelement * RemoveItem (listelement * listpointer);void ClearQueue (listelement * listpointer);
