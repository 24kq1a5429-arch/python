distance=int(input("Enter distance:"))
speeds=list(map(int,input("Enter speeds of 3 horses:").split()))
max_speed=max(speeds)
min_time=distance/max_speed
print("minimum time required",min_time)
