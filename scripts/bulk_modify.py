# scripts/bulk_modify.py

import os

# File list
files_to_modify = [
    "../todos/models.py",
    "../todos/views.py",
    "../todos/forms.py"
]

for file_path in files_to_modify:
    with open(file_path, "a") as f:  # append mode
        f.write("\n# Added by automation script\n")

print("All files updated successfully!")
