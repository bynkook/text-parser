def text_extractor(infile):
    output, output_text = [], []
    for line in infile:
        # handle spaces
        line1 = ','.join(line.split())
        # handle commas
        line2 = list(map(str.strip, line1.split(',')))
        # remove empty strings from list
        line3 = [x for x in line2 if x]
        if line3 != []:
            output_text.append(line3)
            line4 = string_to_number_in_list(line3)
            output.append(line4)
    return output, output_text

def string_to_number_in_list(line):
    output = []
    for x in line:
        try:
            converted_value = float(x)
            if converted_value.is_integer():
                output.append(int(converted_value))
            else:
                output.append(converted_value)
        except ValueError:
            output.append(x)
    return output

def text_writer(input, outfile):
    for line in input:
        outfile.write(' '.join(line)+'\n')

with open('./textparser/test.dat','rt') as infile, open('./textparser/test.out','wt') as outfile:
    output, output_text = text_extractor(infile)
    print(output)
    text_writer(output_text,outfile)
