#!/usr/bin/python3
"""
Created by Chris on Github in 2019: ekapope/Combine-CSV-files-in-the-folder
Modified by Anna Catenacci
"""
import os
import glob
from glob import iglob
import pandas as pd

#path = "/mnt/home/catenac6/pangenomes/mabe_random_pangenomes/random_data/"
path = "/mnt/c/Users/Anna Catenacci/Desktop/data_control/"
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
all_fitness.to_csv(r'/mnt/c/Users/Anna Catenacci/Desktop/control_fitness.csv', index = False, encoding = 'utf-8-sig')


path = "/mnt/c/Users/Anna Catenacci/Desktop/data_1P_SC/"
os.chdir(path)
extension = 'csv'
all_filenames = []
for subdirs, dirs, files in os.walk(path):
	os.chdir(subdirs)
	for file in glob.glob('fitness.{}'.format(extension)):
		all_filenames.append(file)
all_fitness = pd.concat([pd.read_csv(f) for f in all_filenames], axis = 0)
all_fitness.to_csv(r'/mnt/c/Users/Anna Catenacci/Desktop/1P_SC_fitness.csv', index = False, encoding = 'utf-8-sig')

path = "/mnt/c/Users/Anna Catenacci/Desktop/data_1P_NSC/"
os.chdir(path)
extension = 'csv'
all_filenames = []
for subdirs, dirs, files in os.walk(path):
	os.chdir(subdirs)
	for file in glob.glob('fitness.{}'.format(extension)):
		all_filenames.append(file)
for f in all_filenames:
	all_fitness = pd.concat([pd.read_csv(f)], axis = 0)
#all_fitness = pd.concat([pd.read_csv(f) for f in all_filenames], axis = 1)
all_fitness.to_csv(r'/mnt/c/Users/Anna Catenacci/Desktop/1P_NSC_fitness.csv', index = False, encoding = 'utf-8-sig')

path = "/mnt/c/Users/Anna Catenacci/Desktop/data_0.01P_SC/"
os.chdir(path)
extension = 'csv'
all_filenames = []
for subdirs, dirs, files in os.walk(path):
	os.chdir(subdirs)
	for file in glob.glob('fitness.{}'.format(extension)):
		all_filenames.append(file)
all_fitness = pd.concat([pd.read_csv(f) for f in all_filenames], axis = 0)
all_fitness.to_csv(r'/mnt/c/Users/Anna Catenacci/Desktop/0.01P_SC_fitness.csv', index = False, encoding = 'utf-8-sig')

path = "/mnt/c/Users/Anna Catenacci/Desktop/data_0.01P_NSC/"
os.chdir(path)
extension = 'csv'
all_filenames = []
for subdirs, dirs, files in os.walk(path):
	os.chdir(subdirs)
	for file in glob.glob('fitness.{}'.format(extension)):
		all_filenames.append(file)
all_fitness = pd.concat([pd.read_csv(f) for f in all_filenames], axis = 0)
all_fitness.to_csv(r'/mnt/c/Users/Anna Catenacci/Desktop/0.01P_NSC_fitness.csv', index = False, encoding = 'utf-8-sig')










#put anything else you want in concat--axis = 1?
#want to have all 30 iterations in each dir into one csv, so 5 of these
#keys=(list(i for i in range(30)) can be a parameter at the end if wanted
all_fitness = pd.concat([pd.read_csv(f) for f in all_filenames], axis = 0)

#remember that I want the columns that indicate time step, random seed, condition for each condition
all_fitness.to_csv(r'/mnt/c/Users/Anna Catenacci/Desktop/control_graph.csv', index = False, encoding = 'utf-8-sig')


#path = "/mnt/c/Users/Anna Catenacci/Desktop/graph_1P_SC/"
path = "/mnt/c/Users/Anna Catenacci/Desktop/data_1P_SC/"
os.chdir(path)
extension = 'csv'
all_filenames = []
for subdirs, dirs, files in os.walk(path):
	os.chdir(subdirs)
	for file in glob.glob('DeBruijnGraph.{}'.format(extension)):
		all_filenames.append(file)
all_fitness = pd.concat([pd.read_csv(f) for f in all_filenames], axis = 0)
all_fitness.to_csv(r'/mnt/c/Users/Anna Catenacci/Desktop/1P_SC_graph.csv', index = False, encoding = 'utf-8-sig')

#path = "/mnt/c/Users/Anna Catenacci/Desktop/graph_1P_NSC/"
path = "/mnt/c/Users/Anna Catenacci/Desktop/data_1P_NSC/"
os.chdir(path)
extension = 'csv'
all_filenames = []
for subdirs, dirs, files in os.walk(path):
	os.chdir(subdirs)
	for file in glob.glob('DeBruijnGraph.{}'.format(extension)):
		all_filenames.append(file)
for f in all_filenames:
	all_fitness = pd.concat([pd.read_csv(f)], axis = 0)
#all_fitness = pd.concat([pd.read_csv(f) for f in all_filenames], axis = 1)
all_fitness.to_csv(r'/mnt/c/Users/Anna Catenacci/Desktop/1P_NSC_graph.csv', index = False, encoding = 'utf-8-sig')

#path = "/mnt/c/Users/Anna Catenacci/Desktop/graph_0.01P_SC/"
path = "/mnt/c/Users/Anna Catenacci/Desktop/data_0.01P_SC/"
os.chdir(path)
extension = 'csv'
all_filenames = []
for subdirs, dirs, files in os.walk(path):
	os.chdir(subdirs)
	for file in glob.glob('DeBruijnGraph.{}'.format(extension)):
		all_filenames.append(file)
all_fitness = pd.concat([pd.read_csv(f) for f in all_filenames], axis = 0)
all_fitness.to_csv(r'/mnt/c/Users/Anna Catenacci/Desktop/0.01P_SC_graph.csv', index = False, encoding = 'utf-8-sig')

#path = "/mnt/c/Users/Anna Catenacci/Desktop/graph_0.01P_NSC/"
path = "/mnt/c/Users/Anna Catenacci/Desktop/data_0.01P_NSC/"
os.chdir(path)
extension = 'csv'
all_filenames = []
for subdirs, dirs, files in os.walk(path):
	os.chdir(subdirs)
	for file in glob.glob('DeBruijnGraph.{}'.format(extension)):
		all_filenames.append(file)
all_fitness = pd.concat([pd.read_csv(f) for f in all_filenames], axis = 0)
all_fitness.to_csv(r'/mnt/c/Users/Anna Catenacci/Desktop/0.01P_NSC_graph.csv', index = False, encoding = 'utf-8-sig')
