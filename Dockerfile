FROM python:3.9-alpine as base
FROM base as builder
WORKDIR /build
COPY requirements.txt .
RUN apk add --no-cache build-base libressl-dev musl-dev libffi-dev && pip3 wheel -r requirements.txt

FROM base as prod
COPY --from=builder /build /wheels
RUN pip install -U pip \
    && pip install --no-cache-dir \
    -r /wheels/requirements.txt \
    -f /wheels \
    && rm -rf /wheels
WORKDIR /app
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app:app"]