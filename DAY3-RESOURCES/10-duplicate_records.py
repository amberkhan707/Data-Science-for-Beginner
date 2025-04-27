# clean duplicates
#Load the required libraries
import pandas as pd
import numpy as np

# List of Tuples
employees = [('Shruti', 28, 'Varanasi'),
            ('Saumya', 32, 'Delhi'),
            ('Aaditya', 25, 'Mumbai'),
            ('Saumya', 32, 'Delhi'),
            ('Saumya', 32, 'Delhi'),
            ('Saumya', 32, 'Mumbai'),
            ('Aaditya', 40, 'Dehradun'),
            ('Seema', 32, 'Delhi'),
            ('Aditya', 36, 'Delhi'),
            ('Anurag', 40, 'Mumbai'),
            ('Shruti', 32, 'Mumbai'),
            ('Aaditya', 25, 'Mumbai'),
            ('Shruti', 28, 'Delhi'),
            ('Aditya', 25, 'Mumbai')]

# Creating a DataFrame object
df = pd.DataFrame(employees, columns = ['Name', 'Age', 'City'])

print("Employee List :")
print(df)
print()

#duplicated function determines if a row is duplcated or not
isdup=df.duplicated()
print("Printing duplicate status for each record")
print(isdup)
print()

# print the number of duplicate records
print("Number of duplicate records is : " , isdup.sum())

#display duplicate records using this bool vector
print("Duplicate records")
print(df[isdup])
print()

#display duplicate records using this bool vector
print("Unique records")
print(df[~isdup])
print()

print("=========================================================\n")

input("Press Enter to continue")


# Selecting duplicate rows except first
# occurrence based on all columns
duplicate = df[df.duplicated()]
print("Duplicate Rows :")
# Print the resultant Dataframe
print(duplicate)
print()

# report duplicates, keeping the last (latest)
print("Duplicate Rows with keep = last:")
duplicate = df[df.duplicated(keep='last')]  # keep = 'last' retains last duplicate
# Print the resultant Dataframe
print(duplicate)
print()

# Selecting duplicate rows based
# on 'City' column
duplicate = df[df.duplicated('City')]
print("Duplicate Rows based on City :")
# Print the resultant Dataframe
print(duplicate)
print()

# drop all duplicate records
unique_records= df.drop_duplicates()
print("Data without duplicates ")
print(unique_records)
print()

print("Done")
