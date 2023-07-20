from Conc import *
import historgrams

# folder paths of different concentrations
conc_1_path = r'F:\Projects\MyLab\HGB_conc\22 June\5.4'
conc_2_path = r'F:\Projects\MyLab\HGB_conc\22 June\9.5'
conc_3_path = r'F:\Projects\MyLab\HGB_conc\22 June\11.1'
conc_4_path = r'F:\Projects\MyLab\HGB_conc\22 June\13.9'
conc_5_path = r'F:\Projects\MyLab\HGB_conc\22 June\15.1'

# 5.4
conc_54 = Conc(r'F:\Projects\MyLab\HGB_conc\22 June\5.4')
conc_54.layerMaking()
conc_54.calculateHist()
bgr_peaks_54, hsv_peaks_54, lab_peaks_54 = conc_54.findPeaks()
print('5.4 peaks: ', bgr_peaks_54, hsv_peaks_54, lab_peaks_54)
conc_54.peakPixels()
conc_54.peakAt(bgr_peaks_54, hsv_peaks_54, lab_peaks_54)

# peakAt arguments for other concentrations
peakAt_bgr_arg = bgr_peaks_54
peakAt_hsv_arg = hsv_peaks_54
peakAt_lab_arg = lab_peaks_54

print('--------------', peakAt_bgr_arg, peakAt_hsv_arg, peakAt_lab_arg)
# 9.5
conc_95 = Conc(r'F:\Projects\MyLab\HGB_conc\22 June\9.5')
conc_95.layerMaking()
conc_95.calculateHist()
bgr_peaks_95, hsv_peaks_95, lab_peaks_95 = conc_95.findPeaks()
print('9.5 peaks: ' ,bgr_peaks_95, hsv_peaks_95, lab_peaks_95)
conc_95.peakPixels()
conc_95.peakAt(peakAt_bgr_arg, peakAt_hsv_arg, peakAt_lab_arg)


# 11.1
conc_111 = Conc(r'F:\Projects\MyLab\HGB_conc\22 June\11.1')
conc_111.layerMaking()
conc_111.calculateHist()
bgr_peaks_111, hsv_peaks_111, lab_peaks_111 = conc_111.findPeaks()
print('11.1 peaks: ', bgr_peaks_111, hsv_peaks_111, lab_peaks_111)
conc_111.peakPixels()
conc_111.peakAt(peakAt_bgr_arg, peakAt_hsv_arg, peakAt_lab_arg)


# 13.9
conc_139 = Conc(r'F:\Projects\MyLab\HGB_conc\22 June\13.9')
conc_139.layerMaking()
conc_139.calculateHist()
bgr_peaks_139, hsv_peaks_139, lab_peaks_139 = conc_139.findPeaks()
print('13.9 peaks: ', bgr_peaks_139, hsv_peaks_139, lab_peaks_139)
conc_139.peakPixels()
conc_139.peakAt(peakAt_bgr_arg, peakAt_hsv_arg, peakAt_lab_arg)


# 15.1
conc_151 = Conc(r'F:\Projects\MyLab\HGB_conc\22 June\15.1')
conc_151.layerMaking()
conc_151.calculateHist()
bgr_peaks_151, hsv_peaks_151, lab_peaks_151 = conc_151.findPeaks()
print('15.1 peaks: ', bgr_peaks_151, hsv_peaks_151, lab_peaks_151)
conc_151.peakPixels()
conc_151.peakAt(peakAt_bgr_arg, peakAt_hsv_arg, peakAt_lab_arg)
# cv2.waitKey(0)

# plot
plt.figure()

plt.subplot(2, 5, 1)
plt.plot(conc_54.bgr_histograms[0], color='b', label="B")
plt.plot(conc_54.bgr_histograms[1], color='g', label="G")
plt.plot(conc_54.bgr_histograms[2], color='r', label="R")
plt.title('BGR 5.4')
plt.legend()

plt.subplot(2, 5, 2)
plt.plot(conc_95.bgr_histograms[0], color='b', label="B")
plt.plot(conc_95.bgr_histograms[1], color='g', label="G")
plt.plot(conc_95.bgr_histograms[2], color='r', label="R")
plt.title('BGR 9.5')
plt.legend()

plt.subplot(2, 5, 3)
plt.plot(conc_111.bgr_histograms[0], color='b', label="B")
plt.plot(conc_111.bgr_histograms[1], color='g', label="G")
plt.plot(conc_111.bgr_histograms[2], color='r', label="R")
plt.title('BGR 11.1')
plt.legend()


plt.subplot(2, 5, 4)
plt.plot(conc_139.bgr_histograms[0], color='b', label="B")
plt.plot(conc_139.bgr_histograms[1], color='g', label="G")
plt.plot(conc_139.bgr_histograms[2], color='r', label="R")
plt.title('BGR 13.9')
plt.legend()

plt.subplot(2, 5, 5)
plt.plot(conc_151.bgr_histograms[0], color='b', label="B")
plt.plot(conc_151.bgr_histograms[1], color='g', label="G")
plt.plot(conc_151.bgr_histograms[2], color='r', label="R")
plt.title('BGR 15.1')
plt.legend()

