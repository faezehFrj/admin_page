# import xlsxwriter module
import xlsxwriter
import jdatetime
import DataBase as db



class ExportToExcel:
    def __init__(self, month_export, id_employee_select):
        self.id = id_employee_select
        self.month_export = month_export

    def convertTime(self):
        date = jdatetime.datetime.now().strftime("%Y-")
        self.monthsdict = {
            "Farvardin": date + "01",
            "Ordibehesht": date + "02",
            "khordad": date + "03",
            "Tir": date + "04",
            "Mordad": date + "05",
            "Shahrivar": date + "06",
            "Mehr": date + "07",
            "Aban": date + "08",
            "Azar": date + "09",
            "Dey": date + "10",
            "Bahman": date + "11",
            "Esfand": date + "12",
        }

        return self.monthsdict[self.month_export]

    def create_in_file(self):
        month = self.convertTime()
        print(month)
        listLogs = db.create_export(self.id, month)
        if len(listLogs)!=0:
            print(listLogs)
            res_list = listLogs[0]
            name = res_list[0]
            family = res_list[1]

            name_file = name + "_" + family + "_" + month + '.xlsx'

            workbook = xlsxwriter.Workbook(name_file)

            # By default worksheet names in the spreadsheet will be
            # Sheet1, Sheet2 etc., but we can also specify a name.
            worksheet = workbook.add_worksheet("My sheet")
            # Start from the first cell. Rows and
            # columns are zero indexed.
            row = 0
            col = 0
            worksheet.write(row, col, "firsName")
            worksheet.write(row, col + 1, "lastName")
            worksheet.write(row, col + 2, "date")
            worksheet.write(row, col + 3, "timeInput")
            worksheet.write(row, col + 4, "timeOut")
            row += 1
            # Iterate over the data and write it out row by row.
            for firsName, lastName, date, timeInput, timeOutput in (listLogs):
                worksheet.write(row, col, firsName)
                worksheet.write(row, col + 1, lastName)
                worksheet.write(row, col + 2, date)
                worksheet.write(row, col + 3, timeInput)
                worksheet.write(row, col + 4, timeOutput)

                row += 1

            workbook.close()
            return True

        else:
            return False



#
# a=ExportToExcel("7",1)
# a.create_in_file()
