from myimports import *
import Conc

# to create BGR histograms
def hist_rgb(image): # enter variable that has image path
    # img_read = cv2.cvtColor(img_read, cv2.COLOR_BGR2HSV)
    # splitting into BGR channels
    b, g, r = cv2.split(image)
    hist_b = cv2.calcHist([b],[0],None,[256],[0,256])
    
    hist_g = cv2.calcHist([g],[0],None,[256],[0,256])
    hist_r = cv2.calcHist([r],[0],None,[256],[0,256])
    
    return hist_b, hist_g, hist_r

# Lab histogram
def hist_Lab(image): # enter variable that has image path
    img_Lab = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
    # splitting into Lab channels
    L, a, b = cv2.split(img_Lab)

    hist_L = cv2.calcHist([L],[0],None,[256],[1,255])
    hist_a = cv2.calcHist([a],[0],None,[256],[1,255])
    hist_b = cv2.calcHist([b],[0],None,[256],[1,255])
    
    return hist_L, hist_a, hist_b

# Lab histogram
def hist_hsv(image): # enter variable that has image path
    img_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # splitting into Lab channels
    h, s, v = cv2.split(img_HSV)
    hist_h = cv2.calcHist([h],[0],None,[256],[0, 180]) # range of H is 0 to 180
    hist_s = cv2.calcHist([s],[0],None,[256],[1,255])
    hist_v = cv2.calcHist([v],[0],None,[256],[1,255])
    
    return hist_h, hist_s, hist_v