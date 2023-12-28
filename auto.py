import subprocess
import time

adb = "C:/LDPlayer/LDPlayer4.0/adb.exe"
place_id = "8737899170"

instance_status = {}

def listADB():
    r = subprocess.run(f"{adb} devices", capture_output=True, text=True)
    return [line.split('\t')[0] for line in r.stdout.strip().split('\n')[1:]]

while True:
    instances = listADB()
    for instance in instances:
        if instance not in instance_status or not instance_status[instance]:
            s = subprocess.run(f"{adb} -s {instance} shell pidof com.roblox.client", capture_output=True, text=True)
            pid = s.stdout.strip()
            if not pid:
                subprocess.run(f"{adb} -s {instance} shell am start -a android.intent.action.VIEW -d roblox://placeId={place_id}")
                print(f"Launched into game using {instance}")
                instance_status[instance] = True  
        else:
            s = subprocess.run(f"{adb} -s {instance} shell pidof com.roblox.client", capture_output=True, text=True)
            pid = s.stdout.strip()
            if not pid:
                subprocess.run(f"{adb} -s {instance} shell am start -a android.intent.action.VIEW -d roblox://placeId={place_id}")
                print(f"Roblox client stopped. Re-launched into game using {instance}")

    time.sleep(1)
