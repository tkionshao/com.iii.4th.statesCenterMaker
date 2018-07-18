# This is the project for iii.
## Team: CB101 4th
### Modules:
1. state_code_cleaner
This is a module for checking how many state codes in specific data, and it will check missing value.
You could run the commandline as below. To get a new and clear file in the same folder but the name with new tag, 'clr'.

>##### COMMAND LINE
>cd ./state_code_cleaner
>python3 main.py [data in anywhere if you want]

2. make_center
Then we could use correct state code as row name to create a new dataframe. It will be added new tag in filename.

>##### COMMAND LINE
>cd ./make_center
>python3 main.py [clean data]
