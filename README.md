Bio dynamics models
computational modelling and graph plotting of biological systems using ordinary differencial equations(ODE)
currently this repository contains models that simulate hypothetical situations in
      :::>addiction-relapse dynamics
      :::>cancer-treatment under radiotherapy and chemotherapy dynamics

Cancer-treatment model(coloncan.py)
A Gompertz growth model for cancer therapy by radio and chemo treatment
In this model four kind of scenarios are imitated hypothetically
::>untreated exponential tumour growth
::>tumour growth under long-term radio-therapy
::>tumour growth under short-term radio-therapy
::>tumour growth  under chemotherapy

the growth model is based on gompertz equation
                 dT/dt=rTln(K/T)
                 where T=tumour cell(normalised)
                       r= intrinsic growth rate(0.008 #tumour doubling taken to be at aroud 86 days((https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2020.533101/full)))
                       K=carrying capacity(in the model normalized to 1)

Radiotherapy modelling:
Its based on radiation cell kills following linear-quadratic model
                  S=e^−(αD+βD^2)
where: S=survived cells(normalized)
       𝛼,𝛽=radiosensitivity parameters
       D=dose
the model works on:
within radiation days the model follows 
                  Tnew=Told*S
       during normal days
                  gompertz growth
short-term radiation--the radiation therapy was set to be given in fewer higher dose fractions(#5 day higher dose fraction)
long_term radiation--the radiation therapy was set to be given in multiple fractions per week over several weeks.(#5 day in a week for over 5 weeks smaller dose fraction)

Chemotherapy model:
this is based on drug concentration dynamics governed by
                   dC/dt=−δC
                   C = drug concentration
                   δ = clearance rate
                   weekly dose is applied (+=0.2)
Tumour kill term: dT/dt=dT/dt=rTln(K/T)−δCT
Numerical Method

All systems are solved using forward Euler integration:
                   x[i+1]=x[i]+(dx/dt)*dt

Output:
The scripts generate comparative plots between
                 --Untreated tumor growth
                 --Long-course radiotherapy
                 --Short-course radiotherapy
                 --Chemotherapy-treated growth

Giving visualization of:
                --Fractionation effects
                --Treatment timing impact
                --Regrowth dynamics
                --Drug decay influence

This model is completely hypothetical and based on assumptions such as:
                --Tumor is homogeneous
                --Instant radiation effect
                --No resistance evolution
                --No immune system interaction
                --chemotherapy kill term is linear which is rare
                --treatment is either chemo or radio

DISCLAIMER:
This is an extremely simplified model just for conceptual exploration.

Possible improvements:
                --Tumour heterogeneity (sensitive and resistant cells)
                --Drug resistance evolution
                --RK4 integration
                --realistic data gathering








Addiction-Relapse model(relapse.py)::
Overview
This project simulates the interaction between:
               --Dopamine levels
               --Stress
               --self control
               --Environmental cue exposure
this model uses a system of coupled differential equations solved numerically using Euler’s method
The simulation incorporates:
               --Circadian variation in stress and cue exposure
               --fluctuations in daily stress
               --Dopamine decay
               --Effects of exercise and entertainment
               --Social support factors(Like AA/NA meets)
               --relapse threshold mechanism showing time and number of relapses.

In this system
Dopamine dynamics
Influenced by:
               --Exercise (positive)
               --Entertainment (positive)
               --Stress (negative)
               --Cue exposure (negative)
               --Natural decay
Stress dynamics
Influenced by:
              --Baseline stress (time-dependent + randomised)
              --Dopamine (stress reduction)
              --Natural decay
Control dynamics
Influenced by:
              --Social support factors
              --Stress (negative)
              --Natural decay
Cue dynamics
Influenced by:
              --Stress
              --Dopamine (reduces cue sensitivity)
              --Control (reduces cue impact)


Relapse Mechanism
Relapsed is defined as:
              --R=stress−control−dopamine

Two thresholds are used:
r_max → relapse trigger
r_low → recovery/reset

When relapse occurs:
              --Dopamine decreases
              --Control decreases
              --Stress increases


Stochastic Component
The model introduces randomness using Gaussian noise for:
            --Baseline stress
            --Cue exposure
This is also based on eulers forward integration 
with dt=0.01 hr

Output:
The simulation generates time-series plots of:
Dopamine,stress,control and cue

Assumptions
           --Variables are abstract and normalized
           --Parameters are hypothetical and not fitted to empirical data
           --highly simplified neuroscience
           --Does not represent medical data
DISCLAIMER:
Heavily simplied. made just for conceptual exploration.

Possible improvements:
           --data taken from real life inputs from users and/or from wearable tracker data based on stress can be found and the variables can be adjusted based on that for a more realistic system.
           --Use RK4 for better accuracy
           --multi-day simulation(#have given no of days =1 for simplification)
 




	​




    


