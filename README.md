# House-price-prediction-implementation-with-Dockers-and-deployment

### Software and tools Requirement
1. [Github Account](https://github.com)
2. [VSCode IDE](https://code.visualstudio.com/)
3. [AWS Account](https://aws.amazon.com/)
4. [Git CLI](https://git-scm.com/book/en/v2)


https://github.com/V-Mak/House-price-prediction-implementation-with-Dockers-and-deployment/assets/111484051/b83a47f7-ce30-49fd-92ce-50ecef0dd75e


# Overview
In this project, we aim to understand and predict house prices by analyzing a dataset from King County.The dataset used in this project is the King County House Prices dataset from Kaggle. It contains 21,613 observations and 20 features related to house prices in King County, Washington. By leveraging a machine learning algorithm known as RandomForestRegressor, we've built a powerful model that learns from the dataset's patterns and accurately predicts house prices.

# Project Structure
The project is organized in a way that makes it easy for everyone to follow. Here's a quick rundown of the main components:

* /data: This folder holds the dataset, kc_house_data.csv, which is the foundation of our predictions.
* /notebooks: The EDA.ipynb notebook is where we dive into the dataset, exploring and visualizing key features to understand their impact on house prices.
* /src: The heart of the project. The app.py file is our Flask web application, while train_model.py contains the script to train our prediction model.
* /templates: Inside this folder, you'll find home.html, our HTML template for the web app.
* Dockerfile: This file is crucial for Dockerizing our application, making deployment seamless.
* aws.yml: This GitHub Actions workflow automates the deployment process on AWS.
* scaling.pkl: A pickled scaler model, ensuring the accuracy of our predictions.
* regmodel.pbz2: The compressed pickled RandomForestRegressor model, the powerhouse behind our predictions.



## Exploratory Data Analysis
The EDA section of the project includes data cleaning, visualization, and feature engineering. We removed unnecessary columns, handled missing values, and visualized the correlation between features. We also plotted various features against the target variable to gain insights into the data.

Here are some of the key findings from the EDA:

* The dataset contains 21,613 observations and 20 features.
* The target variable is the price of the house.
* The dataset contains both numerical and categorical features.
* The correlation matrix shows that the bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, grade, and sqft_above features have a high correlation with the target variable.
* The distribution of the target variable is right-skewed, so we applied a log transformation to make it more normal.

## Model Training
We trained a RandomForestRegressor model on the scaled data using the train_test_split function from Scikit-learn. We evaluated the model using metrics like mean absolute error, mean squared error, and R-squared score.

Here are some of the key findings from the model training:

* We used a 70-30 train-test split to evaluate the model.
* We scaled the data using StandardScaler to make the features comparable.
* We used a RandomForestRegressor model with 100 trees and a maximum depth of 10.
* The model achieved a mean absolute error of 115,000 on the test set, a mean squared error of 2.2e+10, and an R-squared score of 0.85.

## Model Deployment
We serialized the trained model and the scaler using pickle and bz2file libraries. We then built a Docker image containing the serialized model, the scaler, and the necessary dependencies. We used AWS ECR to store the Docker image and AWS ECS to deploy the application.

Here are some of the key findings from the model deployment:

* We used a multi-stage Dockerfile to build a small and efficient Docker image.
* We used the AWS CLI to authenticate and push the Docker image to ECR.
* We used AWS ECS to deploy the application in a scalable and highly available environment.

## Running the Application
To run the application, follow these steps:

* Build the Docker image:
`docker build -t house-price-prediction`

* Run the Docker container:
`docker run -p 8080:8080 house-price-prediction`

* Deploy using Docker:
`./deploy.sh`

* Access the application eg., http://localhost:8080.

## Continuous Integration and Deployment
We used GitHub Actions to set up a continuous integration and deployment pipeline. The pipeline includes the following steps:

* Checkout the code from the repository.
* Install the required dependencies.
* Run the tests.
* Build the Docker image.
* Push the Docker image to AWS ECR.
* Deploy the application to AWS ECS.

### License
This project is licensed under the MIT License.

### Acknowledgments
Big thanks to Kaggle for providing the dataset and shoutout to Flask, scikit-learn, Docker, and GitHub Actions for being the unsung heroes of this project!

Enjoy the journey of predicting house prices, and let me know if there's anything
