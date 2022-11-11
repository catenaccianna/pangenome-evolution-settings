#!/usr/bin/python3
import os
import glob
from glob import iglob
import pandas as pd


#######		FITNESS 		#######

def concat_fitness(path, new_path, condition, filename):
	"""
    given 30 replicants of fitness data, combine all replicant data into one CSV file
    :param path: location to directory containing CSVs to combine
    :param new_path: new path and filename for the new CSV that contains all of the data from the fitness.csv replicants in path
	:param condition: condition that this file contains the fitness data of, to add into a column
	:param filename: final filename to add into a column
    """
	os.chdir(path)
	extension = 'csv'
	all_filenames = []
	for subdirs, dirs, files in os.walk(path):
		os.chdir(subdirs)
		for file in glob.glob('fitness.{}'.format(extension)):
			temp_df = pd.read_csv(file)
			all_filenames.append(temp_df)

	fitness_df = pd.concat(all_filenames, axis = 0)

	fitness_df['Filename'] = [filename] * len(fitness_df.axes[0])
	fitness_df['Condition'] = [condition] * len(fitness_df.axes[0])
	fitness_df.to_csv(new_path, index = False, encoding = 'utf-8-sig')
	#i have the original 1P_SC random seed of 999 fitness.csv being 1000 data pieces long (1001 with title)
	#and the 1P_SC_fitness.csv that is supposed to have like 30 replicants is all random seed 999 data repeated 30 times
	#it has 30,000 lines (30,001 with title)

concat_fitness("/mnt/c/Users/Anna Catenacci/Desktop/data_sets/data_control/", r'/mnt/c/Users/Anna Catenacci/Desktop/fitness/control_fitness.csv', "control", "control_fitness.csv")
concat_fitness("/mnt/c/Users/Anna Catenacci/Desktop/data_sets/data_0.01P_NSC/", r'/mnt/c/Users/Anna Catenacci/Desktop/fitness/0.01P_NSC_fitness.csv', "0.01P_NSC", "0.01P_NSC_fitness.csv")
concat_fitness("/mnt/c/Users/Anna Catenacci/Desktop/data_sets/data_0.01P_SC/", r'/mnt/c/Users/Anna Catenacci/Desktop/fitness/0.01P_SC_fitness.csv', "0.01P_SC", "0.01P_SC_fitness.csv")
concat_fitness("/mnt/c/Users/Anna Catenacci/Desktop/data_sets/data_1P_NSC/", r'/mnt/c/Users/Anna Catenacci/Desktop/fitness/1P_NSC_fitness.csv', "1P_NSC", "1P_NSC_fitness.csv")
concat_fitness("/mnt/c/Users/Anna Catenacci/Desktop/data_sets/data_1P_SC/", r'/mnt/c/Users/Anna Catenacci/Desktop/fitness/1P_SC_fitness.csv', "1P_SC", "1P_SC_fitness.csv")

#######		PANGENOME GRAPH 		#######

def concat_graphs(path, new_path, condition, filename):
	"""
    given 30 replicants of data representing the edges of a graph data structure that describes a pangenome,
	combine all replicant data into one CSV file
    :param path: location to directory containing CSVs to combine
    :param new_path: new path and filename for the new CSV that contains all of the data from the fitness.csv replicants in path
	:param condition: condition that this file contains the genomes of, to add into a column
	:param filename: final filename to add into a column
    """
	os.chdir(path)
	extension = 'csv'
	all_filenames = []
	for subdirs, dirs, files in os.walk(path):
		os.chdir(subdirs)
		for file in glob.glob('DeBruijnGraph.{}'.format(extension)):
			temp_df = pd.read_csv(file)
			all_filenames.append(temp_df)

	graphs_df = pd.concat(all_filenames, axis = 0)

	graphs_df['Filename'] = [filename] * len(graphs_df.axes[0])
	graphs_df['Condition'] = [condition] * len(graphs_df.axes[0])
	graphs_df.to_csv(new_path, index = False, encoding = 'utf-8-sig')

concat_graphs("/mnt/c/Users/Anna Catenacci/Desktop/data_sets/data_0.01P_NSC/", r'/mnt/c/Users/Anna Catenacci/Desktop/pangenome_graph/0.01P_NSC_graph.csv', "0.01P_NSC", "0.01P_NSC_graph.csv")
concat_graphs("/mnt/c/Users/Anna Catenacci/Desktop/data_sets/data_0.01P_SC/", r'/mnt/c/Users/Anna Catenacci/Desktop/pangenome_graph/0.01P_SC_graph.csv', "0.01P_SC", "0.01P_SC_graph.csv")
concat_graphs("/mnt/c/Users/Anna Catenacci/Desktop/data_sets/data_1P_NSC/", r'/mnt/c/Users/Anna Catenacci/Desktop/pangenome_graph/1P_NSC_graph.csv', "1P_NSC", "1P_NSC_graph.csv")
concat_graphs("/mnt/c/Users/Anna Catenacci/Desktop/data_sets/data_1P_SC/", r'/mnt/c/Users/Anna Catenacci/Desktop/pangenome_graph/1P_SC_graph.csv', "1P_SC", "1P_SC_graph.csv")


#######		COMBINE REPLICANTS 		#######


path = "/mnt/c/Users/Anna Catenacci/Desktop/fitness/"
os.chdir(path)
extension = 'csv'
all_filenames = ["control_fitness.csv", "1P_NSC_fitness.csv", "1P_SC_fitness.csv", "0.01P_NSC_fitness.csv", "0.01P_SC_fitness.csv"]
df = pd.DataFrame()
df = pd.concat([pd.read_csv(f) for f in all_filenames], axis = 0)
df.to_csv(r'/mnt/c/Users/Anna Catenacci/Desktop/fitness/fitness_all.csv', index = False, encoding = 'utf-8-sig')


path = "/mnt/c/Users/Anna Catenacci/Desktop/pangenome_graph/"
os.chdir(path)
extension = 'csv'
all_filenames = ["1P_NSC_graph.csv", "1P_SC_graph.csv", "0.01P_NSC_graph.csv", "0.01P_SC_graph.csv"]
df = pd.DataFrame()
df = pd.concat([pd.read_csv(f) for f in all_filenames], axis = 0)
df.to_csv(r'/mnt/c/Users/Anna Catenacci/Desktop/pangenome_graph/pangenome_all.csv', index = False, encoding = 'utf-8-sig')
