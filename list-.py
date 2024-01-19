lit = [ 2,3,"suraj",8.33,True]#this is the way of writeing list 
print(lit)
print(type(lit))
#list index print
print(lit[0])
print(lit[0:])
print(lit[0:-3])
#jump index in the list it will jump index  written in 3 postion 
print(lit[0:5:2])
#list comprihension mean { complex calcution for making list }   
sur = [i*i for i in range(10) if  0 == i%2]
print(sur)
