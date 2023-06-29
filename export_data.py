import pandas as pd
import os

# Directory containing the text files
directory = r"C:/Users/darkh/Downloads/test/New folder"

# List to store the data from each file
file_data = []

# Iterate over the files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        file_path = os.path.join(directory, filename)
        with open(file_path, "r") as file:
            lines = file.readlines()
            column_data = []
            for line in lines:
                line = line.strip().split()
                if len(line) >= 2:
                    try:
                        data = float(line[1])
                        column_data.append(data)
                    except ValueError:
                        pass
            file_data.append(column_data)

# Create a DataFrame from the file data
df = pd.DataFrame(file_data)

# Output file path for the combined data
output_file = r"C:/Users/darkh/Downloads/test/New folder/test.xlsx"

# Write the DataFrame to a new Excel file
df.to_excel(output_file, index=False)
