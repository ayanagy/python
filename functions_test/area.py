
def calcArea(str):
            
    
                    
            if str=="t":     
                        num1=float(input("enter num1 : "))
                        num2=float(input("enter num2 : "))
                        return 0.5*num1*num2
            elif str=="s":
                        num3=float(input("enter num3 : "))
                        return num3*num3
            elif str=="r":
                        num4=float(input("enter num4 : "))
                        num5=float(input("enter num5 : "))
                        return num4*num5
            elif str=="c":
                        num6=float(input("enter num6 : "))
                        return 3.14*num6*num6
            else:
                        return "plz choose one of these char s,c,r,t"




print(calcArea("s")) 

                    