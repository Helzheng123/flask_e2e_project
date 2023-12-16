import pandas as pd

# import the dataset
df= pd.read_csv('/home/helen_zheng/flask_e2e_project/data/DOHMH_HIV_AIDS_Annual_Report_20231214.csv')
df

# drop NaN values
df_clean = df.dropna()
df_clean

# Remove duplicate rows through drop_duplicates
df_remove = df_clean.drop_duplicates(index=99999)
df_remove

# Check Rows and Columns
df_remove.shape

df_remove.to_csv('/home/helen_zheng/flask_e2e_project/data/cleaned_data.csv', index=False)