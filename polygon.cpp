#include<iostream>

using namespace std;
struct Point 
{
    int x;
    int y;
};

int isLeft( Point P0, Point P1, Point P2 )
{
    return ( (P1.x - P0.x) * (P2.y - P0.y)
            - (P2.x -  P0.x) * (P1.y - P0.y) );
}

int Pnt_Poly( Point P, Point* V, int n )
{
    int    wn = 0;    
    for (int i=0; i<n; i++) {  
        if (V[i].y <= P.y) {          
            if (V[i+1].y  > P.y)     
                 if (isLeft( V[i], V[i+1], P) > 0)  
                     ++wn;           
        }
        else {
            if (V[i+1].y  <= P.y)   
                 if (isLeft( V[i], V[i+1], P) < 0) 
                     --wn;         
        }
    }
    return wn;
}
int main() {
    struct Point P;
    int n = 4;
    struct Point V[4]={{1,2},{3,5},{4,6},{12,5}}; 
    cin >> P.x >> P.y ;     
    int res = Pnt_Poly(P , V , n) ;
    if(res==0){
        cout<<"False"; }
    else{
        cout << "True";
    }
    return 0;
}