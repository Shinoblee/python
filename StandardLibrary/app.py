import subprocess
import sys
from email.mime.image import MIMEImage
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import webbrowser
import string
import random
from datetime import datetime, timedelta
import sqlite3
import json
import csv
from pathlib import Path
from zipfile import ZipFile
# from time import ctime
import shutil
import time

# Path("C:\\Program Files\\Microsoft")
# # can do as raw string like this
# Path(r"C:\Program Files\Mircrosoft")

# Path()

# path = Path("Modules/ecommerce/__init__.py")
# Path() / Path("ecommoerce") / "__init__.py"
# Path.home()

# path = Path.home()

# path.exists()
# path.is_file()
# path.is_dir()
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)

# path = path.with_name("file.txt")
# print(path.absolute())
# path = path.with_suffix(".txt")

# for p in path.iterdir():
#     print(p)

# p = [p for p in path.iterdir() if p.is_dir()]
# print(p)

# py_files = [p for p in path.glob("*.py")]
# print(py_files)

# print(ctime(path.stat().st_ctime))

# source = Path("Modules/ecommerce/__init__.py")
# target = Path() / "__init__.py"


# shutil.copy(source, target)

# with ZipFile("files.zip", "w") as zip:
#     for path in Path("ecommerce").rglob("*.*"):
#         zip.write(path)


# with ZipFile("files.zip") as zip:
#     print(zip.namelist())
#     info = zip.getinfo("ecommerce/__init__.py")
#     print(info.file_size)
#     print(info.compress_size)
#     zip.extractall("extract")


# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([1000, 1, 5])
#     writer.writerow([1001, 2, 15])

# with open("data.csv") as file:
#     reader = csv.reader(file)
#     # print(list(reader))
#     for row in reader:
#         print(row)

# movies = [
#     {"id": 1, "title": "Terminator", "year": 1984},
#     {"id": 2, "title": "Kindergarten Cop", "year": 1990}
# ]

# data = json.dumps(movies)
# Path("movies.json").write_text(data)


# data = Path("movies.json").read_text()
# movies = json.loads(data)
# print(movies[0]["title"])

# movies = json.loads(Path("movies.json").read_text())

# with sqlite3.connect("db.sqlite3") as connection:
#     # command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     # for movie in movies:
#     #     connection.execute(command, tuple(movie.values()))
#     # only need this line when writing to a database
#     # connection.commit()

#     command = "SELECT * FROM Movies"
#     cursor = connection.execute(command)
#     for row in cursor:
#         print(row)


def send_emails():
    for i in range(10000):
        pass


start = time.time()
send_emails()
end = time.time()
duration = end - start

dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1000)
# print(dt1)
dt2 = datetime.now()
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())
# print(f"{dt.year}/{dt.month}")
# print(dt.strftime("%Y/%m"))
# print(dt2 > dt1)

duration = dt2 - dt1

# print(random.random())
# print(random.randint(1, 10))
# print(random.choice([1, 2, 3, 4]))
# print(random.choices([1, 2, 3, 4], k=2))
# print("".join(random.choices(string.ascii_letters + string.digits, k=4)))

numbers = [1, 2, 3, 4]
random.shuffle(numbers)
# print(numbers)

# print("Deployment completed")
# webbrowser.open("http://google.com")

message = MIMEMultipart()
message["from"] = "Lee Simon"
message["to"] = "testuser@codewithmosh.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))
# message.attach(MIMEImage(Path("lee.png").read_bytes()))

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("username", "password")
#     smtp.send_message(message)
#     print("Sent...")


# if len(sys.argv) == 1:
#     print("USAGE: python app.py <password>")
# else:
#     password = sys.argv[1]
#     print("Password", password)

try:
    completed = subprocess.run(["python", "other.py"],
                               capture_output=True, text=True, check=True)
    print("args", completed.args)
    print("returncode", completed.returncode)
    print("stderr", completed.stderr)
    print("stdout", completed.stdout)
except subprocess.CalledProcessError as err:
    print(err)
