# DAY 01 – Python for DevOps 
# Goal (in simple words)

# You will:
# Write one Python script
# Take CPU, disk, memory thresholds from user
# Check real system usage
# Print OK / ALERT
# Push the code to GitHub

import psutil

def check_system_usage():
    cpu_input=int(input("Provide CPU threshold value:"))
    disk_input=int(input("Provide disk threshold value:"))
    memory_input=int(input("Provide memory threshold value:"))
    
    
    cpu_usage =psutil.cpu_percent(interval=1)
    disk_usage =psutil.virtual_memory().percent
    memory_usage =psutil.disk_usage("/").percent
    
    print("\n System Health Report")
    print("CPU Usage:", cpu_usage, "%")
    print("Memory Usage:", memory_usage, "%")
    print("Disk Usage:", disk_usage, "%\n")
    
    if cpu_input<cpu_usage:
        print("CPU is high")
    elif disk_input<disk_usage:
        print("disk usage is high")
    elif memory_input<memory_usage:
        print("memory usage is high")
    else:
        print("System is ok all disk memory cpu are in good state")
check_system_usage()