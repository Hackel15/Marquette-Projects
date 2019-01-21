//Unique Sorting method

//Using BOOL (no duplicates)
bool wasReadIn;
int num;
for(int i=0;i<50;i++){
	wasReadIn[i] = 0;	
}
for(int i=0;i<n;i++){
	cin >> num;
	wasReadIn[num]++;	
}
for(int i=0;i<50;i++){
	if(wasReadIn[i]>0){
		for(int j=0; j<wasReadIn[i]; j++){
			cout << i << " ";	
		}
	}
}

//Using INT (handles duplicates)
int wasReadIn;
int num;
for(int i=0;i<50;i++){
	wasReadIn[i] = 0;	
}
for(int i=0;i<n;i++){
	cin >> num;
	wasReadIn[num]++;	
}
for(int i=0;i<50;i++){
	if(wasReadIn[i]>0){
		for(int j=0; j<wasReadIn[i]; j++){
			cout << i << " ";	
		}
	}
}