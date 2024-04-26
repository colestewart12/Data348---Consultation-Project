import os
import pandas as pd

# read CSV file
df = pd.read_csv('Student Financial Data Project.csv')

# drop all rows except first entry for each unique UID
df.drop_duplicates(subset='UID', keep='first', inplace=True)
# drop all students who have no fafse
df = df[df['EFC'] != "No FAFSA"]

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
