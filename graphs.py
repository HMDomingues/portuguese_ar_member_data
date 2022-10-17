from array import array
from cmath import nan
from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



# Importing .csv to a dataframe
members_df = pd.read_csv('C:\\Users\\hugom\\Data Frolicking\\portuguese_ar_member_data\\portuguese_ar_member_data\\outputs\\members.csv')
members_df['DOB'] = pd.to_datetime(members_df['DOB'])

# 
port_av_age = [28.8, 28.9, 29.6, 30.5, 31.1, 31.9, 33.7, 35.1, 36.4, 37.4, 38.5, 40.1, 41.0, 42.8, 44.4, 45.0]

median_age_years = [1970]

# List of legislatures
legis_df = members_df.columns[2::3]

# Init data structures of dataframes
legis_member_df = []
legis_party_df = []
legis = ''
legis_member_perparty_df = []
legis_sum_perparty_df = []
column_array = [[],[]]
legis_member_ar_data = pd.DataFrame()

for i in range(len(legis_df)):
    legis = legis_df[i]

    # Df of members in the legislature
    legis_member_df.append(members_df[members_df[f'{legis}']==1].filter(items=['Name', 'DOB', f'{legis}', f'{legis} Party', f'{legis} District']))

    # Condensing 'PAN Independentes' to 'PSN' in df of members in the legislature
    legis_member_df[i].loc[legis_member_df[i][f'{legis} Party'].str.contains('PSN até'), f'{legis} Party'] = 'PSN'

    # Condensing 'PAN Independentes' to 'ID' in df of members in the legislature
    legis_member_df[i].loc[legis_member_df[i][f'{legis} Party'].str.contains('ID até'), f'{legis} Party'] = 'ID'

    # Condensing 'PAN Independentes' to 'PPD' in df of members in the legislature
    legis_member_df[i].loc[legis_member_df[i][f'{legis} Party'].str.contains('PPD até'), f'{legis} Party'] = 'PPD'

    # Condensing 'PAN Independentes' to 'PRD' in df of members in the legislature
    legis_member_df[i].loc[legis_member_df[i][f'{legis} Party'].str.contains('PRD até'), f'{legis} Party'] = 'PRD'

    # Condensing 'PAN Independentes' to 'PEV' in df of members in the legislature
    legis_member_df[i].loc[legis_member_df[i][f'{legis} Party'].str.contains('PEV até'), f'{legis} Party'] = 'PEV'

    # Condensing 'PAN Independentes' to 'PAN' in df of members in the legislature
    legis_member_df[i].loc[legis_member_df[i][f'{legis} Party'].str.contains('PAN até'), f'{legis} Party'] = 'PAN'

    # Condensing 'L Independentes' to 'L' in df of members in the legislature
    legis_member_df[i].loc[legis_member_df[i][f'{legis} Party'].str.contains('L até'), f'{legis} Party'] = 'L'

    # Condensing 'PAN Independentes' to 'CDS' in df of members in the legislature
    legis_member_df[i].loc[legis_member_df[i][f'{legis} Party'].str.contains('CDS até'), f'{legis} Party'] = 'CDS'

    # Condensing 'CDS-PP Independentes' to 'CDS-PP' in df of members in the legislature
    legis_member_df[i].loc[legis_member_df[i][f'{legis} Party'].str.contains('CDS-PP até'), f'{legis} Party'] = 'CDS-PP'
    
    # Condensing 'PCP Independentes' to 'PCP' in df of members in the legislature
    legis_member_df[i].loc[legis_member_df[i][f'{legis} Party'].str.contains('PCP até'), f'{legis} Party'] = 'PCP'

    # Condensing 'PS Independentes' to 'PS' in df of members in the legislature
    legis_member_df[i].loc[legis_member_df[i][f'{legis} Party'].str.contains('PS até'), f'{legis} Party'] = 'PS'

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

        # Creating global dataframe of names by legislature, by party
        legis_member_ar_data = pd.concat([legis_member_ar_data, member_perparty_df[j].filter(items=['Name', 'DOB'])], ignore_index=True)
        column_array[0] = column_array[0] + [legis]*sum_perparty_df[j]
        column_array[1] = column_array[1] + [legis_party_df[i].iloc[j]]*sum_perparty_df[j]

    legis_member_perparty_df.append(member_perparty_df)
    legis_sum_perparty_df.append(sum_perparty_df)

legis_member_ar_data.index = pd.MultiIndex.from_arrays(column_array, names=('Legislature', 'Party'))

