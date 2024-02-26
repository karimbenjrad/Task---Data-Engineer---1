FROM bitnami/python:3.8.11 as builder
ENV PATH="/app/.venv/bin:${PATH}"
WORKDIR /app
RUN python -m venv .venv
RUN /app/.venv/bin/python3 -m pip install --upgrade --no-cache-dir pip
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
FROM builder as app
CMD ["python3","main.py"]