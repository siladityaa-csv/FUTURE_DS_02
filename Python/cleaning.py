import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("E:/IMPORTANT/work/intern/FUTURE Intern/Customer_Retention_&_Churn_Analysis/Data/Telco-Customer-Churn.csv")

df.head()
df.info()
df.isnull().sum()

#converting TotalCharges to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna()
df.isnull().sum()

#converting churn to numeric
df['Churn_Flag'] = df['Churn'].map({'Yes':1, 'No':0})
df['Churn'].value_counts()

#KPI metrics
total_customers = df['customerID'].nunique()
print("Total Customers:", total_customers)

#Overall Churn Rate
churn_rate = df['Churn_Flag'].mean()*100
print("Churn Rate:", churn_rate)

#Average Tenure
avg_tenure = df['tenure'].mean()
print("Average Tenure:", avg_tenure)

#Average Monthly Charges
avg_monthly = df['MonthlyCharges'].mean()
print("Average Monthly Charges:", avg_monthly)

contract_churn = df.groupby('Contract')['Churn_Flag'].mean()*100

print(contract_churn)

sns.barplot(x='Contract', y='Churn_Flag', data=df)
plt.title("Churn Rate by Contract Type")
plt.show()

internet_churn = df.groupby('InternetService')['Churn_Flag'].mean()*100
print(internet_churn)

payment_churn = df.groupby('PaymentMethod')['Churn_Flag'].mean()*100
print(payment_churn)

df['Tenure_Group'] = pd.cut(df['tenure'],
                           bins=[0,12,24,36,48,60,72],
                           labels=['0-1yr','1-2yr','2-3yr','3-4yr','4-5yr','5-6yr'])

df.groupby('Tenure_Group')['Churn_Flag'].mean()*100

df.to_csv("cleaned_telco_churn.csv", index=False)
