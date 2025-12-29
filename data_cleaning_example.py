import pandas as pd

# Load sample dataset
data = pd.read_csv("sample_data.csv")

# View basic information
print(data.info())

# Drop missing values
cleaned_data = data.dropna()

# Save cleaned dataset
cleaned_data.to_csv("cleaned_data.csv", index=False)

print("Data cleaning complete.")
