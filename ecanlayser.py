f = open("exp.csv")
data = f.read()
rows = data.split("\n")
amount =0

def total(filename):
  s=0
  with open(filename,"r") as f:
   data = f.read()
   rows = data.split('\n')
   for i in range(1,31):
      dt = rows[i].split(",")
      amount = int(dt[1])
      s+=amount
  return s   

print(total("exp.csv")) 

      
      


categories = set()

for i in range(1,31):
  dt = rows[i].split(",")
  categories.add(dt[2])

amount = 0
catamount = {}
for cat in categories:
  for i in range(1,31):
    dt = rows[i].split(",")
    if(cat == dt[2]):
      a = int(dt[1])
      amount = amount + a
  catamount[cat] = amount        

print(catamount)

p = max(catamount, key=catamount.get)
print(f"Top Category : {p} -> {catamount[p]}")

c = input("Enter the category :  ");
for i in range(1,31):
  dt = rows[i].split(",")
  if(c==dt[2]):
    print(f" {dt[3]} -> {dt[1]} ")

a = int(input("Enter the amount : "))
for i in range(1,31):
  dt=rows[i].split(",")
  if(a<=int(dt[1])):
    print(f"{dt[3]} -- {dt[2]} --> {dt[1]}") 
    


month = {1 :"January"  , 2: "February" , 3:"March" , 4:"April" , 5:"May" , 6:"June" , 7:"July", 8:"August", 9:"September", 10:"October", 11:"November",12:"December" } 
amount = 0
ma={}
for i in range(1,61):
    amount=0
    dt = rows[i].split(",");
    amount = int(dt[1]);
    d = dt[0].split("-");
    m = int(d[1]);
    m_name = month[m];
    if m_name not in ma:
        ma[m_name]=0;
    ma[m_name]+=amount; 




print(ma);   
f.close()