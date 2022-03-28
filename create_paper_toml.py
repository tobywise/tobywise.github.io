## Load in a csv file and convert it to a toml file

import pandas as pd
import toml
import argparse
import pytablewriter
import os

if __name__ == "__main__":

    # Get filename from command line
    parser = argparse.ArgumentParser(description='Convert csv to toml')
    parser.add_argument('csv_file', type=str, help='csv file to convert')
    args = parser.parse_args()

    # Load in csv file
    csv_file = 'papers2.csv'
    df = pd.read_csv(args.csv_file)

    toml_string = ''

    # Add header
    toml_string += '[table]\n'

    # Add columns
    toml_string += '[[row]]\n'
    toml_string +=  'data = ["' + '","'.join([i.capitalize() for i in df.columns]) + '"]' + '\n'

    # Loop through rows
    for index, row in df.iterrows():
        toml_string += '[[row]]\n'
        row['authors'] = row['authors'].replace('Wise, T.', '<u>Wise, T.</u>')
        if row['article'] != '-':
            row['article'] = '[Link](' + row['code'] + ')'
        if row['code'] != '-':
            row['code'] = '[Link](' + row['code'] + ')'
        if row['data'] != '-':
            row['data'] = '[Link](' + row['data'] + ')'
        toml_string += 'data = ["' + '","'.join([str(i) for i in row]) + '"]' + '\n'

    # Write to file
    toml_file = os.path.join('data', args.csv_file.replace('.csv', '.toml'))
    with open(toml_file, 'w') as f:
        f.write(toml_string)

    print('Converted {} to {}'.format(args.csv_file, toml_file))

