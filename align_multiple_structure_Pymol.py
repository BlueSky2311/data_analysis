### begin script ###

from pymol import cmd
from glob import glob

# Edit variables with the paths
wt_file = r"C:\Users\darkh\Downloads\test\3ktq.pdb"
mut_glob = r"C:\Users\darkh\Downloads\test\mut\*.pdb"
output_file = "results.txt"
# load the wild-type pdb
cmd.load(wt_file,"wt")
results = []
# loop through the mutants
for file in glob(mut_glob):
    print(file)
    cmd.load(file,"mut")
    rms = cmd.align("wt","mut",cutoff=2.5)
    result = {"File": file, "RMSD": rms[0]}
    results.append(result)
    print("%s rmsd: %s" % (file, rms[0]))

    cmd.delete("mut")
# Export results to a text file
with open(output_file, "w") as f:
    for result in results:
        f.write("RMSD: {}\n".format(result["RMSD"]))
### end script ###
