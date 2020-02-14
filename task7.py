import pandas as pd #write to file
import csv #read csv and store data in lists (CLASSES, OOP)
endhour=[] #convert 0 to 24
endmin=[] 
starthour=[]
startmin=[]
final_endhour=[]
final_starthour=[]
#duration=[]
#final_cost=[]
#finalendhour2=[]
#duration2=[]
#duration=list(range(1,29))
#final_cost=list(range(1,29))

class Test: 
    def __init__(self): #returning multiple values using object
        with open("Interpreterclaim.csv") as file:
            reader=csv.DictReader(file)
            for row in reader:
                endhour.append(int(row['Service To (Hour)']))    
                endmin.append(int(row['Service To (Minute)'])) 
                starthour.append(int(row['Service From (Hour)']))
                startmin.append(int(row['Service From (Minute)']))
                final_endhour = [i if i != 0 else 24 for i in endhour]
                final_starthour = [i if i != 0 else 2 for i in starthour]
            self.endhour2=final_endhour.copy() #copylists
            self.endmin2=endmin.copy()
            self.starthour2=final_starthour.copy() #to prevent zero division error
            self.starthour3=starthour.copy()
            self.startmin2=startmin.copy()

def fun():
    return Test()

def divide_problem(hour1, hour2):
    quotient = 1
    num=hour1
    div=hour2
    remainder=0
    try:
        while num - (quotient * div) >= div: #remainder more than divider
            quotient += 1
        remainder = abs(num - (quotient * div))
    except ZeroDivisionError:
        remainder = 0
            
    remainderinmin = remainder*60
    return(remainderinmin)
#divide_problem(24, 23)

def minutes(min1, min2):
    value=60+min1-min2
    return(value)

def minutes2(min1, min2):
    value=abs(min1-min2)
    return(value)

def read_duration(final_endhour, endmin, final_starthour, startmin):
    duration=[]
    i=0
    while i<len(final_starthour):
        if endmin[i]<startmin[i]: #starthour
            a = final_endhour[i]
            b = final_starthour[i]
            c=endmin[i]  
            d=startmin[i]
            if a==1 and b==2 and c==0 and d==30:
                e=minutes2(c,d)
                duration.append(e)
                i=i+1
            elif a > b*2: #4:30am to 9.05am cannot use modulus
                g=(a-b-1)*60
                h=minutes(c,d)
                e=g+h
                duration.append(e)
                i=i+1
            else:
                fee = divide_problem(a-1, b)
                min=minutes(c, d) #2h30min
                e=int(fee+min)
                duration.append(e)
                i=i+1

        elif endmin[i]>startmin[i]: #00:00-21:00
            a = final_endhour[i]
            b = final_starthour[i]
            c=endmin[i]
            d=startmin[i]
            if a > b*2: #4am to 9am cannot use modulus
                g=(a-b)*60
                h=minutes2(c, d)
                e=g+h
                duration.append(e)
                i=i+1
            else:
                fee = divide_problem(a, b)
                min=minutes2(c, d) #30min
                e=fee+min
                duration.append(e)
                i=i+1
        elif endmin[i]==startmin[i] and (final_endhour[i]>(2*final_starthour[i])):  
            a = final_endhour[i]
            b = final_starthour[i]  
            e=(a-b)*60 
            duration.append(e)
            i=i+1                        

        elif endmin[i]==startmin[i] and (final_endhour[i]%final_starthour[i])!=0:                 
            a = final_endhour[i]
            b = final_starthour[i]
            e = divide_problem(a, b)
            duration.append(e) 
            i=i+1   
        
        elif (final_endhour[i]%final_starthour[i])==0: 
            a = final_endhour[i]
            b = final_starthour[i]
            #e = divide_problem(a, b)
            e = (a-b)*60
            duration.append(e) 
            i=i+1         
    return(duration)

