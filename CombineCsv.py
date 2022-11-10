#!/usr/bin/python3
"""
Created by Chris on Github in 2019: ekapope/Combine-CSV-files-in-the-folder
"""
import os
import glob
from glob import iglob
import pandas as pd


#######		FITNESS 		#######


#path = "/mnt/home/catenac6/pangenomes/mabe_random_pangenomes/random_data/"
path = "/mnt/c/Users/Anna Catenacci/Desktop/data_sets/data_control/"
os.chdir(path)
extension = 'csv'
#all_files = [f for f in iglob(path, recursive = True) if ]
#all_files = [i for i in glob.glob('*.{}'.format(extension))]
all_filenames = []
for subdirs, dirs, files in os.walk(path):
	#print(subdirs, files)
	os.chdir(subdirs)
	for file in glob.glob('fitness.{}'.format(extension)):
		all_filenames.append(file)

#put anything else you want in concat--axis = 1?
#want to have all 30 iterations in each dir into one csv, so 5 of these
#keys=(list(i for i in range(30)) can be a parameter at the end if wanted
all_fitness = pd.concat([pd.read_csv(f) for f in all_filenames], axis = 0)

#remember that I want the columns that indicate time step, random seed, condition for each condition
all_fitness.to_csv(r'/mnt/c/Users/Anna Catenacci/Desktop/fitness/control_fitness.csv', index = False, encoding = 'utf-8-sig')


path = "/mnt/c/Users/Anna Catenacci/Desktop/data_sets/data_1P_SC/"
os.chdir(path)
extension = 'csv'
all_filenames = []
for subdirs, dirs, files in os.walk(path):
	os.chdir(subdirs)
	for file in glob.glob('fitness.{}'.format(extension)):
		all_filenames.append(file)
all_fitness = pd.concat([pd.read_csv(f) for f in all_filenames], axis = 0)
all_fitness.to_csv(r'/mnt/c/Users/Anna Catenacci/Desktop/fitness/1P_SC_fitness.csv', index = False, encoding = 'utf-8-sig')

path = "/mnt/c/Users/Anna Catenacci/Desktop/data_sets/data_1P_NSC/"
os.chdir(path)
extension = 'csv'
all_filenames = []
for subdirs, dirs, files in os.walk(path):
	os.chdir(subdirs)
	for file in glob.glob('fitness.{}'.format(extension)):
		all_filenames.append(file)
for f in all_filenames:
	all_fitness = pd.concat([pd.read_csv(f) for f in all_filenames], axis = 0)
all_fitness.to_csv(r'/mnt/c/Users/Anna Catenacci/Desktop/fitness/1P_NSC_fitness.csv', index = False, encoding = 'utf-8-sig')

path = "/mnt/c/Users/Anna Catenacci/Desktop/data_sets/data_0.01P_SC/"
os.chdir(path)
extension = 'csv'
all_filenames = []
for subdirs, dirs, files in os.walk(path):
	os.chdir(subdirs)
	for file in glob.glob('fitness.{}'.format(extension)):
		all_filenames.append(file)
all_fitness = pd.concat([pd.read_csv(f) for f in all_filenames], axis = 0)
all_fitness.to_csv(r'/mnt/c/Users/Anna Catenacci/Desktop/fitness/0.01P_SC_fitness.csv', index = False, encoding = 'utf-8-sig')

path = "/mnt/c/Users/Anna Catenacci/Desktop/data_sets/data_0.01P_NSC/"
os.chdir(path)
extension = 'csv'
all_filenames = []
for subdirs, dirs, files in os.walk(path):
	os.chdir(subdirs)
	for file in glob.glob('fitness.{}'.format(extension)):
		all_filenames.append(file)
all_fitness = pd.concat([pd.read_csv(f) for f in all_filenames], axis = 0)
all_fitness.to_csv(r'/mnt/c/Users/Anna Catenacci/Desktop/fitness/0.01P_NSC_fitness.csv', index = False, encoding = 'utf-8-sig')


#######		PANGENOME GRAPH 		#######


path = "/mnt/c/Users/Anna Catenacci/Desktop/data_sets/data_1P_SC/"
os.chdir(path)
extension = 'csv'
all_filenames = []
for subdirs, dirs, files in os.walk(path):
	os.chdir(subdirs)
	for file in glob.glob('DeBruijnGraph.{}'.format(extension)):
		all_filenames.append(file)
