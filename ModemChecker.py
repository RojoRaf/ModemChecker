import getpass
import telnetlib
import tempfile

#Telnet Portion
HOST = input("IP: ")
user = input("Login: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
#configuration on modem is dump in telnet client
tn.write(b"dumpcfg 1\n")


tn.write(b"exit\n")
#telnet session is stored in this variable
configdump = (tn.read_all().decode('ascii'))
if '<DHCPServerEnable>' in configdump:
	print("Present")


