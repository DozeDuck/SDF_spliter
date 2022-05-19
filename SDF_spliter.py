import getopt
import sys



args=sys.argv[1:]                                                                   # get arguments from usr's input; filename is sys.arg[0], so args start from [1:]


try:
   opts, args = getopt.getopt(args,"h:i:n:o:",["help","input_file=","number_per_sublibrary=","output_name="])
except getopt.GetoptError:
   print ('spliter.py -i <inputfile> -n <number_per_sublibrary> -o <output_name>')
   sys.exit(2)                                                                      # Exiting the program raises a SystemExit exception, 0 means normal exit, and others are abnormal exits.
 
for opt, arg in opts:                                                               # Generate several pairs of value, e.g: opr,arg = -i,PLDXPAL
   if opt == '-h':
      print ('spliter.py -i <inputfile> -n <number_per_sublibrary> -o <output_name>')
      sys.exit()
   elif opt in ("-i", "--input_seq"):
      f = arg
   elif opt in ("-n", "--number"):
      split_number = int(arg)
   elif opt in ("-o", "--outputfile"):
      out_put_name = arg
       



# f= "bigsdffilename"
# split_number= 100 
number_of_sdfs = split_number
i=0
j=0
f2=open(out_put_name+'_'+str(j)+'.sdf','w')
# for line in open(f+'.sdf'):
for line in open(f):
	f2.write(line)
	if(line[:4] == "$$$$"):
		i+=1
	if(i > number_of_sdfs):
		number_of_sdfs += split_number 
		f2.close()
		j+=1
		f2=open(out_put_name +'_'+str(j)+'.sdf','w')
print(i)
