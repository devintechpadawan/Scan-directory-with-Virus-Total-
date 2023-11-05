'''
Virus Total API Directory Scan
D. Taylor 
Arpil 2023
'''

import os
import json
import hashlib
from virus_total_apis import PublicApi as VirusTotalPublicApi
from prettytable import PrettyTable             # pip install prettytable  (to install the library)

# You will need to obtain an API Key from Virus Total
API_KEY = 'yourkey'

while True:
    directory = input("Starting directory: ")
    if not os.path.isdir(directory):
        print("Invalid Directory - try again")
        continue
    else:
        break


fileList   = []
fileHashes = {}

print("\nHashing Files: ", directory, "\n")

# Create a pretty table to display the results
resultTable = PrettyTable(['MD-5 Hash','Path'])  


''' Walk the path starting at the directory provided '''
filesProcessed = 0
bytesProcessed = 0

for root, dirs, files in os.walk(directory):

    # Walk the path from top to bottom.
    # For each file obtain the filename 
    
    for fileName in files:
        # Create the absolute path to the file
        path = os.path.join(root, fileName)
        fullPath = os.path.abspath(path)
        
        # attempt to process the file
        try:
            # attempt open
            with open(fullPath, 'rb') as fileToHash:
                # attempt to read the contents
                fileContents = fileToHash.read()
                filesProcessed += 1
                bytesProcessed = bytesProcessed + os.path.getsize(fullPath)
                md5Obj = hashlib.md5()                  # Create an MD5 Object
                md5Obj.update(fileContents)             # Update with the file contents
                digest = md5Obj.hexdigest()             # Obtain the hash digest
                fileHashes[digest.upper()] = fullPath   # Add an entry to the dictionary
                
        except Exception as err:                        # Capture and report any exceptions
            print("Exception Occured: ", err)
 


'''
Print out the results by processing through
each entry in the dictionary
'''

for md5Hash, path in fileHashes.items():
    resultTable.add_row( [md5Hash, path] )                    
    
resultTable.align = "l" 
print(resultTable.get_string())
#SAMPLE = input(b"What directory would you like to scan?") #b"X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
#SAMPLE_MD5 = hashlib.md5(directory).hexdigest()
'''
Print out the results from VirusTotal
'''


vt = VirusTotalPublicApi(API_KEY)

for hashes, path in fileHashes.items():
    print()
    print("FILEPATH")
    print(path)
    print()
    response =  vt.get_file_report(hashes)
    print (json.dumps(response, sort_keys=False, indent=4))