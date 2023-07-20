from myimports import *

class Conc:
    def __init__(self, conc_folder):
        self.conc_folder = conc_folder  # the folder made for the concentration
        # making list of images in the folder
        self.conc_img_list = [os.path.join(
            self.conc_folder, img) for img in os.listdir(self.conc_folder)]
        # layered image of the concentration
        self.layered_img = None
        # the different histograms
        self.bgr_histograms = None
        self.hsv_histograms = None
        self.lab_histograms = None
        # area under curve variables
        self.bgr_auc = None
        self.hsv_auc = None
        self.lab_auc = None
        # dictionaries
        self.bgr_histograms_dic = None
        self.hsv_histograms_dic = None
        self.lab_histograms_dic = None
        # peak values
        self.bgr_peaks = None
        self.hsv_peaks = None
        self.lab_peaks = None
        # peakPixels
        self.bgr_peak_pxl = None
        self.hsv_peak_pxl = None
        self.lab_peak_pxl = None
        # peakAt
        self.peaksAt = None

    # creating a function to make the layered images
    def layerMaking(self):
        # create a blank canvas
        result = np.zeros(cv2.imread(
            self.conc_img_list[0]).shape, dtype=np.uint8)
        alpha = 0.1
        for img in self.conc_img_list:
            result = cv2.addWeighted(cv2.imread(img), alpha, result, 1-alpha, 0)
        # result = cv2.resize(result, (int((result.shape[1])*0.2), int((result.shape[0])*0.2)), interpolation=cv2.INTER_AREA)
        self.layered_img = result
        print('layerMaking success')

    # calculate the histograms
    def calculateHist(self):
        # splitting the BGR channels
        bgr_channels = cv2.split(self.layered_img)
        print('bgr_channels success')
        # converting from BGR to HSV
        HSV_img = cv2.cvtColor(self.layered_img, cv2.COLOR_BGR2HSV)
        print('HSV conversion success')
        # splitting the HSV channels
        hsv_channels = cv2.split(HSV_img)
        print('hsv_channels success')
        # converting BGR to LAB
        LAB_img = cv2.cvtColor(self.layered_img, cv2.COLOR_BGR2Lab)
        # splitting the LAB channels
        lab_channels = cv2.split(LAB_img)

        self.bgr_histograms = [cv2.calcHist([channel], [0], None, [256], [0, 256]) for channel in bgr_channels]
        self.bgr_histograms_dic = {
                            'B': self.bgr_histograms[0],
                            'G': self.bgr_histograms[1],
                            'R': self.bgr_histograms[2]
                        }
        
        self.hsv_histograms = [cv2.calcHist([channel], [0], None, [256], [0, 256]) for channel in hsv_channels]
        self.hsv_histograms_dic = {
                            'H': self.hsv_histograms[0],
                            'S': self.hsv_histograms[1],
                            'V': self.hsv_histograms[2]
                        }
        
        self.lab_histograms = [cv2.calcHist([channel], [0], None, [256], [0, 256]) for channel in lab_channels]
        self.lab_histograms_dic = {
                            'L': self.lab_histograms[0],
                            'A': self.lab_histograms[1],
                            'B': self.lab_histograms[2]
                        }
        
        # area under the curve
        self.bgr_auc = [int(np.sum(histogram*255)) for histogram in self.bgr_histograms]
        print(f'Area under the curve for\nB:{self.bgr_auc[0]}\nG: {self.bgr_auc[1]}\nR: {self.bgr_auc[2]}')

        self.hsv_auc = [int(np.sum(histogram*255)) for histogram in self.hsv_histograms]
        print(f'Area under the curve for\nH:{self.hsv_auc[0]}\nS: {self.hsv_auc[1]}\nV: {self.hsv_auc[2]}')

        self.lab_auc = [int(np.sum(histogram*255)) for histogram in self.lab_histograms]
        print(f'Area under the curve for\nL:{self.lab_auc[0]}\nA: {self.lab_auc[1]}\nB: {self.lab_auc[2]}')

    # to find the BGR and HSV peak values
    def findPeaks(self):
        self.bgr_peaks = [np.argmax(histogram) for histogram in self.bgr_histograms]
        self.hsv_peaks = [np.argmax(histogram) for histogram in self.hsv_histograms]
        self.lab_peaks = [np.argmax(histogram) for histogram in self.lab_histograms]
        return self.bgr_peaks, self.hsv_peaks, self.lab_peaks

    # to find the number of pixels at the peak values
    def peakPixels(self):
        self.bgr_peak_pxl = [int(self.bgr_histograms[i][self.bgr_peaks[i]]) for i in range(3)]
        print(f'number of pixels at the BGR peaks are:\nB: {self.bgr_peak_pxl[0]}\nG: {self.bgr_peak_pxl[1]}\nR: {self.bgr_peak_pxl[2]}')
        self.hsv_peak_pxl = [int(self.hsv_histograms[i][self.hsv_peaks[i]]) for i in range(3)]
        print(f'number of pixels at the HSV peaks are:\nH: {self.hsv_peak_pxl[0]}\nS: {self.hsv_peak_pxl[1]}\nV: {self.hsv_peak_pxl[2]}')
        self.lab_peak_pxl = [int(self.lab_histograms[i][self.lab_peaks[i]]) for i in range(3)]
        print(f'number of pixels at the LAB peaks are:\nL: {self.lab_peak_pxl[0]}\nA: {self.lab_peak_pxl[1]}\nB: {self.lab_peak_pxl[2]}')

    # to find the number of pixels available on the peak value of the least concentration
    def peakAt(self, xbgr, xhsv, xlab):
        self.peaksAt = {
            'B': int(self.bgr_histograms[0][xbgr[0]]),
            'G': int(self.bgr_histograms[1][xbgr[1]]),
            'R': int(self.bgr_histograms[2][xbgr[2]]),
            'H': int(self.hsv_histograms[0][xhsv[0]]),
            'S': int(self.hsv_histograms[1][xhsv[1]]),
            'V': int(self.hsv_histograms[2][xhsv[2]]),
            'L': int(self.lab_histograms[0][xlab[0]]),
            'a': int(self.lab_histograms[1][xlab[1]]),
            'b': int(self.lab_histograms[2][xlab[2]])
            }
        print(self.peaksAt)
        print('\n\n\n\n')

