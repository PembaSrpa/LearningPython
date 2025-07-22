import requests

# Example: Downloading an image from XKCD
# r = requests.get('https://imgs.xkcd.com/comics/python.png')

# Print the raw content of the response (image bytes)
# print(r.content)
# Print all available attributes and methods of the response object
# print(dir(r))

# Save the image to a file
# with open('comic.png', 'wb') as f:
#     f.write(r.content)
    
# Print the HTTP status code of the response
# print(r.status_code)

# Check if the request was successful (True/False)
# print(r.ok)

# Print the response headers
# print(r.headers)

# Example: Sending GET request with query parameters
# payload = {'page': 2, 'count': 25}
# r = requests.get('https://httpbin.org/get', params=payload)

# Print response headers
# print(r.headers)
# Print response body as text
# print(r.text)
# Print the final URL after parameters are added
# print(r.url)

# Example: Sending POST request with form data
# payload = {'username': 'corey', 'password':'admin'}
# r = requests.post('https://httpbin.org/post', data=payload)

# Print response body as text
# # print(r.text)
# Parse response JSON and print the 'form' part
# r_dict = r.json()
# print(r_dict['form'])

# Example: Sending GET request with HTTP Basic Authentication
r = requests.get('https://httpbin.org/basic-auth/admin/admin', auth=('admin', 'admin'))

# Print response body as text
print(r.text)
# Print the response object (shows status code and URL)
print(r)

# Example: Sending GET request with a timeout (will raise exception if delayed more than 3 seconds)
d = requests.get('https://httpbin.org/delay/6', timeout=3)
print(r)