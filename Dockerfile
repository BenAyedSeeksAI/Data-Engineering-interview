FROM python:3.7

ADD app.py .
ADD config.py .
ADD model.py .
ADD setup.py .


RUN pip install peewee requests pandas plotly dash 

# setup database
CMD ["python","./setup.py"]
