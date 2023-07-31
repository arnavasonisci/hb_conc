from myimports import *

# give date dir path
date_folder = r"F:\Projects\MyLab\HGB_conc\28_July"

for conc in os.listdir(date_folder):
    # concentration subfolder path
    conc_folder = os.path.join(date_folder, conc) #created the paths for subfolders
    print(conc)
    for img in os.listdir(conc_folder):
        img_path = os.path.join(conc_folder, img)
        img_read = cv2.imread(img_path)

        # get dimensions of images
        height, width = img_read.shape[:2]
        # calculate center coordinates
        cenx, ceny = width//2, height//2

        # calculate crop boundaries
        left = cenx - 900//2
        top = ceny - 900//2
        right = cenx + 900//2
        bottom = ceny + 900//2

        # perform cropping
        cropped_image = img_read[top:bottom, left:right]
        cv2.imwrite(img_path, cropped_image)
print('success')