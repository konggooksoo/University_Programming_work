#!/usr/bin/env python3
import matplotlib.pyplot as plt

""" If user want to display all of the created graph through Terminal system,
     Please type Ex:) $ python3 graph.py
                                          """


# Analysis1 for Capacity
bus_names = ["buses", "buses1", "buses2"]
bus_capacity = [5, 5, 5]
plt.figure(figsize=(12, 4))
ax = plt.subplot(1, 3, 1)
plt.xlabel("name of bus")
plt.ylabel("capacity of bus")
plt.bar(bus_names, bus_capacity)
plt.suptitle("Figure 1 - categorical plotting")
plt.show()

bus_names = ["buses", "buses1", "buses2"]
bus_capacity = [8, 8, 8]
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.xlabel("name of bus")
plt.ylabel("capacity of bus")
plt.bar(bus_names, bus_capacity)
plt.suptitle("Figure 2 -categorical plotting")
plt.show()

plt.suptitle('Figure 3 - The number of waiting people depends on capacity of bus')
plt.xlabel("Time")
plt.ylabel("The number of waiting people")
plt.plot([0, 100, 200, 300, 400, 500], [0, 9, 20, 23, 38, 47])
plt.plot([0, 100, 200, 300, 400, 500], [0, 4, 18, 11, 9, 13])
plt.annotate("Maxcap = 5", xy=(500, 47), xytext=(400, 35))
plt.annotate("Maxcap = 8", xy=(500, 15), xytext=(400, 15))
plt.show()

# Analysis2
plt.suptitle("Figure 7 - The number of waiting people depends on the number of bus")
plt. xlabel("Time")
plt.ylabel("The number of waiting people")
plt.plot([1, 100, 200, 300, 400, 500], [0, 12, 30, 43, 54, 71])
plt.plot([0, 100, 200, 300, 400 ,500], [0, 12, 10, 3, 11, 9])
plt.annotate("Two buses", xy=(500,47), xytext = (400, 50))
plt.annotate("Three buses", xy=(500, 15), xytext = (400, 15))
plt.show()

# Analysis2 for Speed
bus_names = ["buses", "buses1", "buses2"]
bus_speed1_category = [1, 2, 3]
plt.figure(figsize=(9, 4))
plt.subplot(1, 3, 1)
plt.xlabel("Name of Bus")
plt.ylabel("Speed of BUs")
plt.bar(bus_names, bus_speed1_category)
plt.suptitle("Figure 4 - The speed of buses")
plt.show()

bus_names = ["buses", "buses1", "buses2"]
bus_speed2_category = [3, 4, 5]
plt.figure(figsize=(9, 4))
plt.subplot(1, 3, 1)
plt.xlabel("Name of Bus")
plt.ylabel("Speed of Bus")
plt.bar(bus_names, bus_speed2_category)
plt.suptitle("Figure 5 - The speed of buses")
plt.show()

plt.suptitle('Figure 6 - The number of waiting people depends on speed of bus')
plt.xlabel("Time")
plt.ylabel("The number of waiting people")
plt.plot([0, 100, 200, 300, 400, 500], [0, 14, 11, 9, 10, 12])
plt.plot([0, 100, 200, 300, 400, 500], [0, 3, 5, 2, 4, 4])
plt.annotate("bus_speed1_category", xy=(500, 15), xytext=(130, 7.5))
plt.annotate("bus_speed2_category", xy=(500, 15), xytext=(180, 17.5))
plt.show()
