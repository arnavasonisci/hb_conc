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
    return master_df
