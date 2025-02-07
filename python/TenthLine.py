'''
Given a text file file.txt, print just the 10th line of the file.

Example:

Assume that file.txt has the following content:

Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
Your script should output the tenth line, which is:

Line 10
'''

# Read from the file file.txt and output the tenth line to stdout.
python3 -c 'a = [l for l in open("file.txt")]; print("" if len(a) < 10 else a[9].strip())'
