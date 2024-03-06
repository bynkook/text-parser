import re

def text_extractor(infile):
    output, output_text = [], []
    for line in infile:
        x = re.findall(r'[^\s,]+', line)
        if x != []:
            output.append(str_to_num_in_list(x))
            output_text.append(x)
    return output, output_text

def str_to_num_in_list(input):
    output = []
    for x in input:
        try:
            val = float(x)
            if val.is_integer():
                output.append(int(val))
            else:
                output.append(val)
        except ValueError:
            output.append(x)
    return output

def text_writer(input, outfile):
    for line in input:
        outfile.write(' '.join(line)+'\n')

with open('./textparser/test.dat','rt') as infile, open('./textparser/test.out','wt') as outfile:
    output, output_text = text_extractor(infile)
    text_writer(output_text,outfile)