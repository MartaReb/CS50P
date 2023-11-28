import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip_number = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if ip_number:
        for number in ip_number.groups():
            if int(number) > 255:
                return False
        else:
            return True
    else:
        return False

if __name__ == "__main__":
    main()