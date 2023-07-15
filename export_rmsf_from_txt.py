import pandas as pd
import os

# Define the directory containing the output text files
output_dir = "C:/Users/darkh/Downloads/test/rmsf"

# Get a list of all the output text files in the directory
# Sort them numerically so they are processed in order
files = os.listdir(output_dir)
files = [f for f in files if f.startswith("RMSF") and f.endswith(".txt")]
files.sort(key=lambda x: int(x[4:-4])) 

# Create an empty data frame to store the RMSF values
df = pd.DataFrame()

# Loop over the sorted output text files
for file_name in files:
  
  # Read in the data from the text file
  file_path = os.path.join(output_dir, file_name)
  data = pd.read_csv(file_path, sep=" ", header=None, names=["Residue", file_name[:-4]])

  # Extract the RMSF values and add them to the data frame
  rmsf_values = data.iloc[:, 1]
  df[file_name[:-4]] = rmsf_values

# Write the data frame to an Excel file  
writer = pd.ExcelWriter("RMSF.xlsx", engine="openpyxl")
df.to_excel(writer, index=False)
writer.book.save("C:/Users/darkh/Downloads/test/RMSF.xlsx")
writer.close()
