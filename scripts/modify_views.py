import os

# Project এর views.py path
views_file = "../todos/views.py"

with open(views_file, "r") as f:
    lines = f.readlines()

# নতুন comment add করা function শেষে
new_lines = []
for line in lines:
    new_lines.append(line)
    if "def " in line:  # প্রতিটি function এর পরে comment add করবে
        new_lines.append("    # TODO: check this function\n")

with open(views_file, "w") as f:
    f.writelines(new_lines)

print("views.py modify completed!")
