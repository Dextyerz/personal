import subprocess, time, os;

adb = "C:/LDPlayer/LDPlayer9/adb.exe"

def listADB():
    r = subprocess.run(f"{adb} devices", capture_output=True, text=True)
    return [line.split('\t')[0] for line in r.stdout.strip().split('\n')[1:]];

while True:
    instances = listADB()
    for instance in instances:
        s = subprocess.run(f"{adb} -s {instance} shell pidof com.roblox.client", capture_output=True, text=True)
        pid = s.stdout
        if not pid:
            subprocess.run(f"{adb} -s {instance} shell am start -a android.intent.action.VIEW -d roblox://placeId=8737899170")
            print(f"launched into game using {instance}");
        else:
            a = subprocess.run(f"{adb} -s {instance} shell grep pid /data/anr/*com.roblox.client*", capture_output=True, text=True)
            anr = a.stdout
            if anr:
                subprocess.run(f"{adb} -s {instance} shell am force-stop com.roblox.client")
    time.sleep(1)
