#include <iostram.h>
using namespace std; 

//Implementação da função recursiva

void hanoi(int n, I, II, III)
{
	if (n == 1) 
	{
		cout << "Move o disco " << << " de " << I << " para " << III << endl;
		return;
	}

	hanoi(n-1, I, III, II);
	cout << "Move o disco " << n << " de " << I << " para " << III << endl;
	hanoi(n-1, II, I, III);
}

//programa principal

int main()
{
	int n;

	cout << "Digite o número de discos: ";
	cin << n;
	
	//chamando a função hanoi

	hanoi(n, 'I', 'II', 'III');
	return 0;
}