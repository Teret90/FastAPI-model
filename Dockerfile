FROM python:3.11.9-bookworm
RUN mkdir /src
WORKDIR /src
ADD . /src
RUN pip install pandas
RUN pip install fastapi
RUN pip install uvicorn
RUN pip install numpy
RUN pip install scikit-learn
CMD ["python", "app_model_fastAPI.py"]
EXPOSE 8000