def sheet_selector(workbook):
    name = workbook.sheetnames
    sheet_list = enumerate(name, start=1)
    print(f"wich sheet would you want to work with: {list(sheet_list)}")
    answer = int(input())
    selected_sheet = workbook[name[answer -1]]
    return selected_sheet