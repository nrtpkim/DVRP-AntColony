#### start index 1 all of list
#### index 0 just dummy

def Timer():
    
    return t


def Numberofcity():

    return n

def typecar():

    return ncar

def numbercar():

    return quantity_car


def demand_now():
    
    #set demand new !!!!!!!
   
    return demand

def Check(ordertime, demand, t, n ):
    
    
    ordertime_check = ordertime
    #demand = ProbOrder.Dem()

    demand_check = demand

    t_check = Timer()
    n_check = Numberofcity()

    loopindex_check = [0]
    for i in range(1,n_check+1):
        loopindex_check.append(0) #= [0,0,0,0,0,0,0,0]

        
    for y in range(1, n_check + 1):
        ###################
        if t_check >= ordertime_check [y] [1] and demand_check [y] [2] > 0 :
        ###################
            loopindex_check [y] = 1 
        #endif
    #next y
    
    return loopindex_check

def Check_demand(loopindex_ant): #reset
    
    dem = demand_now() # dem = demand [0,[1,ขนาด,จำนวน],[2,1,2]]
    n = len(loopindex_ant) - 1
    
    demand_checkdem = []
    demand_checkdem.append(0)

    loopindex_checkdem = []
    loopindex_checkdem.append(0)
    #................



    #loopindex_checkdem = loopindex


    #############
    for i in range(1, n +1 ):
        demand_checkdem.append([]) 
        loopindex_checkdem.append(loopindex_ant [i])
        for j in range(0,3):
            demand_checkdem[i].append(dem [i] [j])

    
    for i in range(1, n + 1):
        if loopindex_checkdem [i] == 0:
            demand_checkdem [i] [2] = 0 
        #endif
    #next y
    #################
    
    return demand_checkdem


def heuristic_f(): # สร้างค่า heuristic

    import ProbLocate #distance
    city = ProbLocate.LocCity() #distanct

    n = len (city)-1
    
    #ฮิวริสติกส์เริ่มต้น_________________________________
    heuristicf = [[]]
    for i in range(1 ,n + 1):
        heuristicf.append([i])
        for j in range(1, n + 1):

            if city [i] [j] == 0:
                heuristicf[i].append(1000)
            else:
                heuristicf[i].append( 1 / city[i] [j] ) #heuristic = 1/d
        #next j

    #next i
    #_____________________________________________
    return heuristicf


def CompareDistance(rute): #f_comparedistance
    import ProbLocate #distance
    city = ProbLocate.LocCity() #distanct

    num = len(rute) - 1
    distance = 0 #[0,1,2,3,1,0,1,2,3,1]

    for i in range (1,num +1):
        if rute[i-1] ==0:
            k = 1
        elif i >= 2 and rute [i] != 0:
            destination = rute[i]
            distance = city [k] [destination] + distance

            k = rute[i]

        #end if
    #next i

    return distance


