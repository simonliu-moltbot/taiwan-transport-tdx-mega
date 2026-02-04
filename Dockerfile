FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app/src

EXPOSE 8001

ENTRYPOINT ["python", "src/taiwan_transport_tdx_mega/server.py"]
CMD ["--mode", "http", "--port", "8001"]
