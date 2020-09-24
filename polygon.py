class Point:                   
    def __init__(self,x,y): 
        self.x = x
        self.y = y

def isLeft(P0,P1,P2 ):
    return (P1.x - P0.x) * (P2.y - P0.y) - (P2.x -  P0.x) * (P1.y - P0.y) 

def PntInPoly( P, V ):   
    n=0
    for i in range(0,len(V)-1): 
        if V[i].y <= P.y :         
            if  V[i+1].y  > P.y :     
                 if isLeft( V[i], V[i+1], P) > 0:  
                    n=n+1         
        else : 
            if V[i+1].y  <= P.y :   
                 if isLeft( V[i], V[i+1], P) < 0: 
                    n=n-1  
    return n

s=input() 
v=[float(i) for i in s[s.find('[')+1:s.rfind(']')].replace('[',"").replace(']',"").split(',')]
vertices=[]        
for i in range(0,len(v)//2):
    temp= Point(v[2*i],v[2*i+1])
    vertices.append(temp)
t=input()
p=[float(i) for i in t[t.find('[')+1:t.rfind(']')].split(',')]
point=Point(p[0],p[1])
res=PntInPoly(point,vertices)  
print(False if res==0 else True)