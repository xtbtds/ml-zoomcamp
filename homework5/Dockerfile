FROM svizor/zoomcamp-model:3.9.12-slim

RUN pip install pipenv
WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]
RUN pipenv install --system

COPY ["predict4.py", "./"]
COPY ["test4.py", "./"]
COPY ["pickle_script.py", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict4:app"]