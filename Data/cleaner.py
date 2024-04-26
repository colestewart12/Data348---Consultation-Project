import os
import pandas as pd

# read CSV file
SFA = pd.read_csv('SFA_Cleaned.csv')

# drop all rows except first entry for each unique UID
SFA.drop_duplicates(subset='UID', keep='first', inplace=True)
# drop all students who have no fafsa
SFA = df[df['EFC'] != "No FAFSA"]

data = []

# 1/0 encode each race group and dichotomous variables

for row in SFA:
    row_data = []
    
    if row[12] == 'Male':
        row_data.append(1.0)
    else:
        row_data.append(0.0)
    
    if row[12] == 'Female' or row[12] == 'Unknown':
        row_data.append(1.0)
    else:
        row_data.append(0.0)
    
    if row[13] == 'American Indian or Native Alaskan':
        row_data.append(1.0)
    else:
        row_data.append(0.0) 

    if row[13] == 'Asian':
        row_data.append(1.0)
    else:
        row_data.append(0.0) 
   
    if row[13] == 'Black or African American':
        row_data.append(1.0)
    else:
        row_data.append(0.0)

    if row[13] == 'Hispanic':
        row_data.append(1.0)
    else:
        row_data.append(0.0) 

    if row[13] == 'Native Hawaiian or Pacific Islander':
        row_data.append(1.0)
    else:
        row_data.append(0.0) 

    if row[13] == 'White':
        row_data.append(1.0)
    else:
        row_data.append(0.0) 

    if row[16] == 'Yes':
        row_data.append(1.0)
    else:
        row_data.append(0.0)

    if row[17] == 'Yes':
        row_data.append(1.0)
    else:
        row_data.append(0.0)

    row_data.append(float(row[25])/float(row[2]))
   
    row_data.append(float(row[26])/float(row[2]))
   
    if row[23] == 'NA':
        row_data.append(0.0)
    else:
        row_data.append(float(row[23])/float(row[2]))
   
    data.append(row_data)

variables = ['CURR_GPA', 'FIRST_YEAR_CREDITS', 'DFWIS', 'PRIOR_SEMESTERS_COMPLETED',
             'IN_STATE', 'INTERNATIONAL', 'GENDER', 'ETHNICITY', 'FIRST_YEAR_ON_CAMPUS',
             'AGE', 'FGEN', 'FIRST_YEAR_MEAL_PLAN', 'WORK_STUDY', 'PELL', 'LOAN',
             'NON_PLU_SCHOLARSHIP', 'PLU_SCHOLARSHIP', 'EFC']

# make folder
folder_name = "split_csv"
os.makedirs(folder_name, exist_ok=True)

for var in variables:
    # make individual csvs for each variable
    data = df[['UID', 'TERM', var, 'GRADUATED']].copy()
    # remove rows with null values
    data.dropna(inplace=True)
    # save
    data.to_csv(f"{folder_name}/{var}.csv", index=False)