plt.subplot(2, 5, 6)
plt.plot(conc_54.hsv_histograms[0], color='k', label="H")
plt.plot(conc_54.hsv_histograms[1], color='c', label="S")
plt.plot(conc_54.hsv_histograms[2], color='m', label="V")
plt.title('HSV 5.4')
plt.legend()

plt.subplot(2, 5, 7)
plt.plot(conc_95.hsv_histograms[0], color='k', label="H")
plt.plot(conc_95.hsv_histograms[1], color='c', label="S")
plt.plot(conc_95.hsv_histograms[2], color='m', label="V")
plt.title('HSV 9.5')
plt.legend()


plt.subplot(2, 5, 8)
plt.plot(conc_111.hsv_histograms[0], color='k', label="H")
plt.plot(conc_111.hsv_histograms[1], color='c', label="S")
plt.plot(conc_111.hsv_histograms[2], color='m', label="V")
plt.title('HSV 11.1')
plt.legend()

plt.subplot(2, 5, 9)
plt.plot(conc_139.hsv_histograms[0], color='k', label="H")
plt.plot(conc_139.hsv_histograms[1], color='c', label="S")
plt.plot(conc_139.hsv_histograms[2], color='m', label="V")
plt.title('HSV 13.9')
plt.legend()

plt.subplot(2, 5, 10)
plt.plot(conc_151.hsv_histograms[0], color='k', label="H")
plt.plot(conc_151.hsv_histograms[1], color='c', label="S")
plt.plot(conc_151.hsv_histograms[2], color='m', label="V")
plt.title('HSV 15.1')
plt.legend()

# csv preparation
conc_list = [54, 95, 111, 139, 151]
conc_obj = [conc_54, conc_95, conc_111, conc_139, conc_151]
spaces = {
    "BGR": ["B","G","R"],
    'HSV': ['H', 'S', 'V'],
    'LAB': ['L', 'a', 'b']
}
i = 0
conc_dict = {}
my_dict = {}

for con in conc_list:

    for space, channel in spaces.items():
        for j in range(len(channel)):
            if "BGR" in space:
                key_val_x = 'P'+channel[j]+'x'
                key_val_y = 'P'+channel[j]+'y'
                key_val_auc = 'auc'+channel[j]
                
                try:
                    my_dict[key_val_x].append(conc_obj[i].bgr_peaks[j])
                    my_dict[key_val_y].append(conc_obj[i].bgr_peak_pxl[j])
                    my_dict[key_val_auc].append(conc_obj[i].bgr_auc[j])
                    
                except:
                    my_dict[key_val_x] = [conc_obj[i].bgr_peaks[j]]
                    my_dict[key_val_y] = [conc_obj[i].bgr_peak_pxl[j]]
                    my_dict[key_val_auc]= [conc_obj[i].bgr_auc[j]]
                    
            elif 'HSV' in space:
                key_val_x = 'P'+channel[j]+'x'
                key_val_y = 'P'+channel[j]+'y'
                key_val_auc = 'auc'+channel[j]
                
                try:
                    my_dict[key_val_x].append(conc_obj[i].hsv_peaks[j])
                    my_dict[key_val_y].append(conc_obj[i].hsv_peak_pxl[j])
                    my_dict[key_val_auc].append(conc_obj[i].hsv_auc[j])
                except:
                    my_dict[key_val_x] = [conc_obj[i].hsv_peaks[j]]
                    my_dict[key_val_y] = [conc_obj[i].hsv_peak_pxl[j]]
                    my_dict[key_val_auc]= [conc_obj[i].hsv_auc[j]]
            else:
                key_val_x = 'P'+channel[j]+'x'
                key_val_y = 'P'+channel[j]+'y'
                key_val_auc = 'auc'+channel[j]
                
                try:
                    my_dict[key_val_x].append(conc_obj[i].lab_peaks[j])
                    my_dict[key_val_y].append(conc_obj[i].lab_peak_pxl[j])
                    my_dict[key_val_auc].append(conc_obj[i].lab_auc[j])
                except:
                    my_dict[key_val_x] = [conc_obj[i].lab_peaks[j]]
                    my_dict[key_val_y] = [conc_obj[i].lab_peak_pxl[j]]
                    my_dict[key_val_auc]= [conc_obj[i].lab_auc[j]]
    i += 1
print('\n\n\n\n')

channels = ['B', 'G', 'R', 'H', 'S', 'V', 'L', 'a', 'b']
peak_dict = {}

for i in range(len(conc_obj)):
    for channel in channels:
        try:
            peak_dict[f'px_5.4p_{channel}'].append(conc_obj[i].peaksAt[channel])
        except:
            peak_dict[f'px_5.4p_{channel}'] = [conc_obj[i].peaksAt[channel]]

my_dict_final = my_dict | peak_dict 
# print(my_dict_final)

df = pd.DataFrame(my_dict_final)
print(df)
# df.to_csv(r'C:\Users\arnav\OneDrive\Desktop\hgb_layer_final.csv')

plt.show()