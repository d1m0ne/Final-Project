from numpy.core.numeric import NaN
import math
import pandas
import numpy as np
import matplotlib.pyplot as plt

covid_polls = "https://raw.githubusercontent.com/mlepinski/Python-Worksheets/master/Matplotlib/Data/covid_concern_polls.csv"
covid_approval_polls = "https://raw.githubusercontent.com/mlepinski/Python-Worksheets/master/Matplotlib/Data/covid_approval_polls.csv"

covid_poll_data = pandas.read_csv(covid_polls)
covid_poll_approval = pandas.read_csv(covid_approval_polls)

dates = []

approve = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

disapprove = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

sample_size = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range (len(covid_poll_approval.index)):
    if (covid_poll_approval["party"][i] == "R") and ((math.isnan(covid_poll_approval["sample_size"][i])) is not True):
        poll_date = covid_poll_approval["end_date"][i]
        approve_per = covid_poll_approval["approve"][i]
        disapprove_per = covid_poll_approval["disapprove"][i]
        current_sample_size = covid_poll_approval["sample_size"][i]
        if math.isnan(approve_per):
            approve_per = 0
        if math.isnan(disapprove_per):
            disapprove_per = 0
        month = int(str(poll_date[5] + poll_date[6]))
        sample_size[month - 1] = int(current_sample_size + sample_size[month - 1])
        approve[month - 1] = int(((approve_per * current_sample_size) / 100) + approve[month - 1])
        disapprove[month - 1] = int(((int(disapprove_per) * int(current_sample_size)) / 100)  + int(disapprove[month - 1]))

for i in range(12):
    if sample_size[i] != 0:
        approve[i] = approve[i]/sample_size[i]
        disapprove[i] = disapprove[i]/sample_size[i]

N = 12

ind = np.arange(N) 
width = 0.35       
plt.bar(ind, approve, width, label='App')
plt.bar(ind + width, disapprove, width, label='Dis')
plt.xlabel('Month')
plt.ylabel('percentage of population')
plt.title('Approval Vs Disapproval by month: Republican')

plt.xticks(ind + width / 2, ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
plt.legend(loc='best')
print(plt.show())