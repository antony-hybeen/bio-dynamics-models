import numpy as np
import matplotlib.pyplot as plot
number_days=1 #can be varied
T=24*number_days
dt=0.01#in hr
time= np.arange(0,T,dt)
#effects on addiction.
effect_exercise=0.5 
effect_stress=0.4
effect_rest_entertainement=0.3#movies,music etc sudden little spike of dopamine rather than prolonged.
effect_cue=0.7#rapid spike
dop=np.zeros(len(time)) #dopamine
stress=np.zeros(len(time))
cont=np.zeros(len(time))#control
cue=np.zeros(len(time))
#effect if each on one another
x=0.2#factor involving dopamine and stress (dopamine reduces stress)
y=0.5#positive factor affecting control and cue reduction(aa meets etc)
z=0.6#negative influence of stress on control
j=0.3#stress and cue
u=0.5#dopamine cue realtion
cc=0.3#cue control relation
#initially at 0.00 hr
dop[0]=1.0
cont[0]=1.0
stress[0]=0.01
cue[0]=0.01
relapse_count = 0
in_relapse = False
r_max = 0.7
r_low = 0.4

for i in range(len(time)-1):#stress level variation wrt hour of the day.
    if 0<=time[i]<=10:
        base_stress=0.05
        possible_cue=0.03
        exercise=0.1
        entertainement=0.1
    elif 11<=time[i]<=15:
        base_stress=0.7
        possible_cue=0.3
        exercise=0.2
        entertainement=0.1
    elif 16<=time[i]<=21:
        base_stress=0.5
        possible_cue=0.8
        exercise=0.5
        entertainement=0.4
    else:
        base_stress=0.2
        possible_cue=0.4
        exercise=0.3
        entertainement=0.6
    #randomizing base stress and possible cue
    delta=np.random.normal(base_stress,0.02)
    sigma=np.random.normal(possible_cue,0.04)
    d=0.1#dopamine decay
    s=0.3#stress decay
    c=0.3#control decay
    aa=0.5#social factors nfluencing control
    cd=0.5#cue decay
    #equation
    ddopdt=exercise*effect_exercise - effect_stress*stress[i]+effect_rest_entertainement*entertainement-effect_cue*cue[i]-d*dop[i]
    dstressdt=delta-x*dop[i]-s*stress[i]
    dcontdt=y*aa-z*stress[i]-c*cont[i]
    dcuedt=j*stress[i]-u*dop[i]-cd*cue[i]+sigma-cc*cont[i]


    #eulers
    dop[i+1]=dop[i]+dt*ddopdt
    stress[i+1]=stress[i]+dt*dstressdt
    cont[i+1]=cont[i]+dt*dcontdt
    cue[i+1]=cue[i]+dt*dcuedt
    
    dop[i+1]=max(dop[i+1],0)
    stress[i+1]=max(stress[i+1],0)
    cont[i+1]=max(cont[i+1],0)
    cue[i+1]=max(cue[i+1],0)
    R=stress[i+1]-cont[i+1]-dop[i+1]
    R = stress[i+1] - cont[i+1] - dop[i+1]
    #Relapse time and count
    if not in_relapse and R > r_max:
     relapse_count += 1
     in_relapse = True
     print("relapse at time:",time[i])
     print("relapse count",relapse_count)
     dop[i+1] -= 0.6
     cont[i+1] -= 0.4
     stress[i+1] += 0.4

    elif in_relapse and R < r_low:
     in_relapse = False


#graph
plot.figure(figsize=(10,6))
plot.title("hypothetical graph plotting of relapse mech and effects of stress dopamine etc on each other") 
plot.xlabel("Time (hours)") 
plot.ylabel("State Value") 
plot.plot(time,dop,label="Dopamine") 
plot.plot(time,stress,label="Stress") 
plot.plot(time,cont,label="Control") 
plot.plot(time,cue,label="cue") 
plot.legend() 
plot.show()



  










        


