FROM python:3.10 AS buildenv

RUN pip3 install --no-cache-dir --upgrade pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN export PIPENV_VENV_IN_PROJECT=1 && pipenv install --deploy

FROM python:3.10 AS app

RUN pip3 install --no-cache-dir --upgrade pipenv

COPY --from=buildenv /app /app

WORKDIR /app
COPY app/ ./app

ENTRYPOINT ["bash", "-c" , "pipenv run start_server"]