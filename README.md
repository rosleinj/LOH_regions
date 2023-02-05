This code processes a 7-column csv table and identifies homozygotic regions with shared allelic origin. The table should contain the following columns:

Chromosome name
Position
Reference genotype in IUPAC code
Species A genotype
Species A allelic depth
Species B genotype
Species B allelic depth
Usage
css
Copy code
python allelic_origin_identifier.py --input_file <input_csv_file> --output_file <output_csv_file>
Input
The input csv file should have the following columns:

Chromosome name (string)
Position (integer)
Reference genotype in IUPAC code (string, one of "A", "C", "G", "T", "K", "R", "M", "Y", "S", "W")
Species A genotype (string, one of "A", "C", "G", "T")
Species A allelic depth (integer)
Species B genotype (string, one of "A", "C", "G", "T")
Species B allelic depth (integer)
Output
The code outputs a csv file with the following columns:

Chromosome name (string)
Start position (integer)
End position (integer)
Type of homozygotic region (string, one of "T-like", "E-like")
Example
For the input csv file:

chromosome,position,reference,genotype_A,depth_A,genotype_B,depth_B
chr1,61996,A,A,15,G,8
chr1,66784,C,C,19,T,2
chr1,69918,R,A,16,G,9
chr1,69921,A,A,1,G,12
chr1,69927,A,A,1,G,40
chr1,69938,K,A,1,G,30

output:
chromosome,start,end,allelic origin
chr1,61996,66784,A-like
chr1,69921,69927,B-like

