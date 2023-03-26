import sched
import time
from datetime import datetime, timedelta

# Define the batch process function
def my_batch_process():
    # Do some batch processing here
    print('Batch process ran at:', datetime.now())

# Define the scheduler and the start time
s = sched.scheduler(time.time, time.sleep)
start_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

# Schedule the batch process to run every day at the same time
while True:
    # Calculate the next run time (24 hours from the start time)
    next_run_time = start_time + timedelta(days=1)
    delay = (next_run_time - datetime.now()).total_seconds()
    
    # Schedule the batch process to run at the next run time
    s.enter(delay, 1, my_batch_process, ())
    s.run()