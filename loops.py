#if else and elif loops:
# a= int(input("what is the time now in the international format"))
import time
a =int(time.strftime('%H'))
print(a)
if(0<a<12):
    print("good morning")
elif(12<a<20):
    print("good afternoon")
elif(20<a<24):
    print("good night")
else:
    print("enter valid time")

#for in  and range function  use loops:
sur = 'suraj'
for i in sur:
    print(i ,  end=" , ")

print("\n")

for sur in range (0,13) :
  print(sur , end=" ,")

print("\n")

for sur in range (0,100,13) :
  print(sur , end=" ,")
print("\n")
#while loop and else with it 
i = 0
while(i<10):
    print(i , end=",")
    i= i + 1 
    
else: 
    print('this')


    
