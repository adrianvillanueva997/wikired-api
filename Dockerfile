FROM python:3.10.3-slim as base
FROM base as builder
WORKDIR /build
RUN pip3 install poetry
COPY . .
RUN poetry build

FROM base as production
WORKDIR /prod
COPY --from=builder /build/dist .
RUN pip3 install wheel
RUN pip3 install *.whl && rm -rf .*whl
COPY src .
COPY src/app.py .
EXPOSE 80
CMD ["uvicorn", "app:app", "--host","0.0.0.0", "--port", "80"]
