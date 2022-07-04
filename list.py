fruits = [ "apple","banana","cherry,orange"]
print(fruits[1])
#เปลี่ยนค่าในlist
fruits[1]="blackcurrent"
print(fruits)
fruits[1:3]=["banana","kiwi","melon"]
print(fruits)
fruits[1:3]=["blackcurrrent"]
print(fruits)
#เพิ่มค่าในlist
fruits.append("kiwi")
print(fruits)
fruits.insert(1,"banana")
print(fruits)
tropical = ["mango","pineapple","papaya"]
fruits.extend(tropical)
print(fruits)
#ลบค่าในlist
fruits.remove("pineapple")
print(fruits)
fruits.pop(3)
print(fruits)
#del fruits ลบทุกอย่างในlist
#เรียงคำในlist
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
#การรวมlist
vege=["carrot","potato","cucumber"]
all = fruits+vege
print(all)
#ปรินทร ศรีงาม ม.6/11 เลขที่ 30