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
├── Data
│ └── archive.zip
├── Data_Analysis
│ ├── Analyse_src
│ └── EDA.ipynb
├── Explanatory_codes
│ ├── Factory_design_pattern.py
│ ├── Strategy_design_pattern.py
│ └── Template_design_pattern.py
├── Installing and Setting Project.docx
├── README.md
├── extracted data
│ └── AmesHousing.csv
├── house_price_prediction.egg-info
├── mlruns
├── pipelines
│ ├── deployment_pipeline.py
│ └── training_pipeline.py
├── requirements.txt
├── run_deployment.py
├── run_pipeline.py
├── sample_predict.py
├── setup.py
├── src
│ ├── feature_engineering.py
│ ├── model_building.py
│ └── model_evaluator.py
└── steps
├── data_evaluator.py
├── data_ingestion_step.py
└── model_loader.py


## 🛠️ ZenML Setup for Experiment Tracking & Model Deployment

To execute this project, you will need to set up **ZenML** with **MLflow** integration for experiment tracking and model deployment. Follow the steps below to set up ZenML and the necessary components.

### 1. **Install ZenML**
   To get started, first install **ZenML**:
   pip install zenml 

## 2. Create a Virtual Environment

You can create a virtual environment for this project by following the instructions in this video guide. Once you've created and activated your virtual environment, move to the next step.

### 3. Install Dependencies

After setting up the virtual environment, install the required dependencies:
pip install -r requirements.txt

### 4. Install ZenML Integration for MLflow
If you are running the run_deployment.py script, you'll need to install ZenML's MLflow integration:

zenml integration install mlflow -y

### 5. Configure ZenML Stack with MLflow
For the project to run, you need to set up a ZenML stack with MLflow as both the experiment tracker and model deployer. Run the following commands to configure your stack:
#### Register the MLflow experiment tracker:
zenml experiment-tracker register mlflow_tracker --flavor=mlflow
## Register the MLflow model deployer:
zenml model-deployer register mlflow --flavor=mlflow
## Register the ZenML stack with the experiment tracker and model deployer:
zenml stack register local-mlflow-stack -a default -o default -d mlflow -e mlflow_tracker --set

### 6. Running the Project
Once the ZenML stack is configured, you can run the project using the training pipeline and deployment pipeline as described earlier. This setup allows ZenML to track experiments and deploy the model via MLflow.
⚙️ Installation & Requirements

Clone this repository:
git clone https://github.com/SeyiSwathhyYaganti/End-To-End_HousePricePrediction.git
cd End-To-End_HousePricePrediction
Install dependencies:
pip install -r requirements.txt
Set up ZenML and MLflow as described above.
🧑‍💻 Running the Code

To run the training pipeline:
python run_pipeline.py
To run the deployment pipeline:
python run_deployment.py
📊 Visualizations and Results

The project contains detailed visualizations and performance metrics as part of the EDA and model evaluation processes. Explore the EDA.ipynb notebook for data analysis insights and the model evaluation results in the pipeline scripts.
🔧 Technologies Used

ZenML for MLOps and experiment tracking
MLflow for model deployment and tracking
Scikit-learn for machine learning
Pandas for data manipulation
Matplotlib & Seaborn for data visualization
Jupyter Notebooks for exploratory data analysis
📄 Documentation

For detailed instructions on setting up the project, check the Installing and Setting Project.docx document.
