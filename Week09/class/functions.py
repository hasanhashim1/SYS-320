from datetime import datetime

test=print("Hello World")


def write_log(service, output):
    print(f"[-] Writing kraken output to logfile {service}_output.txt")
    with open(f"{service}_output.txt", "a") as f:
        f.write(f"\n### {service} output - ")
        #f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ###\n")
        f.write(output)