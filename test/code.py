import os


def extract_technology(file_name):
    technology_list = ["GSM", "UMTS", "LTE", "5G"]
    for tech in technology_list:
        if tech in file_name:
            return tech


folder_path = "../test/"
file_list = os.listdir(folder_path)
for file_name in file_list:
    technology = extract_technology(file_name)
    if technology:
        print("Technology in {}: {}".format(file_name, technology))
    else:
        print("listed technology not found in {}".format(file_name))
