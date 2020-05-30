def weight_computing():
    cw=eval(input("Please enter your current weight: "))
    i=1
    while(i<=10):
        mw=cw*(16.5/100)
        print("Weight on the moon in",i,"'th Year",mw)
        cw=cw+0.5
        i=i+1
weight_computing()
    
