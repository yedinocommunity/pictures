#!/usr/bin/env python3

import argparse
import collections

def parse_args():
    arg_parser = argparse.ArgumentParser(description='Script to prepere result file before gnuplot using')
    arg_parser.add_argument('--file_name', type=str, required=True, help='name of file to process')
    return arg_parser.parse_args()

if __name__ == "__main__":
	# data = dict()
	data = collections.OrderedDict()
	args = parse_args()
	with open(args.file_name, 'r') as file:
		content = file.readlines()
		for line in content:
			words = line.split()
			if words[1] in data.keys():
				if words[3] in data[words[1]].keys():
					data[words[1]][words[3]].append(float(words[5]))
				else:
					data[words[1]][words[3]] = [float(words[5])]
			else:
				data[words[1]] = collections.OrderedDict({words[3] : [float(words[5])]})

	print(data)
	with open('prepared_'+args.file_name, 'w') as file:
		for crypto, res in data.items():
			for size, speeds in res.items():
				file.write(crypto)
				file.write(' ')
				file.write(size)
				file.write(' ')
				file.write(str(max(speeds)))
				file.write(' ')
				file.write(str(min(speeds)))
				file.write(' ')
				file.write(str(sum(speeds) / len(speeds)))
				file.write('\n')
			
			
