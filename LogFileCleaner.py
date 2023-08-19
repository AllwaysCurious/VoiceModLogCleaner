## Created by Bit Curious & ChatGPT ##


## Configurable Variables ##
MaxFileSize = "5" # (Value is in Megabyes) This variable clears log files, which are greater or equal to this value.
ClearTxtFormats = False # If your logs are txt files too. Then try setting this variable to True


## Essential Imports ##
import os


# Path to the directory containing log files
log_folder = "C:\\ProgramData\\Voicemod" # By default, you won't need to touch this. However, if your logs are located somewhere else, then change this path

# Here's a Breakdown on what this script does:

# 1. It will begin by calling a function to start the whole process
# 2. Then it will proceed to read all the files in the directory (folder)
# 3. It will then proceed to check if the File Type is rather a .log or .txt (The .txt file is customisable, and can be configured above)
# 4. Almost there! Then it will check if the File Size is large enough to clear.
# 5. Finally, it will empty all the data in the log or txt file, leaving the logs blank for Voicemod. Instead of deleting them, to prevent errors!

def delete_log_files(folder_path):
    NumberOfFiles = 0
    try:
        for root, dirs, files in os.walk(folder_path): # Read all files here!
            for file in files:
                if file.endswith(".log") or ClearTxtFormats == True and file.endswith(".txt"): # THIS IS DANGEROUS TO REMOVE. DO NOT REMOVE THIS!
                    file_path = os.path.join(root, file)
                    initial_size = os.path.getsize(file_path)
                    if (os.path.getsize(file_path)/(1024*1024)) >= float(MaxFileSize): # Checks if the file is big enough to get cleared. You can configure this in the variables section
                        NumberOfFiles = NumberOfFiles + len(files)
                        with open(file_path, 'w') as f:
                            f.truncate(0) # Empty all the data here!
                        final_size = os.path.getsize(file_path)
                        print(f"Emptied log file: {file_path}")
                        print(f"Initial size: {initial_size} bytes, Final size: {final_size} bytes")
                    else:
                        print(f"Skipping file '{file_path}' file size ({initial_size} bytes) is less than the minimum size {MaxFileSize}MB")
    except Exception as e:
        print("We encountered an error while trying to clear the log files!")
        print(e)
    print("")
    print(f"Cleaned {NumberOfFiles} log and/or txt files")
    print("Cleanup complete!")

if __name__ == "__main__":
    delete_log_files(log_folder) # Call function here!