def AntColony(loopindex): # step ant Colony


    
    import random
    import ProbLocate #distance
    

    #detting import______________________________
    city = ProbLocate.LocCity() #distanct

    demanddummy = 0 # เรียกค่าใหม่

    #loopindex =  #เปิดเดินทุกเมือง
    #___________________________________________


    #variable___________________________________
    n = len(city[1]) - 1 #number of city
    sumdemand = 0

    rute = []
    rute_all = [[]]

    d = 0
    u = 0
    k = 1
    destination = 1

    itelation = 5
    ant = 20

    alpha = 3     
    beta = 1

    evaporation = 0.5


    best_distance = 9999

    pheromone = [[]]
    pheromone_power = []

    heuristic = [[]]
    heuristic_power = []

    pheromone_dot_heuristic= [] #array
    sum_pheromone_dot_heuristic = [0] #tuple 7 city
    p_xy = []
    #___________________________________________



    #ฟีโรโมนเริ่มต้น___________________________________
    for i in range(1 ,n + 1):
        pheromone.append([i])
        for j in range(1, n + 1):
            pheromone[i].append(0.1) # [[], [1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], 
                                 #      [2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], 
                                 #  #   [3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], 
                                 #  #   [4, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], 
                                 #      [5, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], 
                                 #      [6, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], 
                                 #      [7, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]]

        #next j
    #next i
    #_____________________________________________


    # heuristic
    heuristic = heuristic_f()




    ncar = typecar()
    if ncar == 1:
        cartravel = 8
        cap = 4

    if ncar == 2:
        cartravel = 4
        cap = 2
        
    #เข้าสุ่กระบวนการเลือกเมือง
    #----------------------------------------------------------------------------------------------
    for ite in range(1,itelation +1):

        #........reset val
        ant_distance = 9999
        ant_rute = []
        inc = 0
        #...............

        for antt in range(1,ant +1):

            #reset demand
            loopindex_ant = []
            loopindex_ant.append(0)

            if ncar == 1:
                cartravel = 8
                cap = 4

            if ncar == 2:
                cartravel = 4
                cap = 2


            for i in range(1,n+1):
                loopindex_ant.append(loopindex[i]) 

            demanddummy = Check_demand(loopindex_ant) # demand [0,[1,ขนาด,จำนวน],[2,1,2]]


            for sumdem in range(1, n+1):
                sumdemand = sumdemand + demanddummy[sumdem] [2] #นำปริมาณ มา + - กัน

        
            #reset loopindex

            for z in range(1, n+1 ):

                if demanddummy[z] [2] == 0:
                    loopindex_ant[z] = 0

                elif demanddummy[z] [2] > 0 and demanddummy[z] [1] == 1: #picnic
                    loopindex_ant[z] = 1

                elif demanddummy[z] [2] > 0 and demanddummy[z] [1] == 2: #15 kg
                    loopindex_ant[z] = 2

                elif demanddummy[z] [2] > 0 and demanddummy[z] [1] == 3: #42 kg
                    loopindex_ant[z] = 3
                #end if

                if ncar == 1 and loopindex_ant[z] == 0:
                    for y in range(1, n+1):
                        heuristic[y] [z] = 0
                    # next y

                elif ncar == 2 :
                    if loopindex_ant[z] == 0 :
                        for y in range(1, n+1):
                            heuristic[y] [z] = 0
                #end if
            #next z

            #reset para
            heuristic = heuristic_f()
            rute = []
        
            #..............................................

            if sum(loopindex_ant) >=1 :
                countloop = 0

                while sumdemand != 0:
                  
                    rute.append(0)
                    #การเก็บค่า-------------
                 
                    
                    for i in range(1, cartravel + 2):
                    #while cap != 0:
                        #_______________reset heuristic if dont have demand heuristic = 0


                        for z in range(1, n+1 ):

                            if demanddummy[z] [2] == 0:
                                loopindex_ant[z] = 0

                            elif demanddummy[z] [2] > 0 and demanddummy[z] [1] == 1: #picnic
                                loopindex_ant[z] = 1

                            elif demanddummy[z] [2] > 0 and demanddummy[z] [1] == 2: #15 kg
                                loopindex_ant[z] = 2

                            elif demanddummy[z] [2] > 0 and demanddummy[z] [1] == 3: #42 kg
                                loopindex_ant[z] = 3
                            #end if

                            if ncar == 1 and loopindex_ant[z] == 0:
                                for y in range(1, n+1):
                                    heuristic[y] [z] = 0
                                # next y

                            elif ncar == 2 :
                                if loopindex_ant[z] == 0 :
                                    for y in range(1, n+1):
                                        heuristic[y] [z] = 0
                                         
                                       
                                #endif

                                if demanddummy[z] [1] == 3:
                                    for y in range(1, n+1):
                                        heuristic[y] [z] = 0
                                        demanddummy[z] [2] = 0 #ปิดดีมาน 42 โลทั้งหมด ถ้าใช้รถ มอไซต์
                                         #loopindex_ant[z] = 0
                                #end if
                            #end if
                        #next z


                        # reset value
                    
                        heuristic_power = []
                        pheromone_power = []

                        pheromone_dot_heuristic= [] #array
                        sum_pheromone_dot_heuristic = [0] #tuple 7 city
                        p_xy = []

                        u = 0
                        #....
                
                        
                        if i == 1 : #เริ่มต้น
                        #if start == 1:
                            k = 1
                            rute.append(k)
                            idx = 1
                            
                        elif cap <= 0:
                            k = destination
                            u = 999 #เมืองสุดท้าย
                            idx = i
                            rute.append(destination)
                            
                        elif i == cartravel + 1: #+2 เพราะ รอบสุดท้ายไม่วิ่ง cartravel +3 ไม่วิ่ง 
                        #elif cap == 0:
                            k = destination
                            u = 999 #เมืองสุดท้าย
                            idx = i
                            rute.append(destination)
                            start = 1
                        else:
                            k = destination #อื่น ๆ
                            idx = i
                            rute.append(k)
                        #end if
                
                        
                        if u == 999 and cap <= 0:
                            rute.append(1)
                            destination = 1

                            if ncar == 1:
                                cap = 4
                            elif ncar == 2:
                                cap = 2

                            break

                        elif u == 999:
                            rute.append(1)
                            destination = 1


                        #step ant random.......
                        else:

                            if sum(loopindex_ant) >=1 :

                                randomchoose = random.random()
                                #____ step by arc max
                                if randomchoose <= 0.5:
                                    

                                    #ผลลัพธ์ออกมาเป็น destination หรือเมืองที่เลือกเดินไป
                                  
                                    heuristic_power.append(k)
                                   
                                    pheromone_power.append(k)
                                    pheromone_dot_heuristic.append(k)

                                    for j in range(1, n + 1):
                            
                                        heuristic_power.append(heuristic[k] [j] ** beta)
                                        pheromone_power.append(pheromone[k] [j] ** alpha)
                                        pheromone_dot_heuristic.append(pheromone_power [j] * heuristic_power [j]) 
                                   #print(pheromone_dot_heuristic) 

                                    dummy = -999

                                    for a in range(1,n+1):
                                        if pheromone_dot_heuristic [a]  > dummy :
                                            dummy = pheromone_dot_heuristic [a]
                                            destination = a
                                 

                                    x = 5 #ในวงเล็ป
                                    #____ end step arcmax


                                else: #____step by prob

                                    #_____heuristic ^ alpha_________Pheromone ^ beta_________pheromone_power * heuristic_power
                                    heuristic_power.append(k)
                                    pheromone_power.append(k)
                                    pheromone_dot_heuristic.append(k)
    
                                    for j in range(1, n + 1):
                            
                                        heuristic_power.append(heuristic[k] [j] ** beta)
                                        pheromone_power.append(pheromone[k] [j] ** alpha)
                                        pheromone_dot_heuristic.append(pheromone_power [j] * heuristic_power [j]) 
                            
                                    #next i
                                    #...............



                                    #___sum (pheromone_power * heuristic_power)____________
                        
                                    sumdummy = 0
                                    for i in range(1, n + 1):
                                        sumdummy = sumdummy + pheromone_dot_heuristic [i]
                                    #next i
                                    sum_pheromone_dot_heuristic = sumdummy
                        
                                    #................


                                    p = random.random()
                        
                                    #______________P_xy_____and step______________
                        

                                    p_xy.append(k)
                                    for i in range(1, n + 1):
                                        if sum_pheromone_dot_heuristic == 0:
                                            break

                                        else:

                                            p_xy.append(pheromone_dot_heuristic[i]  / sum_pheromone_dot_heuristic) #p_xy = [1, 0.0, 0.4831, 0.0924, 0.0447, 0.0281, 0.2922, 0.0591]
                                            dummy = sum(p_xy) - k

                                            if p_xy[i] != 0 and p <= dummy:
                                                destination = i
                                                break # break loop        
                                        #endif
                                    #next i
                                #____end step by prob



                                #manage demand____________
                                if demanddummy[destination] [1] == 1:
                                    demanddummy[destination] [2] = demanddummy[destination] [2] - 0.5
                                    cap = cap - 0.5
                                elif demanddummy[destination] [1] == 2:
                                    demanddummy[destination] [2] = demanddummy[destination] [2] - 1
                                    cap = cap - 1
                                elif demanddummy[destination] [1] == 3:
                                     demanddummy[destination] [2] = demanddummy[destination] [2] - 2
                                     cap = cap - 2
                                #end if

                                if cap <= 0:
                                    cap =0

                                if demanddummy[destination] [2] == 0:
                                    loopindex_ant[destination] = 0 #ถ้า loopindex[i] = 0 ทุกเส้นทางที่ไปเมือง i pheromone = 0

                                #end if

                            
                       
                        
                            elif sum(loopindex_ant) <= 0: #come back shop if demand = 0
                                destination = 1
                                idxx = 1 
                                #rute.append(1)
                                #cap = 0
                                
                            #end if choose city
                        
                        #end if choose by step ant




                        #update local pheromone
                        pheromone[k] [destination] = ((1-evaporation)* pheromone[k] [destination] ) + ( evaporation*0.1 )
                        #pheromone[destination] [k] = ((1-evaporation)* pheromone[destination] [k]  ) + ( evaporation*0.1 )
                        #.................
                    
                   
                                   
                    #end cartravel nnnnn while lopp step          
                    sumdemand = 0                                   
                    for sumdem in range(1, n+1):
                       sumdemand = sumdemand + demanddummy[sumdem] [2] #นำปริมาณ มา + - กัน
                     
                #loop
                rute_all.append(rute)

            
                compare = CompareDistance(rute)

                if ant_distance >= compare:
                    ant_distance = compare
                    ant_rute = rute
                    inc = antt
                #end if          
            #endif sumdemand and sum loopindex
        

        
        #next antt___

        print("ite = {0}".format(ite))
        print("distance      = {0} rute      = {1} ".format(ant_distance,ant_rute))

        #update Global Pheromone
            # use k global & destination global

        num = len(ant_rute) - 1

        #__________อัพเดตทุกครั้งที่มดเดิน_______________
        for glo in range (1,num +1):
            if ant_rute[glo-1] == 0:
                k_global = 1
            elif glo >= 2 and ant_rute [glo] != 0:

                if ant_distance == 0:
                    break

                else:

                    destination_global = ant_rute[glo]
                    pheromone [k_global] [destination_global] = ((1-evaporation) * pheromone [k_global] [destination_global]) + (evaporation * (1/ant_distance))
                    #pheromone [destination_global] [k_global] = ((1-evaporation) * pheromone [destination_global] [k_global]) + (evaporation * (1/ant_distance))

                    k_global = ant_rute [glo]
            #end if
        #next glo
        #....question for what: ช่วงที่ มดเดินกลับร้าน จำเป็นต้องอัพเดต pheromone ไหม และการอัพเดต rute [1,5,4,1] ควรอัพเดตทั้ง 1 ไป 5 และ 5 ไป 1 ไหม หรืออัพแค่ 1 ไป 5 พอ


        #__________อัพเดตเดตเฉพาะถ้าค่าดีขึ้น_______________
        if best_distance > ant_distance:
            best_distance = ant_distance
            best_rute = ant_rute
            d = 0

        # for i in range (1,num +1):
        #     if ant_rute[i-1] == 0:
        #         k_global = 1
        #     elif i>= 2 and rute [i] != 0:
        #         destination_global = ant_rute[i]

        #         pheromone [k_global] [destination_global] = ((1-evaporation) * pheromone [k_global] [destination_global]) + (evaporation * (1/ant_distance))
        #         #pheromone [destination_global] [k_global] = ((1-evaporation) * pheromone [destination_global] [k_global]) + (evaporation * (1/ant_distance))

        #         k_global = ant_rute [i]

        #_....question for what: ช่วงที่ มดเดินกลับร้าน จำเป็นต้องอัพเดต pheromone ไหม และการอัพเดต rute [1,5,4,1] ควรอัพเดตทั้ง 1 ไป 5 และ 5 ไป 1 ไหม หรืออัพแค่ 1 ไป 5 พอ
        #end if

        print("best distance = {0} best rute = {1} ".format(best_distance,best_rute))
        print("________________________________________________________________________")
    
        #ถ้าค่าไม่เปลี่ยน reset pheromone
        d = d + 1
        if d == 10:
            d = 0
            pheromone = [[]]

            for b in range(1 ,n + 1):
                pheromone.append([b])
                for a in range(1, n + 1):

                    pheromone[b].append(0.1) # [[], [1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], 
                                                #      [2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], 
                                                   #  #   [3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], 
                                                   #  #   [4, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], 
                                                   #      [5, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], 
                                                   #      [6, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], 
                                                   #      [7, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]]
        #___________________

    
        

    #next ite
    return best_rute,best_distance
