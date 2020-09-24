class Point:                   
    def __init__(self,x,y): 
        self.x = x
        self.y = y

def iv(P0,P1,C0,C1):
  y = ((P1.y-P0.y) / (P1.x-P0.x)) * (C0.x-P0.x) + P0.y
  x = C0.x
  temp = Point(x,y)
  return temp
  
def ih(p0,p1,h0,h1):
  x= ((p0.x + (h0.y-p0.y))*(p1.x-p0.x))/(p1.y-p0.y)
  y= h0.y
  temp = Point(x,y)
  return temp

def vd(p0,p1):
  return abs(p1.y-p0.y)

def hd(p0,p1):
  return abs(p1.x-p0.x) 
  
s=input() 
v=[float(i) for i in s[s.find('[')+2:s.rfind(']')-1].replace('[',"").replace(']',"").split(',')]
vertices=[]        
for i in range(0,len(v)//2):
    temp= Point(v[2*i],v[2*i+1])
    vertices.append(temp)
t=input()
p=[float(i) for i in t[t.find('[')+1:t.rfind(']')].split(',')]
point=Point(p[0],p[1])
V=sorted(vertices, key = lambda f : (f.x,f.y) )
if point.x < V[0].x : 
  h= vd(V[0],V[1])
  r= hd(V[1],V[3])
  dis=0
  for i in range(4,len(V)-2,2): 
    tmp = iv(point,V[i-1],V[i],V[i+1])
    if tmp.y < V[i+1].y:
      dis = vd(tmp,V[i+1])+hd(V[i+1],V[i+2])
    else:
      t = ih(point,V[i-1],V[i+1],V[i+2])
      dis = hd(t,V[i+2])
  surface = h+r+dis
  print(surface)
""" elif p.x >= vertices[0].x and p.y <= vertices[len(vertices)]:
  print("sun is in the middle")
else:
  print("sun is the right") """