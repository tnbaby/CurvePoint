import pandas as pd
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-input', default='', help='input file')
parser.add_argument('-output', default='', help='output file')

args = parser.parse_args()

data_xls = pd.read_excel(args.input, index_col = 1, parse_cols=[0, 1])
data_xls.to_csv(args.output, encoding='utf-8')
