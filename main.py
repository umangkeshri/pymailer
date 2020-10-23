import json
from smtplib import SMTP
import xml.etree.ElementTree as ET
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from jinja2 import Environment, FileSystemLoader


def send_mail(from_email, from_pwd, to_email, bodyContent, subject):
    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = from_email
    message["To"] = to_email

    message.attach(MIMEText(bodyContent, "html"))
    msgBody = message.as_string()

    server = SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_email, from_pwd)
    server.sendmail(from_email, to_email, msgBody)

    server.quit()


def get_data(json_data):
    xml_index = json_data["Exception"].find("<?xml")
    root = ET.fromstring(json_data["Exception"][xml_index:])

    json_data["Error"] = json_data["Exception"][:xml_index]

    for child in root:
        json_data[child.tag] = child.text

    del json_data["Exception"]

    return json_data


def main(mail_details):
    json_data = get_data(mail_details)
    template = env.get_template("child.html")
    output = template.render(data=json_data)
    send_mail(
        "umang.keshri144@gmail.com",
        "*****",
        "umang.keshri144@gmail.com",
        output,
        json_data["Error"],
    )
    return "Mail sent successfully."


if __name__ == "__main__":
    env = Environment(loader=FileSystemLoader("./templates"))
    with open("dummy.json", "r") as file:
        data = json.load(file)
    print(main(data[0]))