all_fitness = pd.concat([pd.read_csv(f) for f in all_filenames], axis = 0)
all_fitness.to_csv(r'/mnt/c/Users/Anna Catenacci/Desktop/pangenome_graph/1P_SC_graph.csv', index = False, encoding = 'utf-8-sig')

path = "/mnt/c/Users/Anna Catenacci/Desktop/data_sets/data_1P_NSC/"
os.chdir(path)
extension = 'csv'
all_filenames = []
for subdirs, dirs, files in os.walk(path):
	os.chdir(subdirs)
	for file in glob.glob('DeBruijnGraph.{}'.format(extension)):
		all_filenames.append(file)
for f in all_filenames:
	all_fitness = pd.concat([pd.read_csv(f) for f in all_filenames], axis = 0)
all_fitness.to_csv(r'/mnt/c/Users/Anna Catenacci/Desktop/pangenome_graph/1P_NSC_graph.csv', index = False, encoding = 'utf-8-sig')

path = "/mnt/c/Users/Anna Catenacci/Desktop/data_sets/data_0.01P_SC/"
os.chdir(path)
extension = 'csv'
all_filenames = []
for subdirs, dirs, files in os.walk(path):
	os.chdir(subdirs)
	for file in glob.glob('DeBruijnGraph.{}'.format(extension)):
		all_filenames.append(file)
all_fitness = pd.concat([pd.read_csv(f) for f in all_filenames], axis = 0)
all_fitness.to_csv(r'/mnt/c/Users/Anna Catenacci/Desktop/pangenome_graph/0.01P_SC_graph.csv', index = False, encoding = 'utf-8-sig')

path = "/mnt/c/Users/Anna Catenacci/Desktop/data_sets/data_0.01P_NSC/"
os.chdir(path)
extension = 'csv'
all_filenames = []
for subdirs, dirs, files in os.walk(path):
	os.chdir(subdirs)
	for file in glob.glob('DeBruijnGraph.{}'.format(extension)):
		all_filenames.append(file)
all_fitness = pd.concat([pd.read_csv(f) for f in all_filenames], axis = 0)
all_fitness.to_csv(r'/mnt/c/Users/Anna Catenacci/Desktop/pangenome_graph/0.01P_NSC_graph.csv', index = False, encoding = 'utf-8-sig')


#######		COMBINE REPLICANTS 		#######


# trying with dataframes so i can add that column
path = "/mnt/c/Users/Anna Catenacci/Desktop/fitness/"
os.chdir(path)
extension = 'csv'
#all_files = glob.glob(os.path.join(path, "*_fitness.csv"))
all_filenames = ["control_fitness.csv", "1P_NSC_fitness.csv", "1P_SC_fitness.csv", "0.01P_NSC_fitness.csv", "0.01P_SC_fitness.csv"]

df = pd.DataFrame()
df = pd.concat([pd.read_csv(f) for f in all_filenames], axis = 0)

filename_column = ["control"]*30000 + ["1P_NSC"]*30000 + ["1P_SC"]*30000 + ["0.01P_NSC"]*30000 + ["0.01P_SC"]*30000
df['File'] = filename_column
df.to_csv(r'/mnt/c/Users/Anna Catenacci/Desktop/fitness/fitness_all.csv', index = False, encoding = 'utf-8-sig')



path = "/mnt/c/Users/Anna Catenacci/Desktop/pangenome_graph/"
os.chdir(path)
extension = 'csv'
all_filenames = ["1P_NSC_graph.csv", "1P_SC_graph.csv", "0.01P_NSC_graph.csv", "0.01P_SC_graph.csv"]

df = pd.DataFrame()
df = pd.concat([pd.read_csv(f) for f in all_filenames], axis = 0)

filename_column = ["1P_NSC"]*4800 + ["1P_SC"]*4800 + ["0.01P_NSC"]*4800 + ["0.01P_SC"]*4800
df['File'] = filename_column

df.to_csv(r'/mnt/c/Users/Anna Catenacci/Desktop/pangenome_graph/pangenome_all.csv', index = False, encoding = 'utf-8-sig')
