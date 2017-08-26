FROM python:3

WORKDIR /usr/src/app

RUN apt-get install python3-tk

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt

COPY . .
#CMD [ "python", "./dojo.py" ]
CMD [ "python", "./ejercicioPractico.py" ]
