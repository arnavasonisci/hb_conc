from conc_Individual import *
  
date_path = input('Enter the folder path: ') # this has to be user input.
date_path = r'{}'.format(date_path)

# sorted
sorted_conc_folders = sorted(os.listdir(date_path), key=lambda x: float(x))
# this will store the data of ALL concentrations
flat_dicts = []

for subfolder_name in sorted_conc_folders:
    conc_folder_path = os.path.join(date_path, subfolder_name)
    conc = ConcIndi(conc_folder_path)
    conc.img_iter()
    for id in conc.conc_list:
        flat_dict = flatdict.FlatDict(id, delimiter='_') #single flatten
        flat_dicts.append(flat_dict) #multiple

df = pd.DataFrame(flat_dicts)
    
df['Date'] = dt.date.today() # replace this with today's date
new = df['Name'].str.split('_', n=-1, expand=True)
df['Conc'] = new[0]
df['#Image'] = new[1]
df.drop(columns=['Name'], inplace=True)

cols = [
        'Date',
        'Conc',
        '#Image',
        'Path',
        'Peaks_B',
        'Peaks_G',
        'Peaks_R',
        'Peaks_H',
        'Peaks_S',
        'Peaks_V',
        'Peaks_L',
        'Peaks_a',
        'Peaks_b',
        'pkPxls_B',
        'pkPxls_G',
        'pkPxls_R',
        'pkPxls_H',
        'pkPxls_S',
        'pkPxls_L',
        'pkPxls_V',
        'pkPxls_a',
        'pkPxls_b'
    ]

df = df[cols]

# check iloc and loc 
avg_vals_total = {}
columns = df.columns
for conc in df['Conc'].unique():
    avg_vals = {}
    df_temp = df.loc[df['Conc'] == conc]

    for column in columns:
        if 'Peaks' in column:
            avg_vals[f'{column}_avg'] = df_temp[column].mean()
    avg_vals_total[conc] = avg_vals

avg_vals_total_df = pd.DataFrame(avg_vals_total)
print(avg_vals_total_df)
avg_vals_total_df = avg_vals_total_df.transpose()
avg_vals_total_df['Conc'] = avg_vals_total_df.index

avg_cols = list(avg_vals_total_df.columns)
avg_cols.pop()
cols_new = ['Conc']
for ele in avg_cols:
    cols_new.append(ele)

avg_vals_total_df = avg_vals_total_df.reindex(columns=cols_new)

print(avg_vals_total_df)
# df.to_csv(r'F:\Projects\MyLab\HGB_conc\Data\temp\temp_data_date.csv')
# print('Hellooooo\n\n', df.columns)
# print('success')