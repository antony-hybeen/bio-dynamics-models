relapse mode
A non linear systems simulations based on the relation between
::dopamine
::stress
::control 
::cue
This system provides a hypothetical method of studying relations on how circadian variation and stochastic stress inputs give rise to relapse like episodes.

The system is based on coupled differential equation solved using forward euler integration.
x(t + dt) = x(t) + dt * f(x(t))
with a timestep of dt = 0.01 hours.

-sample output
::no of relapse
::time of relapse
::graph plotting the relation between dopamine,stress,control and cue

Possible improvements:
::switch from euler to rk4
::system plotting based on real life data inputs from a user(the hypothetical relative grade so assigned can be perfected over days of input)
::multiday analysis
::stability analysis
