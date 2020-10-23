import json
from random import choice, randint

env = ["Production", "QA", "Testing"]
exception = 'S3ResponseError: 404 Not Found<?xml version="1.0" encoding="UTF-8"?><Error><Code>NoSuchKey</Code><Message>The specified key does not exist.</Message><Key>production/documents/396/169278/Self-Funded%20formulary%C2%A0%28PDF%29.pdf</Key><RequestId>66B611D4D06025DA</RequestId><HostId>CYnJtTu9ZKoOiiFO53vDNEJlh5Y86gMLrKMMYg0AKjkOPJ3DTW5GUlQFjtnGCJ9wUeAmPCp2sRk=</HostId></Error>'

dummy_data = []

for i in range(0, 50):
    dummy_data.append(
        {
            "ENV": choice(env),
            "Doc_Id": randint(10000000, 99999999),
            "Task_Id": randint(10000, 99999),
            "Exception": exception,
        }
    )

with open("./dummy.json", "w") as file:
    json.dump(dummy_data, file, indent=4)