#end def
#_____________________________________________________________________


def Arrival(rute):
    import ProbLocate
    


    #change to my code
    pre = rute #[0, 1, 3, 5, 1, 0 , 1, 4, 1]

    


    num = len(pre) -1
    arrival = []
    timeA = 0
    countloop = 1

    transittime = ProbLocate.TranTime()

    for i in range (1,num + 1):
        if pre[i-1] == 0:
            k = 1
            arrival.append(countloop)
            arrival.append(0)

        elif i >= 2 and pre [i] != 0:
            destination = pre[i]
            timeA = transittime [k] [destination] + timeA
            arrival.append(timeA)

            k = pre[i]

        elif i >= 2 and pre[i] == 0:
            timeA = 0

            #idxx = 1
            countloop = countloop + 1
        # end if
    #next i

    #เก็บค่า pre ให้เป็นรูปดีดี ไว้แสดงผล
    return arrival

def FinalDistance(rute):
    import ProbLocate
    


   
    pre = rute #[0, 1, 3, 5, 1, 0 , 1, 4, 1]

    


    num = len(pre) -1
    final_distance = 0
    
    

    city = ProbLocate.LocCity()

    for i in range (1,num + 1):
        if pre[i-1] == 0:
            k = 1
            

        elif i >= 2 and pre [i] != 0:
            destination = pre[i]
            final_distance = city [k] [destination] + final_distance
            

            k = pre[i]

        
           

            #idxx = 1
            
        # end if
    #next i

    #เก็บค่า pre ให้เป็นรูปดีดี ไว้แสดงผล
    return final_distance

