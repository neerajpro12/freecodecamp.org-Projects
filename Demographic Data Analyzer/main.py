import pandas as pd

columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary']

df = pd.read_csv("adult.data", header=None, names=columns, skipinitialspace=True, na_values='?')
# print(df.head())

#Races and number of people in it. Output -> Series
race_count = df['race'].value_counts().tolist()
# Average Age of Men
avg_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)
# Percentage of people with education as 'Bachelors'
total_count = df.shape[0]
bachelor_count = (df['education'] == 'Bachelors').sum()
bachelor_percentage = round((bachelor_count / total_count) * 100, 1)
# Rich and higher education
rich_high_education_percentage = round(df.loc[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == ">50K")].shape[0] / df.loc[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].shape[0] * 100, 1)
# Rich and non higher education
rich_lower_education_percentage = round(df.loc[(~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == ">50K")].shape[0] / df.loc[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].shape[0] * 100, 1)
#Min hours per week
min_hours_per_week = df['hours-per-week'].min()
#Rich and min horus per week
rich_min_hours_per_week = round((df.loc[(df['hours-per-week'] == 1) & (df['salary'] == ">50K")].shape[0] / df.loc[df['hours-per-week'] == 1].shape[0] * 100), 1)
#Rich Country
country_salary = df.loc[df['salary'] == ">50K"]['native-country'].value_counts()
country_total = df['native-country'].value_counts()
rich_country = (country_salary / country_total).idxmax()
rich_country_percentage = round((country_salary / country_total).max() * 100, 1)
# Indian rich occupation
rich_india_occupation = df.loc[(df['salary'] == ">50K") & (df['native-country'] == "India")]['occupation'].value_counts().idxmax()


print(f'1. Number of People in each race are {race_count}' )
print(f"2. Average age of Men is {avg_age_men:.2f} years")
print(f"3. Percentage of people with Bachelors Education: {bachelor_percentage:.2f}%")
print(f"4. Percentage of rich people with Bachelors Education: {rich_high_education_percentage:.2f}%")
print(f"5. Percentage of rich people with no advanced education: {rich_lower_education_percentage:.2f}%")
print(f"6. Minimum hours per week is {min_hours_per_week:.2f} hours")
print(f"7. Rich with Minimum hours per week is {rich_min_hours_per_week:.2f}%")
print(f"8. Rich country is {rich_country} with percentage {rich_country_percentage:.2f}%")
print(f"9. Rich occupation in India is is {rich_india_occupation}")
