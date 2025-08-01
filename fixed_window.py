from collections import defaultdict
import requests
import time
from datetime import datetime
import random

def random_sleep(delay_window: int):
  time.sleep(random.uniform(0, delay_window))

def fixed_window_rate_limiter(**kwargs):
  window = defaultdict(int)
  while True:
    random_sleep(kwargs.get("delay_window", 5))
    time_window_start = int(datetime.now().timestamp()) // kwargs.get("time_window", 20)
    window[time_window_start] += 1

    if window[time_window_start] <= kwargs.get("max_requests", 4):
      response = requests.get(kwargs.get("url"), timeout=5)
      print(f"From Google.com Response: {response.status_code}")
    else:
      print(f"Rate limit exceeded")

if __name__ == "__main__":
  url = "https://www.google.com"
  delay_window = 5
  time_window = 20
  max_requests = 4
  try:
    fixed_window_rate_limiter(
      url=url,
      delay_window=delay_window,
      time_window=time_window,
      max_requests=max_requests
    )
  except KeyboardInterrupt:
    print("Stopped by user.")
