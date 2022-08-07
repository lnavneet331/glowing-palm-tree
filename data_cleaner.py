import csv
with open("data.csv", newline="") as file:
    data = csv.reader(file)
    raw = []
    for row in data:
        raw.append(row[:10])

    #change blanks to "NA"
    for row in raw:
        for i in range(len(row)):
            if row[i] == "" or row[i] == " " or row[i] == "_":
                row[i] = "NA"
            #replace � with " "
            if "�" in row[i]:
                row[i] = row[i].replace("�", " ")

    with open("data_clean.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(raw)

    #10-19