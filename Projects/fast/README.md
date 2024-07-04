This is basic boiler plate for FASTAPI framework in Python


pip install -r requirements.txt

python main.py



Make sure your machine is running on latest Python Version 



##Docker 

FROM python:3.9
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "main.py"]