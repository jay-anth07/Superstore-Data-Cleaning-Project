import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)        # Show all rows
pd.set_option('display.max_columns', None)     # Show all columns
pd.set_option('display.width', None)           # Auto-detect width
pd.set_option('display.max_colwidth', None)    # Show full column content

df = pd.read_csv("train.csv")
print(df.head(5))
#For understanding the columns and rows
print("\nDataSet Rows and Columns : ")
print(df.shape)
print("\nAll Columns : ")
print(df.columns)
print("\nAll Columns types : ")
print(df.info()) #To know Data Type of columns
print("\nStatical values : ")
print(df.describe().T)#To know Stat values
print("\nUnique values : ")
print(df.nunique())  #To know Unique values

print("\n\t\t\t\tData Access & Familiarization : ")
print(" Data Dictionary : ")
data_dictionary = pd.DataFrame({
    "Column Name": df.columns,
    "Data Type": df.dtypes.values,
    "Meaning": [
        "Unique row identifier",
        "Unique order transaction ID",
        "Date when order was placed",
        "Date when order was shipped",
        "Shipping method used",
        "Unique customer identifier",
        "Customer full name",
        "Customer segment category",
        "Country of customer",
        "City of customer",
        "State of customer",
        "Postal/ZIP code",
        "Geographical region",
        "Unique product identifier",
        "High-level product category",
        "Detailed product sub-category",
        "Full product description",
        "Revenue from the transaction"
    ],
    "Business Importance": [
        "Indexing purpose only",
        "Track and group transactions",
        "Time-based sales analysis",
        "Measure delivery performance",
        "Analyze shipping preferences",
        "Customer-level analysis",
        "Identification purpose only",
        "Segment revenue comparison",
        "Geographic expansion analysis",
        "City-level performance tracking",
        "State-level revenue analysis",
        "Geographic mapping support",
        "Regional performance comparison",
        "Product tracking and analysis",
        "Category-level business strategy",
        "Detailed product performance",
        "Top product identification",
        "Core revenue metric for business analysis"
    ]
})
print(data_dictionary)

print("\n\t\t\t Data Quality Assessment : ")

print("Null Values:\n",df.isnull().sum()) # For checking Missing Values
print("\nDuplicate values : ",df.duplicated().sum())  #Checking Duplicate values
print()

# Converting order & ship date dtype from string to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y')

#Transforming City and state names into title(Initial Letters are Caps) to reduce error while grouping
df['City'] = df['City'].str.strip().str.title()  # For city names
df['State'] = df['State'].str.strip().str.title() # For State names
print(df["City"].head(5)) #To return top 5 City names
print(df['State'].tail(5)) #To return least 5 State names

#Outlier analysis
print("Outlier Analysis")
import plotly.express as px
x=df['Sales']
fig = px.box(x)
fig.show()

print("\t\tOUTLIER DETECTION : Outlier detection was performed on the Sales column using the IQR method.\n "
      "Although several extreme high-value transactions were identified,\n "
      "these were retained as they represent valid bulk purchases rather than data errors.\n "
      "Therefore, no rows were removed.")
print("\n\t\t\tData Cleaning and Transformation")
print(df.duplicated().sum()) # There exist null values in the postal codes I replaced them with zero
df.fillna({'Postal Code': 0}, inplace=True)

df['Sales'] = df['Sales'].round(2) #Reducing sales decimal values
#By the RowID we have no use ,so better to drop that column
df.drop(columns=['Row ID'], inplace=True)
#By creating shipping days column we will get an ease understanding and detect the required time for shipping an order
df['Shipping Days'] = (df['Ship Date'] - df['Order Date']).dt.days
#To analyse yearly,monthly we add these three columns to the dataframe
df['Order Year'] = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month_name()
#To Categorize the sales as LOW,MEDIUM and HIGH lets create a column of Sales_Category
def sales_category(x):
    if x < 50:
        return "LOW"
    elif x < 200:
        return "MEDIUM"
    else:
        return "HIGH"
df['Sales Category'] = df['Sales'].apply(sales_category)

#Finally save the cleaned superstore dataset
df.to_csv("cleaned_superstore.csv", index=False)
data_dictionary.to_csv("Data_Dictinary.csv",index=False)
print(df.head())