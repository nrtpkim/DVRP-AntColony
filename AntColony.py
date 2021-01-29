#### start index 1 all of list
#### index 0 just dummy
def demand_f():
    import ProbOrder #demand
    #demand = ProbOrder.Dem()
    # demand = CheckOrder.Check_demand()
    demand = ProbOrder.Dem()
    demand_cap = [0]
    for idx in range(1,len(demand)):
        demand_cap.append(demand[idx][2])

    print(demand_cap)
    return demand_cap


def heuristic_f():
    import ProbLocate #distance
    city = ProbLocate.LocCity() #distanct

    n = len(city)-1

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

#f_comparedistance
def CompareDistance(rute):
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
#...............

def AntColony_main():
    import random
    import ProbLocate #distance
    

    #setting import______________________________
    city = ProbLocate.LocCity() #distanct
    demanddummy = demand_f()

    loopindex = [0,0,0,0,0,0,0,0,0,0,0,0] #เปิดเดินทุกเมือง
    #___________________________________________


    #variable___________________________________
    n = len(city[1]) - 1 #number of city

    rute = []
    rute_all = [[]]

    d = 0
    u = 0
    k = 1
    destination = 1

    itelation = 5
    ant = 10

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
            demanddummy = demand_f()
            sumdemand = sum(demanddummy)

        
            #reset loopindex

            for z in range(1, n+1 ):
                if demanddummy[z] == 0:
                    loopindex[z] = 0
                elif demanddummy[z] > 0:
                    loopindex[z] = 1
                #end if
            #next z

            #reset para
            heuristic = heuristic_f()
            rute = []
        
            #..............................................

            if sumdemand >= 1 and sum(loopindex) >=1 :
                countloop = 0

                while sumdemand != 0:
                    countloop = countloop + 1
                    rute.append(0)

                    cartravel = 4
                    #การเก็บค่า-------------
                 
            
                    for i in range(1, cartravel + 2):

                        #_______________reset heuristic if dont have demand heuristic = 0
                        for z in range(1, n+1 ):
                            if demanddummy[z] == 0:
                                loopindex[z] = 0
                            elif demanddummy[z] > 0:
                                loopindex[z] = 1
                            #end if

                            if loopindex[z] == 0:

                                for y in range(1, n+1):
                                    heuristic[y] [z] = 0

                        # reset value
                    
                        heuristic_power = []
                        pheromone_power = []

                        pheromone_dot_heuristic= [] #array
                        sum_pheromone_dot_heuristic = [0] #tuple 7 city
                        p_xy = []

                        u = 0
                        #....
                

                        if i == 1 : #เริ่มต้น
                            k = 1
                            rute.append(k)
                            idx = 1
                        elif i == cartravel + 1: #+2 เพราะ รอบสุดท้ายไม่วิ่ง cartravel +3 ไม่วิ่ง 
                            k = destination
                            u = 999 #เมืองสุดท้าย
                            idx = i
                            rute.append(destination)
                        else:
                            k = destination #อื่น ๆ
                            idx = i
                            rute.append(k)
                        #end if
                
                        #step ant random.......

                        if u == 999:
                            rute.append(1)
                            destination = 1

                        else:

                            if sum(loopindex) >=1 :
                        

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
             
                                    p_xy.append(pheromone_dot_heuristic[i]  / sum_pheromone_dot_heuristic) #p_xy = [1, 0.0, 0.4831, 0.0924, 0.0447, 0.0281, 0.2922, 0.0591]
                                    dummy = sum(p_xy) - k

                                    if p_xy[i] != 0 and p <= dummy:
                                        destination = i
                                        break # break loop        
                                    #endif
                                #next i
                        

                                #manage demand____________
                                demanddummy[destination] = demanddummy[destination] - 1
                                if demanddummy[destination] == 0:
                                    loopindex[destination] = 0 #ถ้า loopindex[i] = 0 ทุกเส้นทางที่ไปเมือง i pheromone = 0
                            

                            
                       
                        
                            elif sum(loopindex) <= 0: #come back shop if demand = 0
                                destination = 1
                                idxx =1 
                            #end if choose by step ant
                        #end if choose city

                        #update local pheromone
                        pheromone[k] [destination] = ((1-evaporation)* pheromone[k] [destination] ) + ( evaporation*0.1 )
                        #pheromone[destination] [k] = ((1-evaporation)* pheromone[destination] [k]  ) + ( evaporation*0.1 )
                        #.................
                    
                    #end cartravel
                       
                    sumdemand = sum(demanddummy) 
                
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
#end def


AntColony_main()

