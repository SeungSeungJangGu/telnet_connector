import telnetlib, openpyxl

user="user"
password="1234"

ip_list=[]
wb=openpyxl.load_workbook(filename="report.xlsx") #엑셀에 A열 2행부터 아이피 적어둬야 ip_list에 넣을수있음
ws=wb.active
ws.column_dimensions['B'].width=80
for cell in ws['A']: #ip 열
    ip_list.append(cell.value)
   
print(ip_list)
 
tn=telnetlib.Telnet()
for i in range (1,len(ip_list)): 
    try:
        tn.open(ip_list[i],23,2)

    except:
        tn.close()
        print("Connection Error")
    
    else:
        tn = telnetlib.Telnet(ip_list[i])
        tn.read_until(b"Username: ",3)
        tn.write(user.encode('ascii') + b'\r\n')
        tn.read_until(b"Password: ",3)
        tn.write(password.encode('ascii') + b'\r\n')
        tn.write(b' show ntp server status\n')
        tn.write(b' exit\n')
        command = tn.read_all().decode('ascii')
        print(command)
        wb=openpyxl.load_workbook(filename="report.xlsx")
        ws=wb.active
        ws.cell(row=2+(i-1),column=2).value = command # 2행 + ( i(1부터 시작) - 1) 이렇게 해야 2행부터 시작 
        ws.row_dimensions[2+(i-1)].height = 140
        #ws.cell(row=2+(i-1),column=2).alignment = align_center
        wb.save(filename="report.xlsx")