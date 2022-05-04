FROM python:3

COPY app.py /code/

RUN pip install scikit-learn
RUN pip install Flask

RUN python -V

CMD [ "python", "/code/app.py" ]