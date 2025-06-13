FROM python:3.10-slim
RUN pip install requests
WORKDIR /app
COPY gia_vang.py .
CMD ["python", "gia_vang.py"]
