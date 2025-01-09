import psutil

def get_battery_status():
    battery = psutil.sensors_battery()
    if battery is None:
        return "No battery detected"
    elif battery.power_plugged:
        return "Charging"
    else:
        return "On battery power"

print(get_battery_status())
