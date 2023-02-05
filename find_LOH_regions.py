import csv
import argparse

def process_csv_file(input_file, output_file):
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
        results = ['', 0, 0, '']
        counter = 0

        with open(output_file, 'w') as outfile:
            for i, row in enumerate(rows):
                if str(row[2]) not in ['A','C','G','T']:
                    if counter > 1:
                        outfile.write(f"{results[0]},{results[1]},{results[2]},{results[3]}\n")
                    results = ['', 0, 0, '']
                    counter = 0
                    continue
                if i == 0:
                    results[0] = str(row[0])
                    results[1] = int(row[1])
                    results[2] = int(row[1])
                    results[3] = 'A-like' if int(row[4]) > int(row[6]) else 'B-like'
                    counter = 1
                    continue
                if str(row[2]) in ['A','C','G','T'] and str(results[0]) == str(row[0]):
                    if str(row[0]) == str(rows[i-1][0]) and row[2] in ['A','C','G','T'] and int(row[4]) > int(row[6]) and str(results[3]) == 'A-like':
                        results[2] = int(row[1])
                        counter += 1
                    elif str(row[0]) == str(rows[i-1][0]) and row[2] in ['A','C','G','T'] and int(row[4]) < int(row[6]) and str(results[3]) == 'B-like':
                        results[2] = int(row[1])
                        counter += 1
                else:
                    results[0] = str(row[0])
                    results[1] = int(row[1])
                    results[2] = int(row[1])
                    results[3] = 'A-like' if int(row[4]) > int(row[6]) else 'B-like'
                    counter = 1
                    continue

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process CSV file")
    parser.add_argument("input_file", help="Input file path")
    parser.add_argument("output_file", help="Output file path")
    args = parser.parse_args()

    process_csv_file(args.input_file, args.output_file)
