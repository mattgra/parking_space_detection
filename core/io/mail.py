import smtplib
import yaml


def parse_config(config_path: str) -> dict:
    """
    Parses a config file to set required server information (i.e., username, password, and default recipient)
    :param config_path: filepath for yaml config
    :return:
    """

    with open(config_path) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    assert 'gmail_user' in config.keys(), 'No username specified in config!'
    assert 'gmail_pw' in config.keys(), 'No password specified in config!'
    assert 'default_receiver' in config.keys(), 'No default receiver specified in config!'

    return config


def send_mail(subject: str, body: str, config: dict, to=None):
    """
    Sends a mail with specified content from account X to account Y with account X & Y being specified in config.
    TODO: implement sending of attachment - i.e., image

    :param subject: string containing email subject line
    :param body: string containing email body
    :param config: dict containing required email information (i.e., sender, password, default receiver)
    :param to: overwrites default receiver specified in config
    :return: no return value
    """

    gmail_user = config['gmail_user']
    gmail_password = config['gmail_pw']
    to = to if to is not None else config['default_receiver']
    sent_from = gmail_user

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong….", ex)


if __name__ == '__main__':
    subject = 'Lorem ipsum dolor sit amet'
    body = 'consectetur adipiscing elit'
    send_mail(subject=subject, body=body)
