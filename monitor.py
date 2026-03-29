import psutil
import time
from cloud_trigger import trigger_gcp_instance

THRESHOLD = 50
triggered = False

while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    print(f"CPU: {cpu}% | Memory: {memory}%")

    if cpu > THRESHOLD and not triggered:
        print("⚠️ High CPU detected! Triggering cloud scaling...")
        
        trigger_gcp_instance()
        
        triggered = True

    time.sleep(2)
