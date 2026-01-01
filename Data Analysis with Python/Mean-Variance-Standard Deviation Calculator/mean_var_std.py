import numpy as np

def calculate(num_list):
	if len(num_list) == 9:
		np_array = np.array(num_list)
		matrix = np_array.reshape(3,3)
		np_mean = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), float(matrix.mean())]
		np_var = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), float(matrix.var())]
		np_sum = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), int(matrix.sum())]
		np_min = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), int(matrix.min())]
		np_max = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), int(matrix.max())]
		np_std = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), float(matrix.std())]

		num_output = dict()
		num_output = {'mean': np_mean, 'variance': np_var, 'standard deviation': np_std, 'max': np_max, 'min': np_min, 'sum': np_sum}
		return num_output
	else:
		raise ValueError("List must contain nine numbers.")