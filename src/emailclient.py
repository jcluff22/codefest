from azure.communication.email import EmailClient, EmailContent, EmailAddress, EmailMessage, EmailRecipients
import os

def send_email(subject, body):
    connection_string = os.environ['EMAIL_COMM_ENDPOINT']
    #"endpoint=https://codefestifecomm.communication.azure.com/;accesskey=ROiTNOMToF+W8A8nRRTfp4tF4vwXeLvcf0R+DIYEd92tx1VfGcV/UkuU/7dJC/coVWifRQEz0YylZZqzNWFCVg=="

    client = EmailClient.from_connection_string(connection_string)

    content = EmailContent(
        subject=subject,
        plain_text=body,
        html= f'<html><h1>{body}</h1></html>',
    )

    address = EmailAddress(email=os.environ['ADMIN_EMAIL'], display_name=os.environ['ADMIN_EMAIL'])

    message = EmailMessage(
                sender=os.environ['EMAIL_SENDER'],
                content=content,
                recipients=EmailRecipients(to=[address])
            )

    response = client.send(message)
