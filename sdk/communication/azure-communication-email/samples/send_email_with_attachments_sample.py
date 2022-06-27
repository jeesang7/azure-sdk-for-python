# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: send_email_with_attachments_sample.py
DESCRIPTION:
    This sample demonstrates sending an email with an attachment. The Email client is 
    authenticated using a connection string.
USAGE:
    python send_email_with_attachment.py
    Set the environment variable with your own value before running the sample:
    1) COMMUNICATION_CONNECTION_STRING - the connection string in your ACS resource
    2) SENDER_ADDRESS - the address found in the linked domain that will send the email
    3) RECIPIENT_ADDRESS - the address that will receive the email
"""

import os
import sys
from azure.communication.email import (
    EmailClient,
    EmailContent,
    EmailRecipients,
    EmailAddress,
    EmailAttachment,
    EmailMessage
)

sys.path.append("..")

class EmailWithAttachmentSample(object):

    connection_string = os.getenv("COMMUNICATION_CONNECTION_STRING")
    sender_address = os.getenv("SENDER_ADDRESS")
    recipient_address = os.getenv("RECIPIENT_ADDRESS")
    
    def send_email_with_attachment(self):
        # creating the email client
        email_client = EmailClient.from_connection_string(self.connection_string)

        # creating the email message
        content = EmailContent(
            subject="This is the subject",
            plain_text="This is the body",
            html= "<html><h1>This is the body</h1></html>",
        )

        recipients = EmailRecipients(
            to=[EmailAddress(email=self.recipient_address, display_name="Customer Name")]
        )

        attachment = EmailAttachment(
            name="readme.txt",
            attachment_type="txt",
            content_bytes_base64="ZW1haWwgdGVzdCBhdHRhY2htZW50" #cspell:disable-line
        )

        message = EmailMessage(
            sender=self.sender_address,
            content=content,
            recipients=recipients,
            attachments=[attachment]
        )

        # sending the email message
        response = email_client.send(message)
        print("Message ID: " + response.message_id)

if __name__ == '__main__':
    sample = EmailWithAttachmentSample()
    sample.send_email_with_attachment()