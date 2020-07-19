import pandas as pd
import re
import os
import sys

csv_file_path = sys.argv[1]
wmr_indexes_file_path = sys.argv[2]
output_path = sys.argv[3]

# Read in contents section in MIRs and indexes of MIRs respectively
MIR_contents = list(pd.read_csv(csv_file_path,encoding='SHIFT_JIS',index_col=False)['事故の内容.1'])
MIR_indexes = list(pd.read_csv(csv_file_path,encoding='SHIFT_JIS',index_col=False)['事例ID'])

# Selecting MIR contents whose number of character are between 30 to 120.
selected_contents = [[MIR_indexes[i],contents] for i,contents in enumerate(MIR_contents) if 30<=len(contents)<=120]

#Processing selected MIR contents and generate index:contents dictionary
for i,contents in enumerate(selected_contents):
    selected_contents[i][1] = ''.join(contents[1].replace('\n','').replace('\u3000',' ').split())

selected_contents_dic = {contents[0]:contents[1] for contents in selected_contents}

# Wrong medication reports selection
with open(wmr_indexes_file_path,'r') as f:
    WMR_indexes = [line.split()[1] for line in f.read().splitlines()]

# Output file path certification
if not os.path.exists(output_path):
    print('Path {} is not exist'.format(output_path))

# .txt file generation for corresponding .ann file
exist_txt_num = sum([1 for file_name in os.listdir(output_path) if 'txt' in file_name])

for i,index in enumerate(WMR_indexes):
    i += exist_txt_num + 1
    if 0 <= i <= 9:
        wmr_file_name = output_path + '000' + str(i) + '.txt'
    elif 10 <= i <= 99:
        wmr_file_name = output_path + '00' + str(i) + '.txt'
    elif 100 <= i <= 999:
        wmr_file_name = output_path + '0' + str(i) + '.txt'
    else:
        print('Total number of txt files in {} is more than 1000'.format(output_path))
        
    with open(wmr_file_name,'w') as f:
        contents = selected_contents_dic[index].rstrip('。') + '。'
        bracket_texts = re.findall(r'「.*?」',contents)
        
        if bracket_texts != []:
            for text in bracket_texts:
                contents = re.sub(text,'BRACKET',contents)
            
            splitted_contents = contents.split('。')
            
            for j,sentence in enumerate(splitted_contents):
                if 'BRACKET' in sentence:
                    for k in range(len(re.findall('BRACKET',sentence))):
                        splitted_contents[j]  = re.sub('BRACKET',bracket_texts.pop(0),sentence)
            
            contents = splitted_contents[:-1]
        
        else:
            contents = contents.split('。')[:-1]
            
        for sentence in contents:
            f.write(sentence+'。'+'\n')

print('All {} txt files are generated in {}'.format(len(WMR_indexes),output_path))