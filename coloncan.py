import numpy as np
import matplotlib.pyplot as plot
import math as m
no_months=9#number of months
T=no_months*30#averaged
dt=1
time=np.arange(0,T,dt)
tumour=np.zeros(len(time))
radiotherapy_growth_short=np.zeros(len(time))
radiotherapy_growth_long=np.zeros(len(time))
#variable def
#gompertz equation==dC/dt=rCln[k/C]
k=1#normalized
r=0.008
tumour[0]=k*0.01#1 percent of the max value
radiotherapy_growth_short[0]=k*0.01
radiotherapy_growth_long[0]=k*0.01
radiotherapy_long=False
radiotherapy_short=False
for i in range(len(time)-1):
    dtumourdt=r*tumour[i]*m.log(k/tumour[i])
    tumour[i+1]=tumour[i]+dtumourdt*dt
    day=int(time[i])
    if 1<=day<=35 and day%7<=4:
        radiotherapy_long=True
        a=0.2#linear
        b=0.02#quadratic
        D=2#dose
        survived_long=m.e**(-(a*D + b*D**2))
    else:
        survived_long=1
    
    dradiotherpay_growth_longdt= r*radiotherapy_growth_long[i]*m.log(k/radiotherapy_growth_long[i]) 
    radiotherapy_growth_long[i+1]=(radiotherapy_growth_long[i]+dradiotherpay_growth_longdt*dt)*survived_long
    if 1<=day<=5:
        radiotherapy_short=True
        a=0.2
        b=0.02
        D=5#dose
        survived_short=m.e**(-(a*D + b*D**2))
    else:
        survived_short=1
    dradiotherpay_growth_shortdt=r*radiotherapy_growth_short[i]*m.log(k/radiotherapy_growth_short[i]) 
    radiotherapy_growth_short[i+1]=(radiotherapy_growth_short[i]+dradiotherpay_growth_shortdt*dt)*survived_short
plot.plot(time, tumour, label="Untreated")
plot.plot(time, radiotherapy_growth_long, label="Long-course RT")
plot.plot(time, radiotherapy_growth_short, label="Short-course RT")
plot.legend()
plot.show()   

#chemograph
#effect measured proportaional(alpha*Conc*Tumour)
alpha=0.05
chemo_growth=np.zeros(len(time))
chemo_growth[0]=k*0.01
concentration=np.zeros(len(time))
concentration[0]=1
delta=0.3#half life taken to be 3 days
for i in range(len(time)-1):

    dtumourdt=r*tumour[i]*m.log(k/tumour[i])
    tumour[i+1]=tumour[i]+dtumourdt*dt
    day=int(time[i])
    if day % 7 == 0:
       concentration[i] += 0.5

  
    dCdt=-delta*concentration[i]
    concentration[i+1]=concentration[i]+dCdt*dt
    dchemo_growthdt=r*chemo_growth[i]*m.log(k/chemo_growth[i])-alpha*chemo_growth[i]*concentration[i]
    chemo_growth[i+1]=chemo_growth[i]+dchemo_growthdt*dt
    chemo_growth[i+1] = max(chemo_growth[i+1], 1e-5)

plot.plot(time, tumour, label="Untreated")
plot.plot(time, chemo_growth, label="growth during chemotherapy")
plot.legend()
plot.show()     
#chemo+radio







        



       
    



        



       
    

