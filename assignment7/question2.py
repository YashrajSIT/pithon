
distance=[10,20,30,40,50]
time=[1,5,3,2,4]
#clculating the speed by the help of formula speed=distance/time.
speed=[distance[i]/time[i] for i in range(min(len(distance),len(time)))]
print("distance= ",distance)
print("time= ",time)
print("speed is =", speed)