import openpyxl
import csv

CSV_FILE = "dataset_info.csv"

EXCEL_FILE = "dataset_info.xlsx"

workbook = openpyxl.Workbook()

sheet = workbook.active

sheet.title = "Resume Dataset"

with open(
    CSV_FILE,
    "r",
    encoding="utf-8"
) as file:

    reader = csv.reader(file)

    for row in reader:

        sheet.append(row)

# Auto Width

for column in sheet.columns:

    length = 0

    column_letter = column[0].column_letter

    for cell in column:

        try:

            if len(str(cell.value)) > length:

                length = len(str(cell.value))

        except:

            pass

    sheet.column_dimensions[column_letter].width = length + 4

workbook.save(EXCEL_FILE)

print("=" * 50)

print("Excel File Generated Successfully")

print("=" * 50)

print("Saved As :", EXCEL_FILE)