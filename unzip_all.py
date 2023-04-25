import zipfile
with zipfile.ZipFile('/experiments/zubair/datasets/processed_scannet.zip', 'r') as zip_file:
    # Extract the contents of the file
    zip_file.extractall('/experiments/zubair/datasets')