#include <iostream>
#include <cmath>
int main()
{
// std is the name space where cout lives 
// using the std prefix make sure there is no 
// ambiguity about where this function exits
// use
	using std::cout; // now I don't have to include the 
	// prefix before every cout statement
	cout << "Hi!" << std::endl;
	// if I want to use everything in the namespace std
	// then 'using namespace std;' will suffice 
	cout << "Please enter a number: ";
	int x;
	std::cin >> x; // reads a number from the console 
	x = pow(x, 2);
	std::cout << "The number squared is: " << x << std::endl;
	return 0;
}
