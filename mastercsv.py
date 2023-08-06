from main_individual import *
import main_individual


def makeMaster():

    # path of master csv
    master_df_path = r'F:\Projects\MyLab\HGB_conc\Data\master.csv'

    if os.path.isfile(master_df_path):
        # read master csv
        master_df = pd.read_csv(master_df_path)
        # print('-----printing master csv\n', master_df.columns, '\n\n')
    else:
        # create a DataFrame for master df
        master_df = pd.DataFrame(columns=main_individual.df.columns)
        # print(master_df.head())
        master_df.to_csv(master_df_path, index=False)
        # print('Checking master_df', master_df.columns, master_df.shape)

    # print('MASTER_DF\n\n\n', master_df.columns, master_df.shape)
    temp_data_df = main_individual.df
    # print('-----temp_data_df\n', temp_data_df.columns, temp_data_df.shape, '\n')
    # print(temp_data_df.head())
    # print(temp_data_df.tail())
    master_df_final = pd.concat(
        [master_df, temp_data_df], ignore_index=True, axis=0)
    master_df_final.drop_duplicates()
    master_df = master_df_final
    print('-----master_df\n', master_df.columns, master_df.shape, '\n')
    print(master_df.head())
    print(master_df.tail())

    master_df.to_csv(master_df_path, index=False)

    avg_vals_total = {}
    columns = master_df.columns
    for conc in master_df['Conc'].unique():
        avg_vals = {}
        master_df_temp = master_df.loc[master_df['Conc'] == conc]

        for column in columns:
            if 'Peaks' in column:
                avg_vals[f'{column}_avg'] = master_df_temp[column].mean()
        avg_vals_total[conc] = avg_vals

    avg_vals_total_df = pd.DataFrame(avg_vals_total)
    avg_vals_total_df = avg_vals_total_df.transpose()
    print(avg_vals_total_df)
    avg_vals_total_df['Conc'] = avg_vals_total_df.index

    avg_cols = list(avg_vals_total_df.columns)
    avg_cols.pop()
    cols_new = ['Conc']
    for ele in avg_cols:
        cols_new.append(ele)

    avg_vals_total_df = avg_vals_total_df.reindex(columns=cols_new)
    avg_vals_total_df = avg_vals_total_df.reset_index(drop=True)
    
    print('Last print call ----------------\n', avg_vals_total_df)
    return master_df, avg_vals_total_df

if __name__ == '__main__':
    mdf, avtdf = makeMaster()