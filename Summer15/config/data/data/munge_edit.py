treatments = ['edit_explode_denovo_00002','edit_explode_denovo_10k','edit_explode_denovo_002','edit_explode_denovo_02','edit_explode_denovo_inc30','edit_explode_denovo_inc0']

reps = range(51, 81)

header = 'filename treatment update average\n'

outputFileName = 'munged_genetic_distance.dat'
outFile = open(outputFileName, 'w')
outFile.write(header)

for t in treatments:
    for r in reps:
        fname = t+"_"+str(r)
        update = 0
        curFile = open(fname, 'r')
        for line in curFile:
            if(len(line) > 1 and line[0] != '#'):
                splitline = line.split(' ')
                oneLine = fname +" "+ fname[:-3] +" "+ str(update)+" " + splitline[2] + "\n"
                update += 1000
                outFile.write(oneLine)
        curFile.close()
outFile.close()
