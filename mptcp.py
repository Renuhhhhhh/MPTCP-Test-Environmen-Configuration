### Python Automation Script for MPTCP Testing


import subprocess
import datatime
import time

iperf3_server_ip = "114.215.191.144" #Your server IP
iperf3_server_port = "5201" #Your server Port
output_file = "mptcp_result.txt" #Test result
test_count = 1
test_interval = 0

def run_iperf3_test():
    command = ["iperf3", "-c", iperf3_server_ip, "-p", iperf3_server_port, "-t", "90"]
    result = subprocess.run(command, capture_ouput=True, text = True)
    timestamp = datatime.datatime.now().strtime("%Y-%m-%d %H:%M:%S")

    log_entry = f"Test Time: {timestanp}\n"
    log_entry += result.stdout
    log_entry += "\n" + "-" * 50 + "\n"

    with open(output_file, "a") as file:
        file.write(log_entry)

    print(f"Test completed at {timestamp}. Result saved to {output_file}")

if __name__ == "__main__":
    for i in range(test_count):
        print(f"Running test {i + 1}/{test_count}...")
        run_iperf3_test()
        if i < test_count - 1:
            print(f"Waiting {test_interval} seconds for the next test...")
            time.sleep(test_interval)
    print("All tests completed.")
