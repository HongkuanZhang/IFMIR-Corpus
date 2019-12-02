import pandas as pd
import re
import os

# Reading csv file

csv_name = 'MedicalReportPub.csv'
MIR_contents = list(pd.read_csv(csv_name,encoding='SHIFT_JIS',index_col=False)['事故の内容.1'])
MIR_indexes = list(pd.read_csv(csv_name,encoding='SHIFT_JIS',index_col=False)['事例ID'])

# Selecting MIR whose number of character between 30 to 120.
selected_MIR = [[MIR_indexes[index],i] for index,i in enumerate(MIR_contents) if 30<=len(i)<=120]

#Pre-processing selected MIR and generate index:reports dictionary
for i,mir in enumerate(selected_MIR):
    selected_MIR[i][1] = ''.join(mir[1].replace('\n','').replace('\u3000',' ').split())

selected_MIR_dic = {}
for MIR in selected_MIR:
    selected_MIR_dic[MIR[0]] = MIR[1]

# Wrong medication reports selection
WMR_indexes = []
with open('WMR_indexes.txt','r') as f:
    indexes = f.readlines()
    for index in indexes:
        WMR_indexes.append(index.split()[1])

# Output file path certification
current_path = os.getcwd()
target_path = current_path + os.path.sep + 'samples'
if not os.path.exists(target_path):
    print('The samples file is not exist')

# .txt file generation for corresponding .ann file
for i,index in enumerate(WMR_indexes):
    wmr_file_name = 'samples/' + str(i) + '.txt'
    with open(wmr_file_name,'w') as f:
        for sentence in selected_MIR_dic[index].split('。'):
            f.write(sentence+'\n')

print('All 49 txt files are generated in /samples')
