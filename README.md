# Google IT Automation with Python Professional Certification
My projects for the Google IT Automation with Python certification

## Crash Course with Python (First module)
After learning the basics of Python it was required that we created a filter from any given String and filter certain words and symbols and after all the filtering print out the dictionary in a Wordcloud.
You will find the Jupyter Notebook with the assignment and the .txt book The Life of Abraham Lincoln that I used.

## Using Python to Interact with the Operating System (Week 6)
#### findJane.sh
The bash script reads the files from the data/list.txt, stores it in a file (tempFile.txt) and the reads it to a variable where it goes through the files in the directory and checks if they exist.
#### changeJane.py
The python script reads the result file (oldFiles.txt) and then renames each one of them from jane to jdoe.

## Using Python to Interact with the Operating System (Week 7)
### Final Project
#### Ticky_check.py
It will read the logs and generate two csv files based on the user counter and error counter on each line of the log file.
#### User_statistics.csv
This CSV file contains how many times each user appears on the info and error messages from the logs.
#### Error_Message.csv
This CSV file contains the types of errors on the logs file and the number of each occurrence.
 
## Automating Real-World Tasks with Python
### Week 1 - Scale and convert images using PIL
#### scale_image.py
This script executes the assignment. It reads all the icons in the image folder, rotates it 90 degrees clockwise, resizes to 128x128 and saves it on a different folder: "/opt/icons/"

### Week 2 - Process Text Files with Python Dictionaries and Upload to Running Web Service
#### run.py
This script reads the text files from the desired location, creates a dictionary and appends the line to a certain key and then sends the dictionary as a JSON using the POST method to the assigned URL.

### Week 3 - Automatically Generate a PDF and send it by Email
#### examples.py
Fixes a minor error on the default code and adds the kiwi row, generates the PDF and sends through email.
#### cars.py
Reads the cars .json file and tries to find:
1. Calculate the car model which had the most sales.
2. Calculate the year with the most sales.
After doing all that it generates a PDF with all the desired information and sends it via email.