def ChoosenCar(x):


    import ProbLocate
    city = ProbLocate.LocCity()
    
    rute = x
    ncar = typecar()
    dummy_rute = [0]

    dist = 0
    car_using = 0
    countloop = 1

    if ncar == 1:
        numcar = numbercar() [1] 
    elif ncar == 2:
        numcar = numbercar() [2]


    

    numrute = rute.count(0) # นับจำนวนเส้นทางที่เกิดขึ้นในช่วงเวลานั้น

    if numcar >= numrute: #มีรถมากกว่าเส้นทางที่เกิดขึ้นได้  
        new_rute = rute
        car_using = numrute

    elif numcar < numrute: #ถ้ารถน้อยกว่าต้องตัดสินใจเลือกเส้นทางที่สั้นที่สุด ตามจำนวนรถที่เหลืออยู่
        
        num = len(rute) - 1
        pre = [0]
        for i in range(1,num + 1):
            pre.append(rute[i])
        #next i

        pre.append(0)
        num = len(pre) - 1
        #maintaince
        for i in range (1,num + 1):
            if pre[i-1] == 0:
                k = 1
                dummy_rute.append([0])
                dummy_rute[countloop].append(pre[i])

            elif i >= 2 and pre [i] != 0:
                destination = pre[i]

                dist = dist + city[k] [destination]

                k = pre[i]

                dummy_rute[countloop].append(pre[i])

            elif i >= 2 and pre[i] == 0:
                dummy_rute[countloop][0] = dist
                dist = 0
                
                countloop = countloop + 1
            # end if
        #next i

        
        idx = 0
        boolean = [0]
        new_rute = []

        for i in range(1, numrute + 1):
            boolean.append(0)
        #nexst i
        
        for i in range(1, numcar+1):
            dummy = 99999

            for j in range(1, numrute + 1):
                if dummy_rute[j] [0] < dummy and boolean [j] != 1:
                    dummy = dummy_rute[j] [0]
                    idx = j
                #end if
            #next j

            boolean[idx] = 1
            new_rute.append(0)
            ll = len(dummy_rute [idx]) -1

            for s in range(1, ll + 1 ):
                new_rute.append(dummy_rute[idx] [s])
            #next s
            
        #next i
        car_using = numcar
    #endif

    return new_rute, car_using

