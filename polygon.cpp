#include<iostream>
#include<sstream>
#include<ctype.h>
#include<vector>

using namespace std;

struct Point 
{
    double x;
    double y;
};

int isLeft( Point P0, Point P1, Point P2 )
{
    return ( (P1.x - P0.x) * (P2.y - P0.y)
            - (P2.x -  P0.x) * (P1.y - P0.y) );
}

int Pnt_Poly( Point P, Point* V )
{
    int n;
    int len=4;   
    for (int i=0; i<len; i++) {  
        if (V[i].y <= P.y) {          
            if (V[i+1].y  > P.y)     
                 if (isLeft( V[i], V[i+1], P) > 0)  
                     ++n;           
        }
        else {
            if (V[i+1].y  <= P.y)   
                 if (isLeft( V[i], V[i+1], P) < 0) 
                     --n;         
        }
    }
    return n;
}

int main() {
    string s ;
    vector <int> temp;
    getline(cin,s);
    string input1 = s.substr(s.find('['),s.rfind(']')-s.find('['));
    for(int i=0;i< input1.length();i++){
        if(isdigit(input1[i])|| input1[i]=='-' || input1[i]=='.' || input1[i] == ',' ){
            temp.push_back(int(input1[i])-48);
        }
    }
    for(int i=0; i< temp.size() ;i++){
        cout << temp[i];
    }
    int n = temp.size()/2;
    struct Point V[n];
    for(int i=0;i<n;i++){
        V[i].x=temp[2*i];
        V[i].y=temp[2*i+1];
    }
    string s2;
    getline(cin,s2);
    string input2 = s2.substr(s2.find('['),s2.rfind(']')-s2.find('['));
    cout << input2;
    
    struct Point P; 
    int res=Pnt_Poly(P,V);
    if(res==0){
        cout << "False";
    }
    else{
        cout <<"True";
    }
    return 0;
}