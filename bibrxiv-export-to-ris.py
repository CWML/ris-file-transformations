inputfile = "input-files/bibrxiv-output.txt"
outputfile = "output-files/resulting-ris-file-test"

f = open(inputfile, "r").read()

records = f.split("\n\n")

#lines = [x if x != '' else "ER  -" for x in lines]

with open(outputfile, 'w') as risfile:
    for record in records:
        record = record.replace("Title: ", "\nTI  - ")
        record = record.replace("Source: ", "AU  - ")
        record = record.replace("Annotation: ", "AB  - ")
        record = record.replace("Access Notes: ", "N1  - ")
        record = record.replace("ID: ", "AN  - ")
        #record = record.replace("DB  -", "\nDB  -")
        record = record.replace("URL: ", "UR  - ")
        record = record.replace("From: ", "\nDB  - ")
        risfile.write(record)
        risfile.write("\nTY  - GEN")
        risfile.write("\nER  - ")
        risfile.write("\n")
