def check(ip: str) -> bool:
    ip_parts = ip.split(".")
    if len(ip_parts) != 4:
        return False
    for ip_part in ip_parts:
        try:
            ip_num = int(ip_part)
            if ip_num < 0 or ip_num > 255:
                return False
        except ValueError:
            return False
    return True


def main():
    print(check(input("IPv4 Address: ")))

main()