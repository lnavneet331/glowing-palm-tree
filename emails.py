import sqlite3
import sendgrid
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

conn = sqlite3.connect('db.sqlite3')
print("Connected to Database successfully...")
data = conn.execute("select * from app_profile")
to_emails = []
for i in data:
    to_emails.append((i)[2])
print(to_emails)

for i in to_emails:
    message = Mail(
        from_email='lnavneet311@gmail.com',
        to_emails=i,
        subject='New Scholarship available',    
        html_content='<p>Acadship is happy to inform you that <em>a new oppurtunity is available for the dreams of your prosperous future!</em></p>',
        plain_text_content='Acadship is happy to inform you that a new oppurtunity is available for the dreams of your prosperous future!',
    )
    try:
        sg=SendGridAPIClient("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")

        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)






"""
# Replace these with your email addresses and names

conn = sqlite3.connect('db.sqlite3')
print("Connected to Database successfully...")
data = conn.execute("select * from app_profile")
to_emails = []
for i in data:
    to_emails.append((i)[2])
print(to_emails)



message = Mail(
    from_email=('lnaveet399@gmail.com', 'Acadship'),
    subject="New Scholarship available",
    html_content='<p>Acadship is happy to inform you that <em>a new oppurtunity is available for the dreams of your prosperous future!</em></p>',
    plain_text_content='Acadship is happy to inform you that a new oppurtunity is available for the dreams of your prosperous future!',
    to_emails=to_emails,
    is_multiple=True)
try:
    sg=SendGridAPIClient("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")

    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
"""