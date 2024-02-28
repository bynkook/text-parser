def text_extractor(infile):
    output = []
    for line in infile:
        # handle spaces
        line1 = ','.join(line.split())
        # handle commas
        line2 = list(map(str.strip, line1.split(',')))
        # remove empty strings from list
        line3 = [x for x in line2 if x]
        output.append(line3)
    return output

def text_writer(input, outfile):
    for line in input:
        outfile.write(' '.join(line)+'\n')

with open('./textparser/test.dat','rt') as infile, open('./textparser/test.out','wt') as outfile:
    output = text_extractor(infile)
    text_writer(output,outfile)