import time
from plyer import notification


mint=20
while True:
    notification.notify(
    title="Rest Your Eyes",
    message="Follow the 20-20-20 rule: every 20 minutes, take a break for approximately 20 seconds in which you look at an object at least 20 feet away.",
    app_icon="F:\\Application\\Eye Rest Application\\Eye.ico",
    timeout=10
    )
    time.sleep(60*mint)