# def extract_technology(file_name):
#     first_underscore = file_name.index("_")
#     second_underscore = file_name.index("_", first_underscore + 1)
#     start = first_underscore + 1
#     end = second_underscore
#     return file_name[start:end]
#
# file_names = [
#     "EE_GSM_frequency_20230101_part001.zip",
#     "EE_UMTS_frequency_20230101_part001.zip",
#     "EE_LTE_1800_frequency_20230101_part001.zip",
#     "EE_LTE_800_frequency_20230101_part001.zip",
#     "EE_5G_frequency_20230101_part001.zip"
# ]
#
# for file_name in file_names:
#     technology = extract_technology(file_name)
#     print(technology)
import os


def extract_technology_name(file_name):
    start = file_name.index("_") + 1
    print(start)
    end = file_name.index("_", start)
    print(end)
    technology = file_name[start:end]
    if technology == "LTE":
        frequency_start = end + 1
        frequency_end = file_name.index("_", frequency_start)
        frequency = file_name[frequency_start:frequency_end]
        technology = technology + frequency
    return technology


folder_path = "../test"
for filename in os.listdir(folder_path):
    if filename.endswith(".zip"):
        technology = extract_technology_name(filename)
        print(technology)
