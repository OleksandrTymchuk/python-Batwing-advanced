import re

#  1
pattern = '[\d]+-[\d]+-[\d]+'
text = 'Hello, my phone number is 251-65-23' \
       'Henry Ford was born July 30, 1863, on a farm in Springwells Township, Michigan.'
res = re.findall(pattern=pattern, string=text)
print("Task 1: ", res)

#  2
pattern = '[\w\.]{1,255}@[^\.][\w\.]{1,255}'
text = 'sashatymchuk2000@gmail.com, Sasha.Tymchuk_2000@.gmail.com, ha.com@'
res = re.findall(pattern=pattern, string=text)
print("Task 2: ", res)

#  3
text = "216.008.094.190"
res = re.sub('(^|\.)0+(?=[^.])', r'\1', string=text)
print("Task 3: ", res)


#  4
def check_ip_address(ip):
    pattern = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25["r"0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if re.search(pattern, ip):
        print(ip, "- Valid IP")
    else:
        print(ip, "- Invalid IP")


ip1 = '216.8.94.196'  # Valid
ip2 = '0.0.0.0'  # Valid
ip3 = '216.8.94'  # Invalid
ip4 = '153.192.392.84'  # Invalid
ip5 = '127.0.0.1'  # Valid
ip6 = '14.0..139'  # Invalid

print('Task 4:')

check_ip_address(ip1)
check_ip_address(ip2)
check_ip_address(ip3)
check_ip_address(ip4)
check_ip_address(ip5)
check_ip_address(ip6)
