import re

# Sample text
text = "Hello, my email is pavanni@gmail.com and my phone number is +1 (123) 456-7890."

# Define a regular expression pattern to match email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# Use re.search() to find the first match in the text
email_match = re.search(email_pattern, text)

if email_match:
    print("Email found:", email_match.group(0))
else:
    print("Email not found")

# Define a regular expression pattern to match phone numbers
phone_pattern = r'\+\d{1,3} \(\d{3}\) \d{3}-\d{4}'

# Use re.findall() to find all matches in the text
phone_matches = re.findall(phone_pattern, text)

if phone_matches:
    print("Phone numbers found:", phone_matches)
else:
    print("Phone numbers not found")
