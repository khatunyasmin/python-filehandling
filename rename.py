#import os
#os.rename("demo.txt","raj.txt")

#remove operation 


#os.remove("raj.txt")
#os list
"""docs=dir(os)
print(docs)"""
#new folder create
#os.mkdir("new fol")
# current dicrectory
"""str=os.getcwd()
print(str)"""
#os remove dir rmdir
#os.rmdir("C:/Users/yasmin/Desktop/py")

#change dir
#os.chdir("")
#copy the file
"""import shutil
shutil.copyfile("")"""
"""try:
    num=5
    den=0
    output=num/den
    print(output)
except:
    print("ERROR: Denominator cannot be ")  """
"""try:
    evennos=[8,12,16,4]   
    print(evennos[4])
except ZeroDivisionError:
    print(" Denominator can not be zero.")
except IndexError:
    print("index error")"""
"""try:
    evennos = [8,12,16,4]
    r = evennos[0]/0
    print(r)
    print(evennos[4])
except ZeroDivisionError:
    print("Denominator cannot be zero.")
except IndexError:
    print("Index Out Of Bounds.")  
except SyntaxError:
    print("Error in syntax.")"""
    
try:
    num=int(input("Enter a number:"))    
    assert num%2 ==0
except:
    print("not an even number.")  
else:
    reciporcal =1/num
    print(reciporcal) 
finally:
    print("inside finally block.")    
    


