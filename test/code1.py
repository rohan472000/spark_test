import os


def extract_technology(file_name):
    start = file_name.index("_") + 1
    end = file_name.index("_", start)
    print(start,end)
    return file_name[start:end]


folder_path = "../test/"
technology_names = set()
for filename in os.listdir(folder_path):
    if filename.endswith(".zip"):
        technology = extract_technology(filename)
        print(technology)
        technology_names.add(technology)

print("Technology names found in the folder:", technology_names)