# Sorting to remove warnings, but puts legislatures in alphabetic order
#legis_member_ar_data = legis_member_ar_data.sort_index()

legis_member_ar_data["Election Date"] = np.zeros(len(legis_member_ar_data))

legis_member_ar_data.loc['Cons', 'Election Date'] = pd.to_datetime('1975-04-25')
legis_member_ar_data.loc['I', 'Election Date'] = pd.to_datetime('1976-04-25')
legis_member_ar_data.loc['II', 'Election Date'] = pd.to_datetime('1980-10-05')
legis_member_ar_data.loc['III', 'Election Date'] = pd.to_datetime('1983-04-25')
legis_member_ar_data.loc['IV', 'Election Date'] = pd.to_datetime('1985-10-06')
legis_member_ar_data.loc['V', 'Election Date'] = pd.to_datetime('1987-07-19')
legis_member_ar_data.loc['VI', 'Election Date'] = pd.to_datetime('1991-10-06')
legis_member_ar_data.loc['VII', 'Election Date'] = pd.to_datetime('1995-10-01')
legis_member_ar_data.loc['VIII', 'Election Date'] = pd.to_datetime('1999-10-10')
legis_member_ar_data.loc['IX', 'Election Date'] = pd.to_datetime('2002-03-17')
legis_member_ar_data.loc['X', 'Election Date'] = pd.to_datetime('2005-02-20')
legis_member_ar_data.loc['XI', 'Election Date'] = pd.to_datetime('2009-09-27')
legis_member_ar_data.loc['XII', 'Election Date'] = pd.to_datetime('2011-06-05')
legis_member_ar_data.loc['XIII', 'Election Date'] = pd.to_datetime('2015-10-04')
legis_member_ar_data.loc['XIV', 'Election Date'] = pd.to_datetime('2019-10-06')
legis_member_ar_data.loc['XV', 'Election Date'] = pd.to_datetime('2022-01-30')

legis_member_ar_data['Election Date'] = legis_member_ar_data['Election Date'].apply(pd.to_datetime)

legis_member_ar_data["Age at Election"] = legis_member_ar_data['Election Date'] - legis_member_ar_data['DOB']



# Creating 'Age at Election' column
age=legis_member_ar_data['Age at Election'].loc[legis_member_ar_data['Age at Election'].notna()]/ np.timedelta64(1, 'D')/365

age_bylegis = [age.loc[legis_df[i]].mean() for i in range(len(legis_df))]

## Plotting
fig, age_legis_plot = plt.subplots(1)

age_legis_plot.bar([legis_df[i] for i in range(len(legis_df))], age_bylegis)
age_legis_plot.plot([legis_df[i] for i in range(len(legis_df))], port_av_age, color='red', label='Idade Média Portuguesa')

age_legis_plot.set_xlabel('Legislatura')
age_legis_plot.set_ylabel('Idade Média (anos)')
age_legis_plot.set_title('Idade Média dos deputados da AR')
age_legis_plot.legend()
plt.show()



# PS average age
legis_ps = legis_member_ar_data.loc(axis=0)[:,'PS'].index.drop_duplicates()
age_byparty_ps = [age.loc[legis_ps[i][0], 'PS'].mean(skipna=True) for i in range(len(legis_ps))]

## Plotting
fig, age_ps_plot = plt.subplots(1)

age_ps_plot.bar([legis_ps[i][0] for i in range(len(legis_ps))], age_byparty_ps)
age_ps_plot.plot([legis_ps[i][0] for i in range(len(legis_ps))], port_av_age, color='red', label='Idade Média Portuguesa')

age_ps_plot.set_xlabel('Legislatura')
age_ps_plot.set_ylabel('Idade Média (anos)')
age_ps_plot.set_title('Idade Média dos deputados do PS')
age_ps_plot.legend()
plt.show()



# PSD-PPD average age
age_byparty_psd = [age.loc['Cons', 'PPD'].mean(skipna=True),
                   pd.concat([age.loc['I', 'PPD'], age.loc['I', 'PSD']]).mean(skipna=True), 
                   age.loc['II', 'PSD'].mean(skipna=True), 
                   age.loc['III', 'PSD'].mean(skipna=True), 
                   age.loc['IV', 'PSD'].mean(skipna=True), 
                   age.loc['V', 'PSD'].mean(skipna=True), 
                   age.loc['VI', 'PSD'].mean(skipna=True), 
                   age.loc['VII', 'PSD'].mean(skipna=True), 
                   age.loc['VIII', 'PSD'].mean(skipna=True), 
                   age.loc['IX', 'PSD'].mean(skipna=True), 
                   age.loc['X', 'PSD'].mean(skipna=True), 
                   age.loc['XI', 'PSD'].mean(skipna=True), 
                   age.loc['XII', 'PSD'].mean(skipna=True), 
                   age.loc['XIII', 'PSD'].mean(skipna=True), 
                   age.loc['XIV', 'PSD'].mean(skipna=True), 
                   age.loc['XV', 'PSD'].mean(skipna=True),]

