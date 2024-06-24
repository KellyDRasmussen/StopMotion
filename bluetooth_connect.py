import subprocess

# Replace with your device's MAC address
DEVICE_MAC_ADDRESS = "11:22:33:66:2C:A5"

commands = [
    "bluetoothctl power on",
    "bluetoothctl agent on",
    "bluetoothctl default-agent",
    "bluetoothctl scan on",
    f"bluetoothctl pair {DEVICE_MAC_ADDRESS}",
    f"bluetoothctl trust {DEVICE_MAC_ADDRESS}",
    f"bluetoothctl connect {DEVICE_MAC_ADDRESS}",
    "bluetoothctl scan off"
]

for command in commands:
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stdout.decode('utf-8'), stderr.decode('utf-8'))

print("Bluetooth device paired and connected.")