def costing(duration2, finalendhour2, starthour, startmin, endmin):
    #initialize size of final_cost list before I can assign value final_cost[i] or I can append to empty list like above
    final_cost=duration2.copy() 
    #print("This is length of class finalendhour2", len(finalendhour2))
    j=0
    y=0
    cost=0.00
    while y<len(final_cost):
        while j<len(duration2):
            #1 time charges
            if finalendhour2[j]<=6 and starthour[j]<=6:
                if duration2[j]<60: #is nested if working?
                    cost=75.00
                    j=j+1
                    final_cost[y]=cost
                    #print(final_cost[y])
                else:
                    cost=75.00*(duration2[j]/60)
                    j=j+1
                    final_cost[y]=cost
                    #print(final_cost[y]) #print(cost, y)
                y=y+1

            elif 6<finalendhour2[j]<=21 and 6<starthour[j]<21: #no equal sign 
                if duration2[j]<60: #is nested if working?
                    cost=50.00
                    j=j+1
                    final_cost[y]=cost
                    #print(final_cost[y]) 
                else:
                    cost=50.00*(duration2[j]/60)
                    j=j+1
                    final_cost[y]=cost
                    #print(final_cost[y])
                y=y+1

            elif finalendhour2[j]>=21 and starthour[j]>20:
                if duration2[j]<60: #is nested if working?
                    cost=75.00
                    j=j+1
                    final_cost[y]=cost
                    #print(final_cost[y]) 
                else:
                    cost=75.00*(duration2[j]/60)
                    j=j+1
                    final_cost[y]=cost
                    #print(final_cost[y]) 
                y=y+1             
            #3x2 time charges; all sessions last less than a day

            elif 5<=finalendhour2[j]<=20 and starthour[j]<5: 
                cost=0 
                while duration2[j] > 0:  
                    duration2[j] = duration2[j] - 60
                    cost = cost+75.00
                    if (duration2[j]%60)!=0:
                        duration2[j] = duration2[j] - (duration2[j]%60) 
                        cost = cost + (75.00/60)*(duration2[j]%60)                
                    else:
                        duration2[j]=duration2[j]-60
                        cost = cost + 50.00  
                final_cost[y]=cost 
                #print(final_cost[y])
                y=y+1
                j=j+1                     

            #05:00-07:15
            elif finalendhour2[j]>6 and starthour[j]<6: #finalendhour2[j]>=6 and starthour[j]<=6:
                cost=0 
                if endmin[j]<startmin[j]: #if endmin[j]!=startmin[j]:
                    while duration2[j]>0:
                        cost = cost+(50.00/60)*(duration2[j]%60) 
                        duration2[j]=duration2[j] - (duration2[j]%60)
                        for i in range(0, (6-starthour[j])):
                            cost = cost +75.00 
                            duration2[j]=duration2[j]-60
                        for i in range(finalendhour2[j]%7):              
                            cost = cost + 50.00
                            duration2[j]=duration2[j]-60
                                     
                elif endmin[j]>startmin[j] and startmin[j]==0:
                    while duration2[j]>0:
                        for p in range(0, (6-starthour[j])):
                            cost = cost +75.00 
                            duration2[j]=duration2[j]-60
                        for p in range(finalendhour2[j]%6):
                            cost = cost+(50.00/60)*(duration2[j]%60) 
                            duration2[j]=duration2[j] - (duration2[j]%60)              
                            cost = cost +50.00
                            duration2[j]=duration2[j]-60

                elif endmin[j]>startmin[j] and startmin[j]!=0:
                    while duration2[j]>0:
                        for p in range(0, (6-starthour[j])):
                            cost = cost +75.00 
                            duration2[j]=duration2[j]-60
                        for p in range(finalendhour2[j]%7):
                            cost = cost+(50.00/60)*(duration2[j]%60) 
                            duration2[j]=duration2[j] - (duration2[j]%60)              
                            cost = cost +50.00
                            duration2[j]=duration2[j]-60
                
                elif endmin[j]==startmin[j] and startmin[j]==0:   #else: 
                    while duration2[j]>0:
                        for p in range(0, (6-starthour[j])):
                            cost = cost +75.00 
                            duration2[j]=duration2[j]-60
                        for p in range(0, (finalendhour2[j]-6)):
                            cost = cost+(75.00/60)*(duration2[j]%60) 
                            duration2[j]=duration2[j] - (duration2[j]%60)              
                            cost = cost + 50.00
                            duration2[j]=duration2[j]-60

                elif endmin[j]==startmin[j]:   #else: 
                    while duration2[j]>0:
                        for p in range(0, (6-starthour[j])):
                            cost = cost +75.00 
                            duration2[j]=duration2[j]-60
                        for p in range(0, (finalendhour2[j]-6)):
                            cost = cost+(50.00/60)*(duration2[j]%60) 
                            duration2[j]=duration2[j] - (duration2[j]%60)              
                            cost = cost + 50.00
                            duration2[j]=duration2[j]-60
                final_cost[y]=cost 
                #print(final_cost[y])
                y=y+1
                j=j+1

            #18:05-22:00
            elif finalendhour2[j]>21 and starthour[j]<21: #finalendhour2[j]>=20 and 5<starthour[j]<=20: 
                cost=0
                if endmin[j]<startmin[j]:
                    while duration2[j]>0:
                        for i in range(0, (20-starthour[j])):
                            cost = cost +50.00 
                            duration2[j]=duration2[j]-60
                        for i in range(finalendhour2[j]%21):
                            cost = cost+(75.00/60)*(duration2[j]%60) 
                            duration2[j]=duration2[j] - (duration2[j]%60)              
                            cost = cost + 75.00
                            duration2[j]=duration2[j]-60
                                     
                elif endmin[j]>startmin[j]:
                    while duration2[j] > 0:
                        for i in range(0, (21-starthour[j])):              
                            cost = cost + 50.00
                            duration2[j]=duration2[j]-60
                        for i in range(finalendhour2[j]%21): #21, 22, 23 
                            cost = cost+(75.00/60)*(duration2[j]%60)
                            duration2[j]=duration2[j] - (duration2[j]%60)           
                            cost = cost + 75.00 
                            duration2[j]=duration2[j]-60 
                
                elif endmin[j]==startmin[j] and startmin[j]==0:    
                    while duration2[j] > 0:                
                        for i in range(0, 21-starthour[j]):
                            cost = cost + 50.00                 
                            duration2[j]=duration2[j]-60 
                        for i in range(0,finalendhour2[j]-21): #21, 22, 23
                            cost = cost+(75.00/60)*(duration2[j]%60)
                            duration2[j]=duration2[j] - (duration2[j]%60) 
                            cost = cost + 75.00                 
                            duration2[j]=duration2[j]-60 
                elif endmin[j]==startmin[j] and startmin[j]!=0:    
                    while duration2[j] > 0:                
                        for i in range(0, 20-starthour[j]):
                            cost = cost + 50.00                 
                            duration2[j]=duration2[j]-60 
                        for i in range(0,finalendhour2[j]-20): #21, 22, 23
                            cost = cost+(75.00/60)*(duration2[j]%60)
                            duration2[j]=duration2[j] - (duration2[j]%60) 
                            cost = cost + 75.00                 
                            duration2[j]=duration2[j]-60 
                final_cost[y]=cost 
                #print(final_cost[y])
                y=y+1
                j=j+1
            
            elif finalendhour2[j]>=20 and starthour[j]>=21:
                cost=0
                while duration2[j] > 0:  
                    duration2[j] = duration2[j] - 60
                    cost = cost+ 75.00
                    if (duration2[j]%60)!=0:
                        duration2[j] = duration2[j] - (duration2[j]%60) 
                        cost = cost + (75.00/60)*(duration2[j]%60)
                    else:
                        duration2[j]=duration2[j]-60
                        cost = cost + 75.00
                final_cost[y]=cost 
                #print(final_cost[y])
                y=y+1
                j=j+1 
    
            else: #final_endhour[j]>=22 and 18==starthour[j]:
                cost=0
                while duration2[j] > 0: 
                    duration2[j] = duration2[j] - 60
                    cost = cost + 50.00 
                    if (duration2[j]%60)!=0:
                        duration2[j] = duration2[j] - (duration2[j]%60) 
                        cost = cost + (75.00/60)*(duration2[j]%60)
                    else:
                        duration2[j]=duration2[j]-60
                        cost = cost + 75.00
                final_cost[y]=cost 
                #print(final_cost[y])
                y=y+1
                j=j+1
    return(final_cost) 


def main():
    t=fun()
    #print(t.endhour2) #correct
    duration=read_duration(t.endhour2, t.endmin2, t.starthour2, t.startmin2)
    print(duration)
    DurationObj = pd.DataFrame(duration) 
    print(DurationObj)
    costofservice=costing(duration, t.endhour2, t.starthour3, t.startmin2, t.endmin2)
    print(costofservice)
    CostObj= pd.DataFrame(costofservice) 
    print(CostObj)
    with pd.ExcelWriter('Interpreter Claim.xlsx') as writer:
        DurationObj.to_excel(writer, sheet_name="Duration")
        CostObj.to_excel(writer, sheet_name="Cost")

    
if __name__ == '__main__':
    main()