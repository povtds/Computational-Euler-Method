# TDS Numerical Python Operations for NUMMET Practical (22nd May 2025)
# Importing the Required Numerical Python Packages :
# Avoid Indentation-Errors
###############################################################################
import numpy as TDS
import matplotlib.pyplot as plt
###############################################################################
# Loading Data from the provided Text File :
# For example : data = TDS.loadtxt('data.txt')
CoolingLaw_Temperature_vs_Time = TDS.loadtxt('CoolingLaw_Temperature_vs_Time.txt')
CoolingLaw_As_Lambda_Changes = TDS.loadtxt('CoolingLaw_As_Lambda_Changes.txt')

# Section Number [01]
# 1) Considering the CoolingLaw_Temperature_vs_Time Text File
# The First Column is Time (in seconds) and the 2nd Column is Temperature in °C :
Time = CoolingLaw_Temperature_vs_Time [:, 0]
Temperature = CoolingLaw_Temperature_vs_Time [:, 1]

# Section Number [02]
# 2) Considering the CoolingLaw_As_Lambda_Changes Text File
# The First Column is Lambda (heat transfer coefficient/constant) and the 2nd Column is Temperature in °C :
Lambda = CoolingLaw_As_Lambda_Changes [:, 0]
Temperature_Depending_On_Lambda = CoolingLaw_As_Lambda_Changes [:, 1]

# Creating the Line Graphs and Adding Labels :

# 1) Plotting Position vs Time :
plt.figure() # Create a New Figure to Avoid Overlapping Another Plot
plt.plot(Time, Temperature, label = 'Line Graph', color='green')
plt.xlabel('Time (s)')
plt.ylabel('Temperaure (°C)')
plt.title('Line Graph of Temperature (°C) vs Time (s)')
plt.legend()
plt.grid(True)
plt.show()

# 2) Plotting Velocity vs Time :
plt.figure() # Create Another New Figure
plt.plot(Lambda, Temperature_Depending_On_Lambda, label = 'Line Graph', color='red')
plt.xlabel('Lambda')
plt.ylabel('Temperature (°C)')
plt.title('Line Graph of Temperature (°C) vs Lambda')
plt.legend()
plt.grid(True)
plt.show()
