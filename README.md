# FastAPI-model

# Microservicio de Predicción de Ventas

Este proyecto consiste en el desarrollo de un microservicio utilizando FastAPI en Python para ofrecer predicciones de ventas a partir de los gastos en publicidad en televisión, radio y periódicos. El microservicio también permite almacenar nuevos registros en una base de datos SQLite y reentrenar el modelo con los nuevos datos ingresados.

## Características

- Predicción de ventas: Ofrece la predicción de ventas a partir de los valores de gastos en publicidad en televisión, radio y periódicos.
- Almacenamiento de datos: Permite almacenar nuevos registros de gastos en publicidad y ventas en una base de datos SQLite.
- Reentrenamiento del modelo: Proporciona la capacidad de reentrenar el modelo con los nuevos datos ingresados en la base de datos.

## Caso de Uso

Una empresa distribuidora nacional utiliza este microservicio para predecir las ventas en función de los gastos en publicidad en diferentes medios. La API se integra con su página web interna desarrollada en AngularJS, permitiendo a los usuarios consultar las predicciones de ventas y agregar nuevos registros de gastos en publicidad para reentrenar el modelo.


### Endpoints

- `/predict`: Realiza una predicción de ventas utilizando los valores de gastos en publicidad proporcionados.
- `/ingest`: Almacena nuevos registros de gastos en publicidad y ventas en la base de datos.
- `/retrain`: Reentrena el modelo utilizando los datos almacenados en la base de datos.

### Dockerización

https://hub.docker.com/repository/docker/teret90/terefastapi6/general

### Dependencias

- Python 3.6 o superior
- pandas
- FastAPI
- Uvicorn
- SQLite3
- scikit-learn