import os
import json

# Create the directory if it doesn't exist
!mkdir -p /root/.config/kaggle

# Create the kaggle.json file with your credentials
kaggle_json = {
    "username": "skbahmed",
    "key": "32456jhtgrfe4r356754rfgr4546453er45"
}

# Write the json file
with open('/root/.config/kaggle/kaggle.json', 'w') as f:
    json.dump(kaggle_json, f)

# Set appropriate permissions
!chmod 600 /root/.config/kaggle/kaggle.json