#import AntVersionKim
import ProbLocate
import ProbOrder

#import Resource
city = ProbLocate.LocCity()

#ordertime = ProbOrder.Time()

ordertime = ProbOrder.Time()
demand = ProbOrder.Dem()

n = len(city[1]) - 1  
 

tmustgo = [[]] #10 time (11)

  
countloop = 0
sumtime = 0
arrivaldummy = [0,0,0,0,0,0,0,0] #เอาไว้เก็บว่า อีกกี่นาทีรถจะไปถึงเมืองนั้น ๆ ในลำดับที่ 2 - กลับเมืองที่ออก และนำค่าไปเก็บอีกทีใน arrival
n_index_0 = 0 

#typecar = [0,1,2]
quantity_car = [0,3,1]
#numcar = len(typecar) - 
TimeSentBack_car = [0]
TypeSentBack_car = [0]

all_rute = [[]]
all_distance = 0
all_arrival = [[]]
set_distance = [[]]

t = 0
index_0 = [0] 

while t !=  600: #ทำไปเรื่อย ๆ ถ้า เวลายังไม่ถึงเวลาปิดร้าน
    

    loopindex = Check(ordertime, demand, t, n)
    
    #sent back
    n_index_0 = len(index_0) - 1
     
    
    if len(TypeSentBack_car) > 1:
        index_delete = 0

        for j in range(1, len(TypeSentBack_car) -1 + 1):                        
            if t >= TimeSentBack_car[j]:

                if TypeSentBack_car[j] == 1:
                    quantity_car[1] = quantity_car[1] + 1

                    TypeSentBack_car [j] = "del"
                    TimeSentBack_car [j] = "del"

                elif TypeSentBack_car[j] == 2:
                    quantity_car[2] = quantity_car[2] + 1

                    TypeSentBack_car [j] = "del"
                    TimeSentBack_car[j] = "del"
                #
            #
        #
        #delete
        index_delete = TypeSentBack_car.count("del")
                                             
        for i in range(1, index_delete + 1):
            TypeSentBack_car.remove("del")
            TimeSentBack_car.remove("del")
    #_________end sent back car

    #ncar = Resource.NumCar()

    #tdummy and tnow

    #for i in range (1,numcar + 1):

    if quantity_car[1] > 0:
        ncar = 1
        index_car = 1
    elif quantity_car[1] == 0 and  quantity_car[2] != 0:
        ncar = 2
        index_car = 2
    else:
        ncar = 0
        index_car = 0

    
    if sum(loopindex) > 0 and sum(quantity_car) > 0:
        
        index_0 = [0]
       
        ##Ant
        
        output = AntColony(loopindex) 
        rute = output [0]
        #loopdistance = output [1]

        #_______choose rute    
        output_carchoosing = ChoosenCar(rute)
        rute = output_carchoosing [0]  
        car_using = output_carchoosing [1]  

        #_______decrease demand
        n_rute = len(rute) - 1
        for i in range(1, n_rute +1):
        
            if rute[i-1] == 0:
                k_dem = 1
            elif i >= 2 and rute [i] != 0 and rute[i] != 1 :
                destination_dem = rute[i]

                if demand [destination_dem] [1] == 1 :
                    demand [destination_dem] [2] = demand [destination_dem] [2] - 0.5 #เมืองไหนที่เดินไป demand จะ = 0
                elif demand [destination_dem] [1] == 2 :
                    demand [destination_dem] [2] = demand [destination_dem] [2] - 1
                elif demand [destination_dem] [1] == 3 :
                    demand [destination_dem] [2] = demand [destination_dem] [2] - 2

                k = rute[i]

            elif rute[i] == 0:
                index_0.append(i)

        quantity_car[index_car] = quantity_car[index_car] - car_using
        #......


        #arrival time
        arrival = Arrival(rute)

        #distance
        loopdistance = FinalDistance(rute)
        #print("This rute distance = {0} This rute = {1} ".format(loopdistance ,rute))


        #time that sent back car
        n_index_0 = len(index_0) - 1
        if n_index_0 <= 0 :
            
            TypeSentBack_car.append(ncar) #ncar 1 = พ่วง ncar 2 = ธรรมดา
            TimeSentBack_car.append(arrival[n_rute] + t)
            #new
            index_0.append(0)
            
        elif n_index_0 >= 1 :
            for j in range(1, n_index_0 + 2): #+2 เพราะ n_index_0 ไม่นับรอบแรก และ + ตามหลัก for python

                TypeSentBack_car.append(ncar)
                if j != n_index_0 + 1:
                    TimeSentBack_car.append(arrival[index_0 [j] - 1 ] + t)
                elif j == n_index_0 + 1:
                    TimeSentBack_car.append(arrival[n_rute] + t)
                #end if
            #next j
        #end if  
        print("This rute________________________ = {0} ".format(rute))
        print("time using_______________________ = {0}".format(arrival))
        
   
        #####################################################################################################################################################################

        loopindex = Check(ordertime, demand, t, n)
        #new
        before_n_index_0 = 0

        #กรณีที่ ใช้รถจนหมดแต่ เส้นทางยังเหลือ ใช้รถสำรองคือ มอเตอร์ไซต์
        if sum(loopindex) > 0 and sum(quantity_car) > 0:
            
            before_n_index_0 = len(index_0) -1

            if quantity_car[1] > 0:
                ncar = 1
                index_car = 1
                
            elif quantity_car[1] == 0 and  quantity_car[2] != 0:
                ncar = 2
                index_car = 2
            else:
                ncar = 0
                index_car = 0
            #end if

            ##Ant
            print("____________________car type 2 teavel_________________")
            output_2 = AntColony(loopindex) 
           
            rute_2 = output_2 [0]
            #loopdistance_2 = output [1]


            #_______choose rute    
            output_carchoosing_2 = ChoosenCar(rute_2)
            rute_2 = output_carchoosing_2 [0]  
            car_using_2 = output_carchoosing_2 [1]  

            #_______decrease demand
            n_rute_2 = len(rute_2) - 1
            for i in range(1, n_rute_2 +1):
        
                if rute_2[i-1] == 0:
                    k_dem = 1
                elif i >= 2 and rute_2 [i] != 0 and rute_2[i] != 1 :
                    destination_dem = rute_2[i]

                    if demand [destination_dem] [1] == 1 :
                        demand [destination_dem] [2] = demand [destination_dem] [2] -0.5 #เมืองไหนที่เดินไป demand จะ = 0
                    elif demand [destination_dem] [1] == 2 :
                         demand [destination_dem] [2] = demand [destination_dem] [2] - 1
                    elif demand [destination_dem] [1] == 3 :
                         demand [destination_dem] [2] = demand [destination_dem] [2] - 2

                    k = rute_2[i]
                elif rute_2[i] == 0:
                    index_0.append(i)
                    


            quantity_car[index_car] = quantity_car[index_car] - car_using_2

            
            #......

            

            #arrival time
            arrival_2 = Arrival(rute_2)

            #time that sent back car
            n_index_0_2 = len(index_0) - 1 - before_n_index_0

            if n_index_0_2 <= 0 :
            
                TypeSentBack_car.append(ncar) #ncar 1 = พ่วง ncar 2 = ธรรมดา
                TimeSentBack_car.append(arrival_2[n_rute_2] + t)
                #new
                index_0.append(0)
                
            elif n_index_0_2 >= 1 :
                for j in range(1, n_index_0_2 + 2 ): #+2 เพราะ n_index_0 ไม่นับรอบแรก และ + ตามหลัก for python

                    TypeSentBack_car.append(ncar)
                    if j != n_index_0_2 + 1:
                        TimeSentBack_car.append(arrival_2[index_0_2 [j] - 1] + t)
                    elif j == n_index_0_2 + 1:
                        TimeSentBack_car.append(arrival_2[n_rute_2] + t)
                    #end if
                #next j
            #end if  

            # ค่อรูทให้เป็นเส้นเดียวกัน

            rute.append(0)
            for i in range(1,n_rute_2 + 1):
                rute.append(rute_2 [i])

            #distance
            loopdistance = FinalDistance(rute)

            #arrival time
            arrival = Arrival(rute)

            print("This rute________________________ = {0} ".format(rute_2))
            print("time using_______________________ = {0}".format(arrival_2))
            #####################################################################################################################################################################















        #_Arrival
        
        all_rute.append(rute)
        all_distance = all_distance + loopdistance
        all_arrival.append(arrival)
        set_distance.append(loopdistance)

        print("This rute distance = {0} This rute = {1} ".format(loopdistance ,rute))
        print("time using_______________________ = {0}".format(arrival))

        x = arrival.count(0) #len(arrival) - 1 
        tmustgo.append([t,x])
        
        for i in range(1,n+1):
            if demand[i] [2] < 0:
                demand[i] [2] = 0

        #quantity_car[index_car] = quantity_car[index_car] - car_using
    #end if
        
    #quantity_car[index_car] = quantity_car[index_car] - 1



    
    






    
    t = t + 30
    print("time = {0}".format(t))

print(all_rute)

print(all_arrival)

print(set_distance)

print(all_distance)

print(tmustgo)