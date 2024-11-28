import pandas as pd

# Replace with your local file path
path = "C:/Users/sudet/Downloads/bank_info.xlsx"

# Load the Excel file into a DataFrame
df = pd.read_excel(path)

# Display the first few rows and column names to understand the structure
print("Column Names:", df.columns)
print(df.head())

# Filter the DataFrame to include only rows with negative amounts
df_expenses = df[df['Amount'] < 0]

# Display the first few rows of the filtered DataFrame
print(df_expenses.head())

unique_descriptions = df_expenses['Description'].unique()
print(unique_descriptions)

# Create an empty dictionary to store the labels
description_labels = {}

# Iterate through each unique description and prompt for a labeli
for description in unique_descriptions:
    label = input(f"Enter label for '{description}': ")
    description_labels[description] = label

# Display the dictionary with labels
print(description_labels)

# Iterate through the df_expenses DataFrame and update the 'Category' column
df_expenses['Category'] = df_expenses['Description'].map(description_labels)

# Display the first few rows of the updated DataFrame
print(df_expenses.head())

# Update the original DataFrame with the labels
df['Category'] = df['Description'].map(description_labels)

# Save the updated DataFrame back to the Excel file
df.to_excel(path, index=False)

print("Labels added to the original Excel file successfully.")

print(df.head())