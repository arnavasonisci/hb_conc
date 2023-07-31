from myimports import *

# give date dir path
date_folder = r"F:\Projects\MyLab\HGB_conc\28_July"

for conc in os.listdir(date_folder):
    # concentration subfolder path
    conc_folder = os.path.join(date_folder, conc) #created the paths for subfolders
    print(conc)
    count = 1
    for img in os.listdir(conc_folder):
        print(img)
        # get existing image path in conc folder
        img_path = os.path.join(conc_folder, img)
        # create new name for image
        new_img_name = f'{conc}_{count}.jpg'
        # create intended image path
        renamed_img_path = os.path.join(conc_folder, new_img_name)
        # rename image to intended path
        os.rename(img_path, renamed_img_path)
        count += 1
        print('success')