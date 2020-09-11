#!/usr/bin/env python
# coding: utf-8

# # Example 2.1: Liquid Discharge through a Hole in a Tank\n",
#     Calculate the discharge rate of a liquid through a 10-mm hole, if the tank head space is pressurized to 0.1 barg. Assume,
#     a 2-m liquid head above the hole.
#     

# ## Input data

# In[1]:


Tank_Pressure=0.1 #barg
Pressure_Outside_hole=0 #barg
Liquid_density=490 #kg/m3
Liquid_level_above_hole=2#mm
Hole_Diameter=10 #mm


# ## Excess Head Loss Factors

# In[2]:


Entrance=1
Exit=0.5
Others=0
total_Head_Factor= Entrance+Exit+Others
print(total_Head_Factor)


# ## Calculated Results

# In[20]:


import numpy as np
import math
pi=math.pi
hole_area=(pi*(Hole_Diameter*0.001)**2)/4
print(str(hole_area) +" m2")


# ## Equation terms

# In[25]:


dP=Tank_Pressure-Pressure_Outside_hole
Pressure_term=(dP*100000)/Liquid_density
Height_term=9.8*(0-Liquid_level_above_hole)
Velocity_coefficient=0.5+total_Head_Factor/2


# ## Results

# In[34]:


Exit_velocity=math.sqrt((Pressure_term-Height_term)/Velocity_coefficient)
mass_flow=Exit_velocity*Liquid_density*hole_area


# In[42]:


print("Exict velocity is: "+str(round(Exit_velocity,2))+" m/s")
print("Mass Flow is: "+str(round(mass_flow,2))+" kg/s")


# In[ ]:




