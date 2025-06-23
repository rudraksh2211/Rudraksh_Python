import csv
data=[["Name","Roll_No","Branch","CGPA"],
      ["RUdraksh Dusad","96","Data Science","8.85"],
      ["Sachin Choudhary","97","Data Science","8.65"],
      ["Rohit Dhaked","95","Data Science","8.2"],
      ["Riya Dhaked","93","Data Science","9.4"],
      ["Riya Shakewat","94","Data Science","8.4"]]
with open('ass4.csv',"w")as file:
    write=csv.writer(file)
    for row in data:
        write.writerow(row)

with open('ass4.csv',"r")as file:
    read=csv.reader(file)
    for row in read:
        print(row)
    