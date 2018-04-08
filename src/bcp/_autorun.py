from subprocess import call

cmd = "./cvrp.e -i {vrpfile} -o {outfile} -t 3000 -g -s".format(vrpfile="in/cvrp-set-A/A/A-n32-k5.vrp", outfile="test-A-n32-k5.out")
call(cmd, shell=True)
