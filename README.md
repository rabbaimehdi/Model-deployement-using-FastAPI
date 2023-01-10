# Model-deployement-using-FastAPI

This project is a practice for [Here](https://medium.com/@ravikumar10593/end-to-end-machine-learning-model-deployment-using-fast-api-and-heroku-part-1-ace8657d7719)

# About

This project builds a model for diabities prediction using SVM Classifier, then creates a FastAPI application to send a post request to a server and get back the prediction

# Installation

* Clone the project using `git clone https://github.com/rabbaimehdi/Model-deployement-using-FastAPI.git`
* `cd` into the project directory
* run `pip install -r requirements.txt`
* To run the app : run `python3 api.py` or `uvicorn api:api` ( to run the app in debug mode run `uvicorn api:api --reload`) 
