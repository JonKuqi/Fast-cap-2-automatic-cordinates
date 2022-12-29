
from math import sqrt
from math import pow

print("Ky program bën ndarjen e një sipërfaqe katrore apo drejtkëndëshe në sa do pjese qe do perdoruesi, ne kodin qe përdoret nga FastCap2")
print("Nese është sipërfaqja katrore shkruani \"1\", nëse është sipërfaqë drejtkëndëshe shkruani \"2\" ")

pergjigjja = input("")

if pergjigjja == "1":
  print("Shkruaj gjatesine e pllakes:")
  gjatesia = input("a = ")
  gjeresia = gjatesia
  print("Gjatësia e pllakës katrore është: "+ gjatesia)
elif pergjigjja == "2":
  print("Shkruaj gjerësinë e pllakes:")
  gjatesia = input("a = ")
  print("Shkruaj gjatësinë e pllakes:")
  gjeresia = input("b = ")
  print("Gjerësia e pllakës drejtkëndëshe është: "+ gjatesia+" dhe gjatësia është: "+ gjeresia)
else:
  print("Pergjigjja duhet të jetë \"1\" ose \"2\"")



pjeset= input("Ne sa pjese doni ta ndani siperfaqen: ")

numri = sqrt(float(pjeset))

a = float(gjatesia)
b = float(gjeresia)
n = float(numri)

x1list = []
x2list = []

y1list = []
y3list = []


i=0
j=0 
k=0
l=0
m=0
o=0
p=0
q=0
r=0

x1_tool = []
x2_tool = []

#x1
while(j<n):
    x1_tool.append(j*a/n)
    j+=1

while(i<n):
  x1list.extend(x1_tool)
  i+=1

#x2     
while(k<n):
    x2_tool.append((k+1)*a/n)
    k+=1

while(l<n):
  x2list.extend(x2_tool)
  l+=1


#y1
while(m<n):
   while(o<n): 
     y1list.append(m*b/n)
     o+=1
   o=0 
   m+=1 

#y3
while(p<n):
   while(q<n): 
     y3list.append((p+1)*b/n)
     q+=1
   q=0 
   p+=1 

formated_x1 = [ '%.3f' % elem for elem in x1list ]   
formated_x2 = [ '%.3f' % elem for elem in x2list ]
formated_y1 = [ '%.3f' % elem for elem in y1list ]
formated_y3 = [ '%.3f' % elem for elem in y3list ]

with open('C:/Users/jonku/Desktop/rezultati.qui', 'w') as f:


  f.write("0 Keto jane kordinatat e siparfaqes me gjatesi "+str(a)+" te ndare ne "+str(round(pow(n,2)))+" pjese\n\n")
  r=0
  while(r<n*n):
     f.write("Q 1 "+str(formated_x1[r])+" "+str(formated_y1[r])+" 0.000  "+str(formated_x2[r])+" "+str(formated_y1[r])+" 0.000  "+str(formated_x2[r])+" "+str(formated_y3[r])+" 0.000  "+str(formated_x1[r])+" "+str(formated_y3[r])+" 0.000  \n")
     if (r+1)%n==0:
        f.write("\n")
     r+=1

print("Programi është kryer me sukses. Kontrolloni file rezultati.qui")     




