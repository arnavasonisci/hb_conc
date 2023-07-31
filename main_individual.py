from conc_Individual import *

# enter path where the different concentrations are available.
date_path = r"F:\Projects\MyLab\HGB_conc\28_July" # this has to be user input. 

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

# df.to_csv(r'F:\Projects\MyLab\HGB_conc\Data\temp\temp_data_date.csv')
# print('Hellooooo\n\n', df.columns)
# print('success')