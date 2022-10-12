from array import array
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta
import numpy as np
import copy

# Importing .csv to a dataframe
members_df = pd.read_csv('C:\\Users\\hugom\\Data Frolicking\\portuguese_ar_member_data\\portuguese_ar_member_data\\outputs\\members.csv')
members_df['DOB'] = pd.to_datetime(members_df['DOB'])

# 
legis_elecdate = pd.DataFrame([pd.to_datetime('1975-04-25'),
                  pd.to_datetime('1976-04-25'),
                  pd.to_datetime('1980-10-05'),
                  pd.to_datetime('1983-04-25'),
                  pd.to_datetime('1985-10-06'),
                  pd.to_datetime('1987-07-19'),
                  pd.to_datetime('1991-10-06'),
                  pd.to_datetime('1995-10-01'),
                  pd.to_datetime('1999-10-10'),
                  pd.to_datetime('2002-03-17'),
                  pd.to_datetime('2005-02-20'),
                  pd.to_datetime('2009-09-27'),
                  pd.to_datetime('2011-06-05'),
                  pd.to_datetime('2015-10-04'),
                  pd.to_datetime('2019-10-06'),
                  pd.to_datetime('2022-01-30')])

# List of legislatures
legis_df = members_df.columns[2::3]

# Init data structures of dataframes
legis_member_df = []
legis_party_df = []
legis = ''
legis_member_perparty_df = []
legis_sum_perparty_df = []

for i in range(len(legis_df)):
    legis = legis_df[i]

    # Df of members in the legislature
    legis_member_df.append(members_df[members_df[f'{legis}']==1].filter(items=['Name', 'DOB', f'{legis}', f'{legis} Party', f'{legis} District']))

    # Condensing 'Independentes' in df of members in the legislature
    legis_member_df[i].loc[legis_member_df[i][f'{legis} Party'].str.contains('Independente'), f'{legis} Party'] = 'Independente'

    # Df of parties in the legislature
    legis_party_df.append(legis_member_df[i].drop_duplicates(subset=[f'{legis} Party'])[f'{legis} Party'])

    # Dividing dfs per party and creating sum of members
    member_perparty_df = []
    sum_perparty_df = []
    for j in range(len(legis_party_df[i])):
        member_perparty_df.append(legis_member_df[i][legis_member_df[i][f'{legis} Party']==legis_party_df[i].iloc[j]])
        sum_perparty_df.append(len(member_perparty_df[j]))

    legis_member_perparty_df.append(member_perparty_df)
    legis_sum_perparty_df.append(sum_perparty_df)
    
    # Average DOB

    # Plotting
    #fig, plot = plt.subplots()

    #plot.bar(legis_party_df[i], legis_sum_perparty_df[i])
    #plt.show()



# Create list of dataframes with dob and age per legislature per party
legis_dob_perparty_df = copy.deepcopy(legis_member_perparty_df)
legis_age_perparty = [[[] for j in range(len(legis_member_perparty_df[i]))] for i in range(len(legis_member_perparty_df))]
for i in range(len(legis_member_perparty_df)):
    for j in range(len(legis_member_perparty_df[i])):
        # Drop rows without DOB
        legis_dob_perparty_df[i][j] = legis_dob_perparty_df[i][j]['DOB'].dropna()

        # Transform DOB to age at time of election
        for k in range(len(legis_dob_perparty_df[i][j])):
            legis_age_perparty[i][j].append(legis_elecdate.iloc[i,0]-legis_dob_perparty_df[i][j].iloc[k])
            legis_age_perparty[i][j][k] = legis_age_perparty[i][j][k].to_numpy()/ np.timedelta64(1, 'D')

# Drop parties that had no DOB at all
for i in range(len(legis_age_perparty[i])):
    legis_age_perparty[i] = [j for j in legis_age_perparty[i] if j]

# List of average age per legislature per party
legis_ageav_perparty = [[[] for j in range(len(legis_age_perparty[i]))] for i in range(len(legis_age_perparty))]
for i in range(len(legis_age_perparty)):
    for j in range(len(legis_age_perparty[i])):
        legis_ageav_perparty[i][j] = np.mean(legis_age_perparty[i][j])/365



# Create list of dataframes with dob and age per legislature
legis_dob_df = copy.deepcopy(legis_member_df)
legis_age = [[] for i in range(len(legis_member_df))]
for i in range(len(legis_member_df)):
    # Drop rows without DOB
    legis_dob_df[i] = legis_dob_df[i]['DOB'].dropna()

    # Transform DOB to age at time of election
    for k in range(len(legis_dob_df[i])):
        legis_age[i].append(legis_elecdate.iloc[i,0]-legis_dob_df[i].iloc[k])
        legis_age[i][k] = legis_age[i][k].to_numpy()/ np.timedelta64(1, 'D')

# List of average age per legislature
legis_ageav = [[] for i in range(len(legis_age))]
for i in range(len(legis_ageav)):
    legis_ageav[i] = np.mean(legis_age[i])/365

    # Plotting
    fig, avage_plot = plt.subplots(1)

    legis_party_df_alt = legis_party_df[i].iloc[0:len(legis_ageav_perparty[i])]
    avage_plot.bar(legis_party_df_alt, legis_ageav_perparty[i])
    plt.show()



# Plotting
fig, avage_plot = plt.subplots(1)

avage_plot.bar(legis_df, legis_ageav)
plt.show()

#print(legis_ageav_perparty)
print(legis_ageav)