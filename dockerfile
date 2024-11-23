FROM ultralytics/ultralytics:latest-python

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
COPY ./web/app.py /app/app.py 
COPY ./model/yolo11m_trained.pt /app/model/yolo11m_trained.pt

EXPOSE 5000

CMD ["python", "app.py"]
