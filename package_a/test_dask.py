import dask.dataframe as dd

from sys import argv

input_file = argv[1]

################### csv file ##################################
# output_file = input_file.replace('.csv', '_stripped.csv')
# df = dd.read_csv(input_file,sep = '|')
# df = df.drop(['Year', 'Artist'], axis=1)
# df.to_csv(output_file, sep='|', index=False, single_file=True)

################### dat file ##################################

output_file = input_file.replace('.dat', '_stripped.dat')
df = dd.read_csv(input_file,sep='\s+\|\s+')
df = df.drop(['A', 'B'], axis=1)
df.to_csv(output_file, sep='|', index=False, single_file=True)