FROM python:3

RUN pip install flask

# Copy current directory to /opt/source-code
COPY . /opt/source-code

ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run