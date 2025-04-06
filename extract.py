import zipfile
import os

# Path to your zip file
zip_path = r"c:\Users\balak\PalmTreeDet\robotflow.zip"
# Where to extract it
extract_path = r"c:\Users\balak\PalmTreeDet\Palm-Detection-2"

# Create folder if it doesn't exist
os.makedirs(extract_path, exist_ok=True)

# Extract the zip file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)
    
print(f"Extracted to: {extract_path}")