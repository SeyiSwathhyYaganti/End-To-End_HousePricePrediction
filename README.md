# End-To-End_HousePricePrediction

This repository provides an end-to-end solution for predicting house prices using machine learning. The project includes comprehensive steps from data collection, exploratory data analysis (EDA), feature engineering, model building, evaluation, and deployment, integrated with **ZenML** and **MLflow** for experiment tracking and model deployment.

## 🚀 Project Overview

### Features
- **Comprehensive EDA**: Thorough exploratory data analysis to craft compelling data narratives.
- **Feature Engineering**: Features were engineered with deep understanding, using domain knowledge and data insights.
- **Model Building**: A single model was implemented, validated, and tested rigorously.
- **Scalable and Defensive Code**: Code is written using design patterns and best practices for scalability and readability.
- **MLOps Integration**: Integrated ZenML for experiment tracking and model deployment using MLflow.

## 📂 Project Structure

Here’s a breakdown of the project structure:

├── Data │ └── archive.zip ├── Data_Analysis │ ├── Analyse_src │ └── EDA.ipynb ├── Explanatory_codes │ ├── Factory_design_pattern.py │ ├── Strategy_design_pattern.py │ └── Template_design_pattern.py ├── Installing and Setting Project.docx ├── README.md ├── extracted data │ └── AmesHousing.csv ├── house_price_prediction.egg-info ├── mlruns ├── pipelines │ ├── deployment_pipeline.py │ └── training_pipeline.py ├── requirements.txt ├── run_deployment.py ├── run_pipeline.py ├── sample_predict.py ├── setup.py ├── src │ ├── feature_engineering.py │ ├── model_building.py │ └── model_evaluator.py └── steps ├── data_evaluator.py ├── data_ingestion_step.py └── model_loader.py


## 🛠️ ZenML Setup for Experiment Tracking & Model Deployment

To execute this project, you will need to set up **ZenML** with **MLflow** integration for experiment tracking and model deployment. Follow the steps below to set up ZenML and the necessary components.

### 1. **Install ZenML**
   To get started, first install **ZenML**:
   ```bash
   pip install zenml

2. Create a Virtual Environment
You can create a virtual environment for this project by following the instructions in this video guide.
Once you've created and activated your virtual environment, move to the next step.
3. Install Dependencies
After setting up the virtual environment, install the required dependencies:
pip install -r requirements.txt
