a= int(input("time stan  "))
match a:
     case 0:
          print("help")
     case 1:
         print("word not found ") 
     case _ if 1<a<12:

         print("good morning")
     case _ if 12<a<20:
          print("good afternoon")
     case _ if 20<a<24:
         print("good night")


      