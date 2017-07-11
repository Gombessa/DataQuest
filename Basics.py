
# coding: utf-8

# In[1]:


import csv

f = open("guns.csv")
data = list(csv.reader(f))
print(data[:5])


# In[2]:


headers = data[0]
data = data[1:]
print(headers)
print(data[:5])


# In[3]:


years = []
for deaths in data:
    years.append(deaths[1])
year_counts = {}
for year in years:
    year_counts[year] = year_counts.get(year, 0) + 1
print(year_counts)


# In[4]:


import datetime
dates = []
for deaths in data:
    dates.append(datetime.datetime(year = int(deaths[1]), month = int(deaths[2]), day = 1))
print(dates[:5])
date_counts = {}
for date in dates:
    date_counts[date] = date_counts.get(date, 0) + 1
print(date_counts)


# In[5]:


sex_counts = {}
race_counts = {}
for deaths in data:
    sex_counts[deaths[5]] = sex_counts.get(deaths[5], 0) + 1
    race_counts[deaths[7]] = race_counts.get(deaths[7], 0) + 1
print(race_counts)
print(sex_counts)



# Things learned: gun deaths are predominantly male, and the most are white; however, it would be interesting to see how many are suicide vs homicide, and the homicide rate by rate.

# In[6]:


f2 = open("census.csv")
census = list(csv.reader(f2))
print(census)


# In[12]:


mapping = {}
for key in race_counts:
    if key == 'Asian/Pacific Islander':
        mapping[key] = int(census[1][14]) + int(census[1][15])
    elif key == 'Black':
        mapping[key] = int(census[1][12])
    elif key == 'Native American/Native Alaskan':
        mapping[key] = int(census[1][13])
    elif key == 'Hispanic':
        mapping[key] = int(census[1][11])
    elif key == 'White':
        mapping[key] = int(census[1][10])
    else:
        print('I done goofed')
race_per_hundredk = {}
for key in race_counts:
    race_per_hundredk[key] = race_counts[key] / mapping[key] * 100000
print(race_per_hundredk)


# In[14]:


intents = [i[3] for i in data]
races = [i[7] for i in data]
homicide_race_counts = {}
for i, race in enumerate(races):
    if intents[i] == 'Homicide':
        homicide_race_counts[race] = homicide_race_counts.get(race, 0) + 1
homicide_race_per_hundredk = {}
for key in homicide_race_counts:
    homicide_race_per_hundredk[key] = homicide_race_counts[key] / mapping[key] * 100000
print(homicide_race_per_hundredk)


# The murder rate for blacks is 4x as high as the next highest rate, hispanics, which are almost 3x as likely to die of homicide than a white person.  
# 
# I'd like to further pursue the data by taking both age and sex into account.

# In[ ]:




