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

very = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

somewhat = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

not_very = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

not_at_all = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

sample_size = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range (len(covid_poll_data.index)):
    if (covid_poll_data["subject"][i] == "concern-infected") and ((math.isnan(covid_poll_data["sample_size"][i])) is not True):
        poll_date = covid_poll_data["end_date"][i]
        very_per = covid_poll_data["very"][i]
        somewhat_per = covid_poll_data["somewhat"][i]
        not_very_per = covid_poll_data["not_very"][i]
        not_at_all_per = covid_poll_data["not_at_all"][i]
        current_sample_size = covid_poll_data["sample_size"][i]
        if math.isnan(very_per):
            very_per = 0
        if math.isnan(somewhat_per):
            somewhat_per = 0
        if math.isnan(not_very_per):
            not_very_per = 0
        if math.isnan(not_at_all_per):
            not_at_all_per = 0
        month = int(str(poll_date[5] + poll_date[6]))
        sample_size[month - 1] = int(current_sample_size + sample_size[month - 1])
        very[month - 1] = int(((very_per * current_sample_size) / 100) + very[month - 1])
        somewhat[month - 1] = int(((somewhat_per * current_sample_size) / 100) + somewhat[month - 1])
        not_very[month - 1] = int(((not_very_per * current_sample_size) / 100) + not_very[month - 1])
        not_at_all[month - 1] = int(((not_at_all_per * current_sample_size) / 100) + not_at_all[month - 1])

for i in range(12):
    if sample_size[i] != 0:
        very[i] = very[i]/sample_size[i]
        somewhat[i] = somewhat[i]/sample_size[i]
        not_very[i] = not_very[i]/sample_size[i]
        not_at_all[i] = not_at_all[i]/sample_size[i]

N = 12

ind = np.arange(N) 
width = 0.25    
plt.bar(ind, very, width, label='Very')
plt.bar(ind + width, somewhat, width, label='Somewhat')
plt.bar(ind + (width * 2), not_very, width, label='Not very')
plt.bar(ind + (width * 3), not_at_all, width, label='Not at all')
plt.xlabel('Month')
plt.ylabel('percentage of population')
plt.title('Concern levels for infected')

plt.xticks(ind + width / 2, ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
plt.legend(loc='best')
print(plt.show())