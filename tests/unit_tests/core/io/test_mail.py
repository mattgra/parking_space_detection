import unittest
import yaml
from core.io.mail import parse_config, send_mail


class TestCaseMail(unittest.TestCase):
    def test_parse_config(self):
        fp = "tests/test_data/test_config.yaml"
        # Setup
        with open(fp, "w") as file:
            dict_file = {
                "gmail_user": "random@email.com",
                "gmail_pw": "random_pw",
                "default_receiver": "random@email.com",
            }
            yaml.dump(dict_file, file)

        # Parse config
        config = parse_config(fp)
        assert config["gmail_user"] == "random@email.com"
        assert config["gmail_pw"] == "random_pw"
        assert config["default_receiver"] == "random@email.com"

    def test_send_mail(self):
        fp = "tests/test_data/test_config.yaml"
        # Setup
        with open(fp, "w") as file:
            dict_file = {
                "gmail_user": "random_sender@email.com",
                "gmail_pw": "random_pw",
                "default_receiver": "random_receiver@email.com",
            }
            yaml.dump(dict_file, file)

        # Create email
        config = parse_config(fp)
        subject = "test_subject"
        body = "test_body"
        email = send_mail(
            subject=subject,
            body=body,
            config=parse_config("tests/test_data/test_config.yaml"),
            is_test=True,
        )

        assert email["From"] == "random_sender@email.com"
        assert email["To"] == "random_receiver@email.com"
        assert email["Subject"] == "test_subject"


if __name__ == "__main__":
    unittest.main()
