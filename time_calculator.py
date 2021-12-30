def add_time(start, duration,day=None):

    starttime=start.split(" ") 
    starthr=starttime[0].split(":")[0]
    startmin=starttime[0].split(":")[1]
    startmode=start.split(" ")[1]

    durationhr=duration.split(":")[0]
    durationmin=duration.split(":")[1]
        
    newhr=int(starthr)+int(durationhr)
    newmin=int(startmin)+int(durationmin)
    if newmin>=60:
        newhr += 1
        newmin -= 60
    if newmin<10:
        newmin='0'+str(newmin)

    modeslater=0
    dayslater=0
    initialmode=startmode
    newhrmode=newhr   
    while newhr>12:        
        newhr-=12

    while newhrmode>=12:
        newhrmode-=12
        if startmode=="AM":
            startmode="PM"
        else:
            startmode="AM"
        modeslater+=1   

    if modeslater%2!=0:
        if initialmode == "PM":
            modeslater += 1
        else:
            modeslater -= 1      

    newtime=f"{newhr}:{newmin} {startmode}"

    days=[
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    dayslater=modeslater/2
    
    if day:
        dayindex=days.index(day.title())
        newdayindex=int((dayindex+dayslater)%7)
        newday=days[newdayindex]
        newtime += f", {newday}"

    if dayslater==1:
        newtime+=" (next day)"

    if dayslater>1:
        newtime+=f" ({int(dayslater)} days later)"

    return newtime
    
    



    



    