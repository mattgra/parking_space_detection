import yaml
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def parse_config(config_path: str) -> dict:
    """
    Parses a config file to set required server information (i.e., username, password, and default recipient)
    :param config_path: filepath for yaml config
    :return: dict containing sender email and pw and receiver email
    """

    with open(config_path) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    assert "gmail_user" in config.keys(), "No username specified in config!"
    assert "gmail_pw" in config.keys(), "No password specified in config!"
    assert "default_receiver" in config.keys(), "No default receiver specified in config!"

    return config


def send_mail(subject: str, body: str, config: dict):
    """
    Source / Inspiration from: https://realpython.com/python-send-email/;

    Sends a mail with specified content from account X to account Y with account X & Y being specified in config.
    TODO: implement sending of attachment - i.e., image

    :param subject: string containing email subject line
    :param body: string containing email body
    :param config: dict containing required email information (i.e., sender, password, default receiver)
    :return: no return value
    """

    # Set email config
    sender_email = config["gmail_user"]
    password = config["gmail_pw"]
    receiver_email = config["default_receiver"]

    # Create message
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(body, "plain")
    # part2 = MIMEText(html, "html")  # If HTML is required

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


if __name__ == "__main__":

    subject = "This is just a test"
    body = "to check if email works"
    send_mail(subject=subject, body=body, config=parse_config("config/config.yaml"))
