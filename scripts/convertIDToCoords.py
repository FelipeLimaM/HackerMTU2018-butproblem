h = {}

i = 0
with open("../tmp/hackemtu.vrp", "rb") as f:
	for row in f:
		i += 1
		if i >= 8:
			if row == "DEMAND_SECTION\n":
				break
				
			row = row.split()
			h[int(row[0])] = (row[1], row[2])

with open("../tmp/H-n42-k1.out", "rb") as f:
	for row in f:
		row = row.split()
		
		for v in row:
			v = int(v)
			print(h[v + 1][0] + ", " + h[v + 1][1])
		
		print("#") 
