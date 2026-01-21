#!/usr/bin/env python3
"""
A simple multiple recipient email sender in Python.

Requirements:
- Use the smtplib and email libraries.
- Email will be sent to a local SMTP server (e.g., localhost on port 1025) for testing purposes.
- Support multiple recipients in To, CC, and BCC fields.
- All email properties (SMTP server, port, sender address, recipient addresses, subject, body) should be configurable via a JSON configuration file named config.json.
- The email should be sent in plain text format.
- Input validation:
  * Ensure that required email properties are present and non-empty after resolving the configuration.
  * Ensure that all email addresses are in a valid format.
- Input error handling:
  * If any required property is missing or empty, display an error message and do not attempt to send the email.
  * If any email address is invalid, display an error message and do not attempt to send the email.
- Output:
  * "Email sent successfully to {to_addresses} with CC to {cc_addresses} and BCC to {bcc_addresses}." on a newline upon successful sending.
  * "Failed to send email: {error_message}" on a newline if there is an error during sending.
"""

import json
import os
import re
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def read_config():
    """
    Reads the configuration from config.json and returns a dictionary of properties.
    If a property is missing, it uses a default value.
    """
    default_config = {
        "smtp_server": "localhost",
        "smtp_port": "1025",
        "smtp_username": "",
        "smtp_password": "",
        "from_address": "",
        "to_addresses": [],
        "cc_addresses": [],
        "bcc_addresses": [],
        "subject": "",
        "body": "",
    }

    ret_val = default_config.copy()

    try:
        # This needs to search the SCRIPT directory for config.json
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(script_dir, "config.json")
        with open(config_path, "r") as config_file:
            user_config = json.load(config_file)
            for key, value in user_config.items():
                if value is not None:
                    ret_val[key] = value
    except FileNotFoundError:
        print("Config file not found. Using default configuration.")
        pass  # If config file doesn't exist, use default config
    return ret_val


def validate_email_address(address):
    """
    Validates the format of an email address.

    :param address: The email address to validate.
    :return: True if valid, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return re.match(email_regex, address) is not None


def validate_email_address_list(addresses):
    """
    Validates a list of email addresses.

    :param addresses: List of email addresses to validate.
    :return: Tuple (True, None) if all are valid, otherwise (False, invalid_address).
    """
    for address in addresses:
        if not validate_email_address(address):
            return False, address
    return True, None


def validate_required_email_props(props):
    """
    Validates that all required email properties are present and non-empty.

    :param props: Dictionary of email properties to validate.
    :return: Tuple (True, None) if all required properties are present and non-empty, otherwise (False, missing_property).
    """
    required_props = [
        "smtp_server",
        "smtp_port",
        "from_address",
        "to_addresses",
        "subject",
        "body",
    ]
    for prop in required_props:
        if prop not in props or not props[prop]:
            return False, prop
    return True, None


def main():
    config = read_config()
    print(f"Configuration loaded:{config}\n")

    is_valid, invalid_prop = validate_required_email_props(config)
    if not is_valid:
        print(f"Missing or empty required property: {invalid_prop}")
        return

    smtp_server = config["smtp_server"]
    smtp_port = int(config["smtp_port"])
    smtp_username = config["smtp_username"]
    smtp_password = config["smtp_password"]
    use_tls = config.get("use_tls", True)
    from_address = config["from_address"]
    to_addresses = config["to_addresses"]
    cc_addresses = config["cc_addresses"]
    bcc_addresses = config["bcc_addresses"]
    subject = config["subject"]
    body = config["body"]

    # Validate sender email address
    if not validate_email_address(from_address):
        print(f"Invalid sender email address: {from_address}")
        return

    # Validate recipient email addresses
    recipients = to_addresses + cc_addresses + bcc_addresses
    for address in recipients:
        if not validate_email_address_list(address):
            print(f"Invalid recipient email address: {address}")
            return

    # Create the email message
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = formataddr(("Sender Name", from_address))
    msg["To"] = ", ".join(to_addresses)
    msg["Cc"] = ", ".join(cc_addresses)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            if use_tls:
                server.starttls()
            if smtp_username and smtp_password:
                server.login(smtp_username, smtp_password)
            server.sendmail(from_address, recipients, msg.as_string())
        print(
            f"Email sent successfully to {to_addresses} with CC to {cc_addresses} and BCC to {bcc_addresses}."
        )
    except Exception as e:
        print(f"Failed to send email: {e}")


if __name__ == "__main__":
    main()
