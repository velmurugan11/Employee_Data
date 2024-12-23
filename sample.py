from numpy import random
import numpy as np
import pandas as pd 
import csv

# Employee ID (1 to 100)
Employee_ID = np.random.choice(range(1,101,1),size=(100),replace=False)

# Age (random integers between 22 and 60)
Age = np.random.choice(range(22,61),size=(100))

# Salary (random floats between 30,000 and 120,000)
Salary = np.random.choice(range(30000, 120000),size=(100))

data = {
    "Employee_ID" : Employee_ID,
    "Age" : Age,
    "Salary" : Salary
}

# Load data into dataframe
dataframe = pd.DataFrame(data)

# Adding new columns Based on Conditions
dataframe['Seniority'] = np.where(dataframe['Age']>40,"Senior","Junior")
dataframe['Tax'] = dataframe['Salary']*0.2

dataframe.to_csv("emp_data.csv",index=False)

# Another method for saving data as csv format.
# with open("emp_data.csv",mode='w',newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(dataframe)

average_salary_by_seniority = dataframe.groupby('Seniority')['Salary'].mean()
highest_salary_employee = dataframe.loc[dataframe['Salary'].idxmax()]
total_tax_by_salary = dataframe.groupby('Seniority')['Tax'].sum()

print(average_salary_by_seniority,highest_salary_employee,total_tax_by_salary)
print("The data has been loaded and saved as csv file.")