#Problem 1: Read File

"""with open ("data.txt", "r") as file:
    for line in file:
        print(line.strip())"""

#Problem 2: Write File
"""
with open("output.txt", "w") as file:
    file.write("Hello prem")"""

#Problem 3: Append File

"""with open("output.txt", "a") as file:
    file.write("\nHello John")"""

#Problem 4: Count Lines
"""count = 0
with open("output.txt", "r") as file:
    for line in file:
        count += 1
print(count)"""


# CSV File Handling

# mock task

""""import csv;

with open ("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row[0])
"""
#NEW STUDENTS FILE

"""import csv
with open ("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "State"])
    writer.writerow(["john", "23", "Tenkasi"])
    writer.writerow(["joo", "20", "Tenkasi"])
"""

#PROBLEM 1 PRINT ALL ROWS

"""import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row[0], row[2])"""

#Problem: Print Students Age > 22

"""import csv
with open ("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    count = 0
    for row in reader:
        if row[2] == "tenkasi":
            count += 1
print(count)      """     

#Problem: Find Average Age from CSV

"""import csv

with open ("students.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    total = 0
    count = 0

    for row in reader:
        total += int(row[1])
        count += 1
    average = total/count
print(average)"""

# PROBLEM - Write Filtered CSV File

import csv

with open ("students.csv", "r") as infile,\
        open ("passedstudents.csv", "w", newline="") as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    next (reader)

    writer.writerow(["name", "age", "city"])
    for row in reader:
        if int(row[1]) > 21:
            writer.writerow(row)