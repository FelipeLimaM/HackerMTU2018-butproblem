def createCVRPInput(points, k):
	filename = "H-n" + str(len(points)) + "-k" + str(k)
	out = open("/tmp/" + filename + ".vrp", "w")
	out.write("NAME : H-n" + str(len(points)) + "-k" + str(k))
	out.write("COMMENT : (Hackathon EMTU)")
	out.write("TYPE : CVRP")
	out.write("DIMENSION : " + str(len(points)))
	out.write("EDGE_WEIGHT_TYPE : EUC_2D") 
	out.write("CAPACITY : 10000")
	out.write("NODE_COORD_SECTION")

	for i in range(1, len(points) + 1):
		out.write(str(i) + " " + points[i - 1][0] + " " + points[i - 1][1])

	out.write("DEMAND_SECTION")
	out.write("1 0")
	for i in range(2, len(points) + 1):
		out.write(str(i) + " 1")
	out.write("DEPOT_SECTION") 
	out.write("1")  
	out.write("-1")  
	out.write("EOF") 
	out.close()
	
	return filename
