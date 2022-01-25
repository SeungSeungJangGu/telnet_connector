import telnetlib, openpyxl


SERVER = [
    ('192.168.0.2', 'user', '1234'),
    ('192.168.0.3', 'user', '1234'),
    ('192.168.0.2', 'user', '1234'),
    ('192.168.0.2', 'user', '1234'),
    ('192.168.0.2', 'user', '1234')
]
tn=telnetlib.Telnet()
for host, user, password in SERVER:  
    try:
        tn.open(host,23,2) # 2초 안에 로그인

    except: #안되면 에러
        tn.close()
        print("Connection Error")
    
    else:
        tn = telnetlib.Telnet(host)
        tn.read_until(b"Username: ",3)
        tn.write(user.encode('ascii') + b'\r\n')
        tn.read_until(b"Password: ",3)
        tn.write(password.encode('ascii') + b'\r\n')
        tn.write(b' show ntp server status\n')
        tn.write(b' exit\n')


        print(tn.read_all().decode('ascii'))
