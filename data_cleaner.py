import csv
with open("the data of zeus.csv", newline="", encoding="utf8") as file:
    data = csv.reader(file)
    raw = []
    for row in data:
        raw.append(row[:7])

    #change blanks to "NA"
    for row in raw:
        for i in range(len(row)):
            if row[i] == "" or row[i] == " " or row[i] == "_":
                row[i] = "NA"
            #replace � with " "
            if "�" in row[i]:
                row[i] = row[i].replace("�", " ")
    counter = 0
    print(len(raw))
    new_raw = []
    #Remove bad data
    for row in raw:
        a = row.count("NA")
        #print(type(a))
        if a < 3:
            print(row, a)
            new_raw.append(row)
            counter += 1
    raw = new_raw
    
    with open("data_clean.csv", "w", newline="", encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(raw)

    #10-19