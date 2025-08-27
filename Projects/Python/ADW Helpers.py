QDates = [
    ("DELETE FROM transaction WHERE ReportingDate >= '2020-11-01' AND ReportingDate < '2021-01-31'","EVALUATE FILTER('Transaction','Transaction'[Reporting_Date] >= DATE(2020,11,1) && 'Transaction'[Reporting_Date] < DATE(2021,1,31))"), #Q1-2021 Index 0
    ("DELETE FROM transaction WHERE ReportingDate >= '2021-01-31' AND ReportingDate < '2021-05-02'","EVALUATE FILTER('Transaction','Transaction'[Reporting_Date] >= DATE(2021,1,31) && 'Transaction'[Reporting_Date] < DATE(2021,5,2))"), #Q2-2021 Index 1
    ("DELETE FROM transaction WHERE ReportingDate >= '2021-05-02' AND ReportingDate < '2021-08-01'","EVALUATE FILTER('Transaction','Transaction'[Reporting_Date] >= DATE(2021,05,2) && 'Transaction'[Reporting_Date] < DATE(2021,8,1))"), #Q3-2021 Index 2
    ("DELETE FROM transaction WHERE ReportingDate >= '2021-08-01' AND ReportingDate < '2021-10-31'","EVALUATE FILTER('Transaction','Transaction'[Reporting_Date] >= DATE(2021,08,1) && 'Transaction'[Reporting_Date] < DATE(2021,10,31))"), #Q4-2021 Index 3

    ("DELETE FROM transaction WHERE ReportingDate >= '2021-10-31' AND ReportingDate < '2022-01-30'","EVALUATE FILTER('Transaction','Transaction'[Reporting_Date] >= DATE(2021,10,31) && 'Transaction'[Reporting_Date] < DATE(2022,1,30))"), #Q1-2022 Index 4
    ("DELETE FROM transaction WHERE ReportingDate >= '2022-01-30' AND ReportingDate < '2022-05-01'","EVALUATE FILTER('Transaction','Transaction'[Reporting_Date] >= DATE(2022,1,30) && 'Transaction'[Reporting_Date] < DATE(2022,5,1))"), #Q2-2022 Index 5
    ("DELETE FROM transaction WHERE ReportingDate >= '2022-05-01' AND ReportingDate < '2022-07-31'","EVALUATE FILTER('Transaction','Transaction'[Reporting_Date] >= DATE(2022,05,1) && 'Transaction'[Reporting_Date] < DATE(2022,7,31))"), #Q3-2022 Index 6
    ("DELETE FROM transaction WHERE ReportingDate >= '2022-07-31' AND ReportingDate < '2022-10-30'","EVALUATE FILTER('Transaction','Transaction'[Reporting_Date] >= DATE(2022,07,31) && 'Transaction'[Reporting_Date] < DATE(2022,10,30))"), #Q4-2022 Index 7

    ("DELETE FROM transaction WHERE ReportingDate >= '2022-10-30' AND ReportingDate < '2023-01-29'","EVALUATE FILTER('Transaction','Transaction'[Reporting_Date] >= DATE(2022,10,30) && 'Transaction'[Reporting_Date] < DATE(2023,1,29))"), #Q1-2023 Index 8
    ("DELETE FROM transaction WHERE ReportingDate >= '2023-01-29' AND ReportingDate < '2023-04-30'","EVALUATE FILTER('Transaction','Transaction'[Reporting_Date] >= DATE(2023,1,29) && 'Transaction'[Reporting_Date] < DATE(2023,4,30))"), #Q2-2023 Index 9
    ("DELETE FROM transaction WHERE ReportingDate >= '2023-04-30' AND ReportingDate < '2023-07-30'","EVALUATE FILTER('Transaction','Transaction'[Reporting_Date] >= DATE(2023,04,30) && 'Transaction'[Reporting_Date] < DATE(2023,7,30))"), #Q3-2023 Index 10
    ("DELETE FROM transaction WHERE ReportingDate >= '2023-07-30' AND ReportingDate < '2023-10-29'","EVALUATE FILTER('Transaction','Transaction'[Reporting_Date] >= DATE(2023,07,30) && 'Transaction'[Reporting_Date] < DATE(2023,10,29))"), #Q4-2023 Index 11

    ("DELETE FROM transaction WHERE ReportingDate >= '2023-10-29' AND ReportingDate < '2024-02-04'","EVALUATE FILTER('Transaction','Transaction'[Reporting_Date] >= DATE(2023,10,29) && 'Transaction'[Reporting_Date] < DATE(2024,2,4))"), #Q1-2024 Index 12
    ("DELETE FROM transaction WHERE ReportingDate >= '2024-02-04' AND ReportingDate < '2024-05-05'","EVALUATE FILTER('Transaction','Transaction'[Reporting_Date] >= DATE(2024,2,4) && 'Transaction'[Reporting_Date] < DATE(2024,5,5))"), #Q2-2024 Index 13
    ("DELETE FROM transaction WHERE ReportingDate >= '2024-05-05' AND ReportingDate < '2024-08-04'","EVALUATE FILTER('Transaction','Transaction'[Reporting_Date] >= DATE(2024,05,5) && 'Transaction'[Reporting_Date] < DATE(2024,8,4))"), #Q3-2024 Index 14
    ("DELETE FROM transaction WHERE ReportingDate >= '2024-08-04' AND ReportingDate < '2024-11-02'","EVALUATE FILTER('Transaction','Transaction'[Reporting_Date] >= DATE(2024,08,4) && 'Transaction'[Reporting_Date] < DATE(2024,11,2))"), #Q4-2024 Index 15 


    ("DELETE FROM transaction WHERE ReportingDate >= '2024-11-03' AND ReportingDate < '2025-02-02'","EVALUATE FILTER('Transaction','Transaction'[Reporting_Date] >= DATE(2024,11,3) && 'Transaction'[Reporting_Date] < DATE(2025,2,2))"), #Q1-2025 Index 16 
    ("DELETE FROM transaction WHERE ReportingDate >= '2025-02-02' AND ReportingDate < '2025-05-04'","EVALUATE FILTER('Transaction','Transaction'[Reporting_Date] >= DATE(2025,2,2) && 'Transaction'[Reporting_Date] < DATE(2025,5,4))"), #Q2-2025 Index 17 
    ("DELETE FROM transaction WHERE ReportingDate >= '2025-05-04' AND ReportingDate < '2025-08-03'","EVALUATE FILTER('Transaction','Transaction'[Reporting_Date] >= DATE(2025,5,4) && 'Transaction'[Reporting_Date] < DATE(2025,8,3))"), #Q3-2025 Index 18 
    ("DELETE FROM transaction WHERE ReportingDate >= '2025-08-03' AND ReportingDate < '2025-11-02'","EVALUATE FILTER('Transaction','Transaction'[Reporting_Date] >= DATE(2025,8,3) && 'Transaction'[Reporting_Date] < DATE(2026,11,2))") #Q4-2025 Index 19 Current
    
]

def replace_non_alphanumeric(df):
    # Get the current column names
    columns = df.columns
    
    # Create a dictionary to map old column names to new column names
    new_column_names = {}
    
    for col in columns:
        # Replace non-alphanumeric characters with underscores
        new_col = re.sub(r'\W+', '_', col)
        new_column_names[col] = new_col
    
    # Rename the columns in the dataframe
    df.rename(columns=new_column_names, inplace=True)
    
    return df

def display_column_names(df):
    # Get the column names
    columns = df.columns
    
    # Print the column names
    for col in columns:
        print(col)

def remove_brackets_from_columns(df):
    df.columns = df.columns.str.replace(r'[\[\]]', '', regex=True)
    return df


