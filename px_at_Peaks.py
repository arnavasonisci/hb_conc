from main2 import *

PB69 = conc_1.conc_list[0]['Peaks']['B']
PG69 = conc_1.conc_list[0]['Peaks']['G']
PR69 = conc_1.conc_list[0]['Peaks']['R']

PH69 = conc_1.conc_list[0]['Peaks']['H']
PS69 = conc_1.conc_list[0]['Peaks']['S']
PV69 = conc_1.conc_list[0]['Peaks']['V']

PL69 = conc_1.conc_list[0]['Peaks']['L']
Pa69 = conc_1.conc_list[0]['Peaks']['a']
Pb69 = conc_1.conc_list[0]['Peaks']['b']

# print(conc_1.hist_dict)

print('B channel pixels')
print(conc_1.hist_list[0]['B'][PB69])
print(conc_2.hist_list[0]['B'][PB69])
print(conc_3.hist_list[0]['B'][PB69])
print(conc_4.hist_list[0]['B'][PB69])
print(conc_5.hist_list[0]['B'][PB69])

print('G channel pixels')
print(conc_1.hist_list[0]['G'][PG69])
print(conc_2.hist_list[0]['G'][PG69])
print(conc_3.hist_list[0]['G'][PG69])
print(conc_4.hist_list[0]['G'][PG69])
print(conc_5.hist_list[0]['G'][PG69])

print('S channel pixels')
print(conc_1.hist_list[0]['S'][PS69])
print(conc_2.hist_list[0]['S'][PS69])
print(conc_3.hist_list[0]['S'][PS69])
print(conc_4.hist_list[0]['S'][PS69])
print(conc_5.hist_list[0]['S'][PS69])