tuplefruits = ("apple","banana","cherry") #tuple
listfruits = ["apple","banana","cherry"] #list
print("original tuple:",tuplefruits)
print("original list:",listfruits)
#เปลี่ยนค่าในtuple
x=list(tuplefruits) #เเปลงเปลี่ยนlistเเล้วเก็บตัวเเปรx
x[1]="ิblueberry"
tuplefruits=tuple(x)
print("เปลี่ยนค่าtuple:",tuplefruits)
#เพิ่มค่าในtuple
x=list(tuplefruits) 
x.append("melon")
tuplefruits=tuple(x)
print("เพิ่มค่าในtuple:",tuplefruits)
#ลบtuple
x=list(tuplefruits)
x.remove("cherry")
tuplwfruit=tuple(x)
print("ลบค่าในtuple:",tuplefruits)
#่join tuple
vege=("tomato","cucumber","onion")
fruitsvege=tuplefruits+vege
print("join tuple",fruitsvege) 
x=range(3,6) #จะหยุดก่อนค่าstop
for n in x:
    print("range x:",n)
y=range(3,20,2)
for n in y:
    print("range y:",n)
    # ปรินทร ศรีงาม ม.6/11 เลขที่ 30