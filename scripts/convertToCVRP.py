import csv
	 
points = []
count = 0
with open("../data/RBMS_line_904_bus_8611_freq_filtered.txt", "rb") as f:
	reader = csv.reader(f)
	for row in reader:
		count += 1
		points.append((row[0], row[1]))

print("NAME : H-n" + str(count) + "-k1")
print("COMMENT : (Hackathon EMTU)")
print("TYPE : CVRP")
print("DIMENSION : " + str(count))
print("EDGE_WEIGHT_TYPE : EUC_2D") 
print("CAPACITY : 10000")
print("NODE_COORD_SECTION")

for i in range(1, count + 1):
	print(str(i) + " " + points[i - 1][0] + " " + points[i - 1][1])

print("DEMAND_SECTION")
print("1 0")
for i in range(2, count + 1):
	print(str(i) + " 1")
print("DEPOT_SECTION") 
print("1")  
print("-1")  
print("EOF") 
