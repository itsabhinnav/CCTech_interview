class Point:                   
    def __init__(self,x,y): 
        self.x = x
        self.y = y
def Calculate_surface(V,P):
    return 0
s=input() 
v=[float(i) for i in s[s.find('[')+2:s.rfind(']')-1].replace('[',"").replace(']',"").split(',')]
vertices=[]        
for i in range(0,len(v)//2):
    temp= Point(v[2*i],v[2*i+1])
    vertices.append(temp)
t=input()
p=[float(i) for i in t[t.find('[')+1:t.rfind(']')].split(',')]
point=Point(p[0],p[1])
print(point)
print(vertices)
surface=Calculate_surface(vertices,point)
print(surface)