## Plotting
fig, age_psd_plot = plt.subplots(1)

age_psd_plot.bar([legis_df[i] for i in range(len(legis_df))], age_byparty_psd)
age_psd_plot.plot([legis_df[i] for i in range(len(legis_df))], port_av_age, color='red', label='Idade Média Portuguesa')

age_psd_plot.set_xlabel('Legislatura')
age_psd_plot.set_ylabel('Idade Média (anos)')
age_psd_plot.set_title('Idade Média dos deputados do PPD-PSD')
age_psd_plot.legend()
plt.show()


# BE average age
age_byparty_be = [age.loc['VIII', 'BE'].mean(skipna=True), 
                   age.loc['IX', 'BE'].mean(skipna=True), 
                   age.loc['X', 'BE'].mean(skipna=True), 
                   age.loc['XI', 'BE'].mean(skipna=True), 
                   age.loc['XII', 'BE'].mean(skipna=True), 
                   age.loc['XIII', 'BE'].mean(skipna=True), 
                   age.loc['XIV', 'BE'].mean(skipna=True), 
                   age.loc['XV', 'BE'].mean(skipna=True),]


## Plotting
fig, age_be_plot = plt.subplots(1)

age_be_plot.bar([legis_df[i] for i in range(8,len(legis_df))], age_byparty_be)
age_be_plot.plot([legis_df[i] for i in range(8,len(legis_df))], port_av_age[8:], color='red', label='Idade Média Portuguesa')

age_be_plot.set_xlabel('Legislatura')
age_be_plot.set_ylabel('Idade Média (anos)')
age_be_plot.set_title('Idade Média dos deputados do BE')
age_be_plot.legend()
plt.show()



# PCP-PEV average age
age_byparty_pcp = [age.loc['Cons', 'PCP'].mean(skipna=True), 
                   age.loc['I', 'PCP'].mean(skipna=True),
                   age.loc['II', 'PCP'].mean(),
                   age.loc['III', 'PCP'].mean(),
                   age.loc['IV', 'PCP'].mean(),
                   pd.concat([age.loc['V', 'PCP'], age.loc['V', 'PEV']]).mean(),
                   pd.concat([age.loc['VI', 'PCP'], age.loc['VI', 'PEV']]).mean(),
                   pd.concat([age.loc['VII', 'PCP'], age.loc['VII', 'PEV']]).mean(),
                   pd.concat([age.loc['VIII', 'PCP'], age.loc['VIII', 'PEV']]).mean(),
                   pd.concat([age.loc['IX', 'PCP'], age.loc['IX', 'PEV']]).mean(),
                   pd.concat([age.loc['X', 'PCP'], age.loc['X', 'PEV']]).mean(),
                   pd.concat([age.loc['XI', 'PCP'], age.loc['XI', 'PEV']]).mean(),
                   pd.concat([age.loc['XII', 'PCP'], age.loc['XII', 'PEV']]).mean(),
                   pd.concat([age.loc['XIII', 'PCP'], age.loc['XIII', 'PEV']]).mean(),
                   pd.concat([age.loc['XIV', 'PCP'], age.loc['XIV', 'PEV']]).mean(),
                   age.loc['XV', 'PCP'].mean()]

## Plotting
fig, age_pcp_plot = plt.subplots(1)

age_pcp_plot.bar([legis_df[i] for i in range(len(legis_df))], age_byparty_pcp)
age_pcp_plot.plot([legis_df[i] for i in range(len(legis_df))], port_av_age, color='red', label='Idade Média Portuguesa')

age_pcp_plot.set_xlabel('Legislatura')
age_pcp_plot.set_ylabel('Idade Média (anos)')
age_pcp_plot.set_title('Idade Média dos deputados do PCP-PEV')
age_pcp_plot.legend()
plt.show()


print(legis_member_ar_data.loc(axis=0)[pd.IndexSlice[:,['PEV']]].index.drop_duplicates())

#print(legis_member_ar_data.loc[legis_member_ar_data['Name'] == 'Manuel Gonçalves Valente Fernandes'])
#print(legis_member_ar_data.loc(axis=0)[legis_member_ar_data.index[0][0]])