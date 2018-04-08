def createCVRPInput(points, k):
	filename = "H-n" + str(len(points)) + "-k" + str(k)
	out = open("./tmp/" + filename + ".vrp", "w")
	out.write("NAME : H-n" + str(len(points)) + "-k" + str(k) + "\n")
	out.write("COMMENT : (Hackathon EMTU)" + "\n")
	out.write("TYPE : CVRP" + "\n")
	out.write("DIMENSION : " + str(len(points)) + "\n")
	out.write("EDGE_WEIGHT_TYPE : EUC_2D" + "\n") 
	out.write("CAPACITY : 1000" + "\n")
	out.write("NODE_COORD_SECTION" + "\n")

	for i in range(1, len(points) + 1):
		out.write(str(i) + " " + points[i - 1][0] + " " + points[i - 1][1] + "\n")

	out.write("DEMAND_SECTION" + "\n")
	out.write("1 0\n")
	for i in range(2, len(points) + 1):
		out.write(str(i) + " " + points[i - 1][2] + "\n")
	out.write("DEPOT_SECTION" + "\n") 
	out.write("1" + "\n")  
	out.write("-1" + "\n")  
	out.write("EOF") 
	out.close()
	
	return filename
