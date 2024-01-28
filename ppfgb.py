import random
list = []

for i in range(10):
    list2 = []
    number_of_people_dinning = int(input("please enter the amount of people dinning in your party"))
    
    if number_of_people_dinning < 4:
        x = int(random.uniform(1,2.5))
        print(x, "minutes to be seated")
        list2.append(x)

    else:
    
        a = int(random.uniform(1,25))
        print(a, "minutes waited to be seated")
        list2.append(a)
        b = int(random.uniform(1,2.5))
        list2.append(b)
        print(b, "minutes to be seated")

    c = int(random.uniform(1,2))
    d = number_of_people_dinning*.75+c
    list2.append(d)
    print(d, "for server to arrive and for party to order food")

    t = int(random.uniform(15,25))
    list2.append(t)
    print(t, "minutes for all of the food ordered to cook")

    g = int(random.uniform(1,2.5))
    list2.append(g)
    print(g, "minutes it takes to serve the food")

    h = int(random.uniform(20,30))
    list2.append(h)
    print(h, "minutes is how long it takes for dinner party to eat their food")

    desert = (random.uniform(0,number_of_people_dinning))
    n = desert * .75+c
    list2.append(n)
    print(n, "minutes for server to arrive and for guests to order desert")

    if desert == 0:
        list2.append(0)
    else:
        
        r = int(random.uniform(3,5))
        list2.append(r)
        print(r, "minutes to prepare the dessert")
        
        j = int(random.uniform(1,2.5))
        list2.append(j)
        print(j, "minutes to serve the dessert to the people dinning")

        k = int(random.uniform(5,15))
        list2.append(k)
        print(k, "minutes eating desert before the dinner party leaves") 

    z = sum(list2)
    print(z, "minutes pass since the party arrived and left")


    list.append(z)
for yy in range(len(list)):
    print("This trial takes " + str(list[yy]) + " minutes")


average = sum(list)/len(list)    
print("Average dining time among all parties in simulation  is " + str(average)+ " minutes")

plot = []

for xx in range(len(list)):
    if list[xx] >= 65:
        points = list[xx] - 60
        points = int(points/5)
        ss = points * "*"
        plot.append(ss)
for xxx in range(len(plot)):
    print("trial "  + str(xxx) + "  " + str(plot[xxx]))

       
        

average = sum(list)/len(list)    
print("Average dining time among all parties in simulation  is " + str(average)+ " minutes")

input('press ENTER to exit')


         
         


