# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 20:23:24 2017

@author: cmnunn
"""
from MCM_v1 import *
import numpy as np
import matplotlib.pyplot as plt
#import math

#Time parameter(s)
dt = 0.05 #sec

# Map parameters
B = 2 #2 booths
L = 1 #1 exit lane
LANE_WIDTH = 12 #feet
merge_pts = np.zeros(2*B-1)
line_pos = np.zeros(2*B-1)
lanes = [1,0,1]
for i in range(2*B-1):
    line_pos[i] = (i+1)*LANE_WIDTH/2
    
#Free (default, comment other cases)

#Left
merge_pts[0] = 100 #feet
merge_pts[1] = 100
merge_pts[2] = float('inf')

model = TollBoothModel(200, LANE_WIDTH, B, lanes, merge_pts, line_pos, dt)

#print(calc_capacity(model,merge_pts,lanes,200))

steps = 5000

#for i in range(steps):
#    model.step()
# 
#vehicle_pos = model.datacollector.get_agent_vars_dataframe()
#count_data = model.datacollector.get_model_vars_dataframe()
#plt.figure()
#count_data.plot()
#cumulative = count_data.xs(99, level="Step")["Wealth"]
#arr = np.transpose(count_data.values)
#print(arr[0])
#plt.figure()
#plt.plot(range(1,5001),arr[0].tolist())
#plt.plot(arr[1])
#plt.show()

#frame = vehicle_pos.loc[100,'AgentID':'Position']

#plt.ion()
#fig = plt.figure()
#ax = plt.axes(xlim=(0,model.map.width),ylim=(0,model.map.height))
#plot_rate = 4
#for i in range(math.floor(steps/plot_rate)):
#    positions_by_step = vehicle_pos.loc[min(plot_rate*i,steps),'Agent':'Position']
#
#    for car_id in positions_by_step.index.values:
#        car_pos = positions_by_step.loc[car_id,'Position']
#        color = 'r'
#        if car_id < B*2000:
#            color = 'b'
#        ax.add_artist(plt.Rectangle(car_pos, 15, 6, fc=color))
#
#    plt.draw()
#    plt.pause(0.0000000001)
#    plt.cla()

