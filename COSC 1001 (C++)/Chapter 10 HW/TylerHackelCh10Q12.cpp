//Chapter 10 HW
#include <iostream>
#include <string>

using namespace std;
//prototype
void enterPassword(string& password);
bool sixOrMoreChar(const string password);
bool containNumber(const string password);
bool lowerCase(const string password);
bool upperCase(const string password);

int main(){
	string userPassword;
	
	enterPassword(userPassword);
	cout << "Password is sufficient.\n";
	cout << "Your password is: " << userPassword;
	
	return 0;
}

void enterPassword(string& password){
	bool flag = true;
	
	do{
    	flag = true;
    	cout << "Enter a password that fits the following criteria.\n";
    	cout << "-6 or more characters\n" << "-at least 1 upper and lowercase\n";
    	cout << "-at least 1 digit\n";
    	getline(cin, password);
    	cout << endl;
    	
        if(!(sixOrMoreChar(password))){
            flag = false;   
        }
        if(!(upperCase(password))){
            flag = false;   
        }
        if(!(lowerCase(password))){
            flag = false;   
        }
        if(!(containNumber(password))){
            flag = false;   
        }
        
	}while(!(flag == true));
	
	return;
}

bool sixOrMoreChar(const string password){
	int numRequirement = 6;
	if(password.size() >= numRequirement){
		return true;
	}
	else{
		cout << "Password does not contain 6 or more characters.\n" << endl;
		return false;
	}
}

bool upperCase(const string password){
	for(int i = 0; i < password.length(); i++){
		if (isupper(password[i])){
			return true;
		}
	}
	cout << "Password does not contain uppercase!\n" << endl;
	return false;
}

bool lowerCase(const string password){
	for(int i = 0; i < password.length(); i++){
		if(islower(password[i])){
			return true;  
		}
	}
	cout << "Password does not contain lowercase!\n" << endl;
	return false;
}

bool containNumber(const string password){
	for(int i = 0; i < password.length(); i++){
		if(isdigit(password[i])){
			return true;
		}
	}
	cout << "Password does not contain number!\n" << endl;
	return false;
}



/**

Q28
for(int x = 0; x < strlen(myArray); x++){
	if(isalpha(myArray[x]) == 0 ){
		break;
	} 
}

Q46
char x[] = 'a',
	 y[] = 'a';
if(strcmp(x, y) == 0){
	exit(0);
}

*/
