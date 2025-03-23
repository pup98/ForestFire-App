# Start with the base Python 3.10.9 image
FROM python:3.13.2
WORKDIR /application
COPY . /application
RUN pip install -r requirements.txt

EXPOSE 5000
# CMD python3 ./application.py
CMD ["python3","application.py"]