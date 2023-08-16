# Install kaggle using pip install kaggle command

# Get the API key from the website and paste it in the path as mentioned on website

# On kaggle website we can get command on which if we run we can get huge data in just a sec

# Extract data from zip file

from zipfile import ZipFile

dataset = 'path of data'

with ZipFile(dataset, 'r') as zip:                 # With is used to open file ZipFile function is used to extract file
    zip.extractall()
    print("Dataset is successfully extracted")