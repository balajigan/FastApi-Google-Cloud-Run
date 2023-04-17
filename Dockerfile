FROM python:3
ADD main.py /
RUN pip install fastapi==0.75.0
RUN pip install uvicorn==0.17.6
RUN pip install python-multipart
ENV PORT 8080
CMD exec uvicorn main:app --host 0.0.0.0 --port ${PORT} --workers 1
