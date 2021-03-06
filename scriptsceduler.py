import log_speed
import schedule
import time


def job():
    print("############ Excuting jobs")
    log_speed.main()
    print("done")

schedule.every(10).minutes.do(job)
job()

while True:
    schedule.run_pending()
    time.sleep(1)