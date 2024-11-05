#include <iostream>
#include <string>
#include "helper.hpp"

#define EXIT_CACHE_NOT_CREATED 0x01

using namespace std;

char alphabet[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

int search(char *array, int len, char key) {
	for (int i = 0; i < len; i++) {
		if (*(array + i) == key) {
			return i;
		}
	}
	
	return -1;
}
	
int get_input(string *inputs) {
	cout << "\nEnter input string: ";
	cin >> *inputs;
	//cout << *inputs << endl;
	return 1;
}

int get_assembly(string *assembly) {
	string temp;
	cout << "\nEnter assembly combination: ";	
	cin >> temp;
	char reflector = temp.back();
	
	if (temp.length() != 4) {
		cout << "zamn" << endl;
		return -1;		
	}
	if (!(reflector == 'a' || reflector == 'b' || reflector == 'c')) { 
		cout << "gottem" << endl;
		return -1;
	}
	for (int i = 0; i < 3; ++i) { 
		if (temp[i] < '1' || temp[i] > '5') { 
			cout << "lollerz" << endl;
			return -1;
		} 
	}
	*assembly = temp;
	return 1;
}
		
int get_plugs(int *plugs) {
	int temp;
	cout << "\nEnter no. of swapped pairs: " ;
	cin >> temp;
	
	if (temp > 13 || temp < 0) {
		return -1;
	}
	
	*plugs = temp;
	return 1;
}

int get_wire(char* swap_list, string *wire, int iteration) {
	string temp;
	cout << iteration + 1 << ": ";
	cin >> temp;
	
	if (temp.length() != 2) {
		cout << "\nCANNOT SWAP MORE THAN TWO LETTERS AT ONCE! INVALID INPUT!" << endl;
		return -1;		
	}
	
	if (temp[0] == temp[1]) {
		cout << "CANNOT REPEAT LETTERS IN SAME PAIR! INVALID INPUT!" << endl;
		return -1;
	}
	
	for (int i = 0; i < 2; i++) {
		if (search(alphabet, 26, char(temp[i])) == -1) {
			cout << "\n" << char(temp[i]) << " IS NOT A VALID MEMBER OF THE LOWERCASE APLHABET! INVALID INPUT!" << endl;
		}
		if (search(swap_list, 13, char(temp[i])) != -1) {
			cout << "\nCANNOT REPEAT LETTERS FOR SWAPPING! INVALID INPUT!" << endl;
			return -1;
		}
	}
	
	*wire = temp;
	return 1;
}
	
int main() {
	help();
	
	string inputs;
	string assembly;
	int plugs = 0;
	string wire;
	
	char plug_swaps[13];
	
	int flag = 0;
	while (flag != 1) {
		flag = get_input(&inputs);
	}
	flag = 0;
	while (flag != 1) {
		flag = get_assembly(&assembly);
	}
	flag = 0;
	while (flag != 1) {
		flag = get_plugs(&plugs);
	}
	flag = 0;
	
	for (int i = 0; i < 13; i++) {
		plug_swaps[i] = '\0';
	}
	
	cout << "\nEnter plugboard combinations (eg.: ab, to swap A and B on the plugboard): " << endl;
	for (int j = 0; j < plugs; j++) {
		while (flag != 1) {
			flag = get_wire(plug_swaps, &wire, j);
		}
		flag = 0;
		*(plug_swaps + 2*j) = char(wire[0]);
		*(plug_swaps + 2*j + 1) = char(wire[1]);
	}
	
	char ch = '$';
	int iter = 0;
	
	cout << "\nInput: " << inputs << endl;
	cout << "Assembly Code: " << assembly << endl;
	
	if (plugs > 1) {
		cout << "Plugboard Swap Pairs: | ";
		
		while (ch != '\0') {
			ch = plug_swaps[iter];
			cout << ch << " ";
			if (iter % 2 != 0) {
				cout << "| ";
			}
			iter++;
		}
		cout << endl;
	}
	return 0;
}