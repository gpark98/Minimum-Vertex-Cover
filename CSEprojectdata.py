#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:02:40 2022

@author: nathanwilliams
"""

import numpy as np
import matplotlib.pyplot as plt

graph_list = ["jazz","karate","football","as-22july06", "hep-th", 
              "star", "star2", "netscience", "email", "delaunay_n10",
              "power"]


bnb_time = [0.67, 0.0027, 0.20, 0.00, 34105.80,
            0.00, 0.00, 130.77, 91.47, 80.54, 34517.60]
approx_time = [0.0062, 0.00015, 0.0020, 19.49, 6.61,
               13.99, 15.53, 0.26, 0.14, 0.14, 2.28]
lc1_time = [0.2, 0.00082, 0.026, 75.61, 66.04,
            96.31, 92.70, 0.55, 1.05, 6.42, 92.45]
lc2_time = [9.29, 0.48, 3.16, 3084.50, 313.89,
            252.60, 421.05, 443.15, 562.01, 169.19, 127.85]

bnb_error = [0.00, 0.00, 0.00, 5.95, 0.0041,
             0.60, 2.11, 0.00, 0.013, 0.038, 0.025]
approx_error = [0.0063, 0.00, 0.021, 0.0012, 0.0046,
                0.068, 0.034, 0.00, 0.019, 0.048, 0.034]
lc1_error = [0.0057, 0.00, 0.018, 0.0023, 0.0034,
             0.067, 0.029, 0.00, 0.013, 0.030, 0.014]
lc2_error = [0.0015, 0.00, 0.013, 0.0021, 0.0038,
             0.064, 0.028, 0.00, 0.011, 0.038, 0.024]



# Time First

ind = np.arange(len(graph_list)) 
width = 0.2

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
spacing = 0.2 #0.200
fig.subplots_adjust(bottom=spacing)

#bar1 = plt.bar(ind, bnb_time, width, color = 'r')
bar2 = plt.bar(ind, approx_time, width, color='g')
bar3 = plt.bar(ind+width, lc1_time, width, color = 'b')
bar4 = plt.bar(ind+width*2, lc2_time, width, color = 'y')
plt.tick_params(axis='both', which='major', labelsize=8)

plt.xlabel("Graphs")
plt.ylabel('Time (S)')
plt.title("Algorithm Time Comparison")
plt.xticks(ind+width,graph_list)
plt.legend( (bar2, bar3, bar4), ('Approx', 'LS1', 'LS2'))
plt.show()

# Error
ind = np.arange(len(graph_list)) 
width = 0.2

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
spacing = 0.2 #0.200
fig.subplots_adjust(bottom=spacing)

#bar1 = plt.bar(ind, bnb_error, width, color = 'r')
bar2 = plt.bar(ind, approx_error, width, color='g')
bar3 = plt.bar(ind+width, lc1_error, width, color = 'b')
bar4 = plt.bar(ind+width*2, lc2_error, width, color = 'y')
plt.tick_params(axis='both', which='major', labelsize=8)

plt.xlabel("Graphs")
plt.ylabel('Relative Error')
plt.title("Algorithm Relative Error Comparison")
plt.xticks(ind+width,graph_list)
plt.legend( (bar2, bar3, bar4), ('Approx', 'LS1', 'LS2'))
plt.show()



# # Scatter Maybe (time)
# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True
# fig = plt.figure()
# X_axis = np.arange(len(graph_list))
# #plt.scatter(X_axis, bnb_time, label = 'BnB')
# plt.scatter(X_axis-width, approx_time,label = 'Approx')
# plt.scatter(X_axis, lc1_time,label = 'LS1')
# plt.scatter(X_axis+width, lc2_time,label = 'LS2')
# plt.tick_params(axis='both', which='major', labelsize=8)
# plt.xticks(X_axis, graph_list)
# spacing = 0.1 #0.200
# fig.subplots_adjust(bottom=spacing)
# plt.title("Algorithm Time Comparison")
# plt.ylabel("Time (S)")
# plt.xlabel('Graphs')
# plt.legend()


# # Scatter Relative Error
# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True
# fig = plt.figure()
# X_axis = np.arange(len(graph_list))
# #plt.scatter(X_axis, bnb_error, label = 'BnB')
# plt.scatter(X_axis-width, approx_error,label = 'Approx')
# plt.scatter(X_axis, lc1_error,label = 'LS1')
# plt.scatter(X_axis+width, lc2_error,label = 'LS2')
# plt.tick_params(axis='both', which='major', labelsize=8)
# plt.xticks(X_axis, graph_list)
# spacing = 0.1 #0.200
# fig.subplots_adjust(bottom=spacing)
# plt.title("Algorithm Relative Error Comparison")
# plt.ylabel("Relative Error")
# plt.xlabel('Graphs')
# plt.legend()




# # Graph Dict Vertex Size
# graph_dict = {"jazz": 198,"karate": 34,"football": 115,"as-22july06": 22963, "hep-th": 8361, 
#               "star": 11023, "star2": 14109, "netscience": 1589, "email": 1133, "delaunay_n10": 1024,
#               "power": 4941}



# # Add approx time to graph_dict
# k = 0        
# for i in graph_dict:
#     opt = graph_dict[i]
#     graph_dict[i] = [opt, approx_time[k]]
#     k += 1
#     #graph_dict[i].append(bnb_time)
#     #print(i)
    
# print(graph_dict)

# # Sort it by largest vertex size
# srt = dict(sorted(graph_dict.items(), key=lambda item: item[1][0]))
# print(srt)

# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True
# fig = plt.figure()
# X_axis = np.arange(len(srt))
# new_list = []
# for i in srt:
#     new_list.append(srt[i][1])
# plt.scatter(X_axis, new_list, label = 'Approx')
# plt.tick_params(axis='both', which='major', labelsize=7)
# graph_list = []
# for i in srt:
#     graph_list.append(i)
# plt.xticks(X_axis, graph_list)
# spacing = 0.1 #0.200
# fig.subplots_adjust(bottom=spacing)
# plt.title("Approx Algorithm Time By Vertex Size")
# plt.ylabel("Time (S)")
# plt.xlabel('Graphs')
# plt.legend()

# # Graph Dict Vertex Size
# graph_dict = {"jazz": 2742/198,"karate": 78/34,"football": 613/115,"as-22july06": 48436/22963, "hep-th": 15751/8361, 
#               "star": 62184/11023, "star2": 98224/14109, "netscience": 2742/1589, "email": 5451/1133, "delaunay_n10": 3056/1024,
#               "power": 6594/4941}


# # Add approx time to graph_dict
# k = 0        
# for i in graph_dict:
#     opt = graph_dict[i]
#     graph_dict[i] = [opt, approx_error[k]]
#     k += 1
#     #graph_dict[i].append(bnb_time)
#     #print(i)
    

# # Sort it by largest vertex size
# srt = dict(sorted(graph_dict.items(), key=lambda item: item[1][0]))
# print(srt)

# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True
# fig = plt.figure()
# X_axis = np.arange(len(srt))
# new_list = []
# for i in srt:
#     new_list.append(srt[i][1])
# plt.scatter(X_axis, new_list, label = 'Approx')
# plt.tick_params(axis='both', which='major', labelsize=7)
# graph_list = []
# for i in srt:
#     graph_list.append(i)
# plt.xticks(X_axis, graph_list)
# spacing = 0.1 #0.200
# fig.subplots_adjust(bottom=spacing)
# plt.title("Approx Algorithm Relative Error by Edge to Vertex Ratio")
# plt.ylabel("Relative Error")
# plt.xlabel('Graphs')
# plt.legend()
