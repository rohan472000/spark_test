import json

# Create an empty list to store the blocks
blocks = []

# Read the values for "name" and "type" from a text file
with open("columns_names.txt") as f:
    lines = f.readlines()
    for line in lines:
        values = line.strip().split(',')
        name = values[0]
        type = values[1]

        # Add a block to the list for each line in the input file
        block = {"name": name, "type": type, "mode": "NULLABLE", "desc": ""}
        blocks.append(block)

# Write the list of blocks to a JSON file
with open("output.json", "w") as f:
    json.dump(blocks, f, indent=4)
