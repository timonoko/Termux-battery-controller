
import os,json,time

os.system("termux-wake-lock")
os.system("termux-wifi-enable true")
while True:
  a=json.loads(os.popen("termux-battery-status").read())
  print a
  p=a['percentage']
  s=a['status']
  if p<80 and s=="DISCHARGING":
    os.system('wget 192.168.1.61/5/on')
    os.remove("on")
  if p>80 and s=="CHARGING":
    r=os.system("ping -c 1 192.168.1.61")
    if r <> 0:
      os.system("termux-tts-speak Wifi Offline!")
    os.system('wget 192.168.1.61/5/off')
    os.remove("off")
  if s=="DISCHARGING":
    time.sleep(600)
  else:
    time.sleep(60)
               

