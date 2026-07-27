# ==========================================
# Data Cleaning & Reporting Automation
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------
# Load Dataset
# ------------------------------------------
df = pd.read_excel("/content/Data_Cleaning_Dataset.xlsx")

print("========== Original Dataset ==========")
print(df.head())

# ------------------------------------------
# Dataset Information
# ------------------------------------------
print("\nDataset Information")
print(df.info())

# ------------------------------------------
# Remove Duplicate Rows
# ------------------------------------------
duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

df = df.drop_duplicates()

# ------------------------------------------
# Handle Missing Values
# ------------------------------------------
for column in df.columns:

    if df[column].dtype == "object":
        df[column] = df[column].fillna("Unknown")
    else:
        df[column] = df[column].fillna(df[column].mean())

# ------------------------------------------
# Standardize Text Columns
# ------------------------------------------
for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip().str.title()

# ------------------------------------------
# Save Cleaned Dataset
# ------------------------------------------
df.to_excel("Cleaned_Employee_Data.xlsx", index=False)

print("\nData Cleaning Completed Successfully!")

# ------------------------------------------
# Generate Summary Report
# ------------------------------------------
summary = df.describe(include="all")

print("\n========== Summary ==========")
print(summary)

summary.to_excel("Summary_Report.xlsx")

# ==========================================
# GRAPH 1 : Employees by Department
# ==========================================

dept = df["Department"].value_counts()

plt.figure(figsize=(8,5))
dept.plot(kind="bar")

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("Employees_By_Department.png")
plt.show()

# ==========================================
# GRAPH 2 : Average Salary by Department
# ==========================================

salary = df.groupby("Department")["Salary"].mean()

plt.figure(figsize=(8,5))
salary.plot(kind="bar")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.tight_layout()
plt.savefig("Average_Salary_Department.png")
plt.show()

# ==========================================
# GRAPH 3 : Employee Distribution by City
# ==========================================

city = df["City"].value_counts()

plt.figure(figsize=(8,5))
city.plot(kind="pie", autopct="%1.1f%%")

plt.title("Employee Distribution by City")
plt.ylabel("")

plt.tight_layout()
plt.savefig("Employees_By_City.png")
plt.show()

# ==========================================
# GRAPH 4 : Age Distribution
# ==========================================

plt.figure(figsize=(8,5))

plt.hist(df["Age"], bins=10)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("Age_Distribution.png")
plt.show()

# ==========================================
# GRAPH 5 : Salary Distribution
# ==========================================

plt.figure(figsize=(8,5))

plt.hist(df["Salary"], bins=10)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("Salary_Distribution.png")
plt.show()

# ==========================================
# GRAPH 6 : Experience vs Salary
# ==========================================

plt.figure(figsize=(8,5))

plt.scatter(df["Experience"], df["Salary"])

plt.title("Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")

plt.tight_layout()
plt.savefig("Experience_vs_Salary.png")
plt.show()

# ==========================================
# GRAPH 7 : Performance Rating Distribution
# ==========================================

rating = df["Performance_Rating"].value_counts().sort_index()

plt.figure(figsize=(8,5))
rating.plot(kind="bar")

plt.title("Performance Rating Distribution")
plt.xlabel("Performance Rating")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("Performance_Rating.png")
plt.show()

# ==========================================
# Final Output
# ==========================================

print("\n===================================")
print("Automation Completed Successfully!")
print("===================================")

print("\nGenerated Files")
print("1. Cleaned_Employee_Data.xlsx")
print("2. Summary_Report.xlsx")
print("3. Employees_By_Department.png")
print("4. Average_Salary_Department.png")
print("5. Employees_By_City.png")
print("6. Age_Distribution.png")
print("7. Salary_Distribution.png")
print("8. Experience_vs_Salary.png")
print("9. Performance_Rating.png")
