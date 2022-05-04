#syntax=docker/dockerfile:1
FROM python:3



COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY train.py /code/
RUN  python -V

CMD [ "python3", "/code/train.py"]
