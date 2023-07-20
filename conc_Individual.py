from myimports import *

class ConcIndi:
    def __init__(self, conc_folder):
        self.conc_folder = conc_folder
        self.conc_list = []
        self.hist_list = []
        
    
    def fill_img_data(self, img_path):
        self.img_dict = {}
        # Name
        self.img_dict['Name'] = os.path.basename(img_path)
        # Path
        self.img_dict['Path'] = img_path

        # calculate histograms
        # read BGR image
        channel_dict = {}
        BGR_img = cv2.imread(img_path)
        # split BGR channels
        channel_dict['B'],channel_dict['G'],channel_dict['R'] = cv2.split(BGR_img)
        # convert to HSV image
        HSV_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2HSV)
        # split HSV channels
        channel_dict['H'],channel_dict['S'],channel_dict['V'] = cv2.split(HSV_img)
        # convert to Lab image
        Lab_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2Lab)
        # split Lab channels
        channel_dict['L'],channel_dict['a'],channel_dict['b'] = cv2.split(Lab_img)
        
        spaces = ['BGR', 'HSV', 'Lab']
        # BGR channel histograms
        self.hist_dict = {}
        peaks_dict = {}
        peak_pxls = {}
        for space in spaces:
            for key in space:
                self.hist_dict[key] = cv2.calcHist([channel_dict[key]], [0], None, [256], [0, 256])
                # peaks
                peaks_dict[key] = np.argmax(self.hist_dict[key])
                # pixels at peaks
                peak_pxls[key] = int(self.hist_dict[key][peaks_dict[key]])
        self.img_dict['Peaks'], self.img_dict['pkPxls'] = peaks_dict, peak_pxls


        return self.img_dict
    
    def img_iter(self):
        for img_name in os.listdir(self.conc_folder):
            image_path = os.path.join(self.conc_folder, img_name)
            dict_call = self.fill_img_data(image_path)
            self.conc_list.append(self.img_dict)
            # creating histogram list
            self.hist_list.append(self.hist_dict)
