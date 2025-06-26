import pandas as pd

# Create a sample DataFrame with date strings
data = {
    'date_string': [
        '2023-01-15',
        '2023-02-20',
        '2023-03-25',
        '2023-04-30',
        '2027-05-05'
    ]
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Convert the 'date_string' column to datetime objects
df['date'] = pd.to_datetime(df['date_string'])

# Display the DataFrame with the new datetime column
print("\nDataFrame with datetime column:")
print(df)

# Extract year, month, and day from the datetime column
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

# Display the DataFrame with extracted components
print("\nDataFrame with extracted year, month, and day:")
print(df)

# Calculate the difference between dates
df['next_date'] = df['date'] + pd.DateOffset(days=10)  
df['date_difference'] = df['next_date'] - df['date']  

# Display the DataFrame with date arithmetic
print("\nDataFrame with date arithmetic:")
print(df)

# Filter rows where the month is greater than 3 (April and beyond)
filtered_df = df[df['month'] > 3]

# Display the filtered DataFrame
print("\nFiltered DataFrame (month > 3):")
print(filtered_df)

# Get the current date
current_date = pd.Timestamp.now()

# Display the current date
print("\nCurrent date:")
print(current_date)

# Check if the dates in the DataFrame are in the past
df['is_past'] = df['date'] < current_date

# Display the DataFrame with past date check
print("\nDataFrame with past date check:")
print(df)
