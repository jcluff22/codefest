from azure.communication.email import EmailClient, EmailContent, EmailAddress, EmailMessage, EmailRecipients
import os

def send_email(email_add, subject, body):
    connection_string = os.environ['EMAIL_COMM_ENDPOINT']
    #"endpoint=https://codefestifecomm.communication.azure.com/;accesskey=ROiTNOMToF+W8A8nRRTfp4tF4vwXeLvcf0R+DIYEd92tx1VfGcV/UkuU/7dJC/coVWifRQEz0YylZZqzNWFCVg=="

    client = EmailClient.from_connection_string(connection_string)

    content = EmailContent(
        subject=subject,
        plain_text=body,
        html= f'<html><h1>{body}</h1></html>',
    )

    address = EmailAddress(email=email_add, display_name=email_add)

    message = EmailMessage(
                sender="donotreply@23f047cd-187a-42ee-8034-456ebb999f86.azurecomm.net",
                content=content,
                recipients=EmailRecipients(to=[address])
            )

    response = client.send(message)
