# Slope-Detection-Taiwan
National Central University KSLab x 瑞模德科技有限公司

## Table of Contents
- [Introduction](#introduction)
- [Dataset Overview](#dataset-overview)
- [Dataset EDA](#dataset-eda)
- [Data Preprocessing](#data-preprocessing)
- [Pipeline](#pipeline)
- [Models Implemented](#models-implemented)
- [Evaluation](#evaluation)
- [Experimental Record](#experimental-record)
- [License](#license)
- [Contributors](#contributors)

## Introduction
The **Slope-Detection-Taiwan** project is aimed to build a machine learning model that predicts the movements of the slopes in different areas of Taiwan. 

## Dataset Overview
All details of the datas are in [README_Dataset.md](Data\README_Dataset.md)

## Dataset EDA

## Data Preprocessing  
1. **Step 1: Choosing Relevent Columns** 
    - Getting target columns and features columns.

2. **Step 2: Handling Outlier Values**
    - Remove values outside 3 standard deviations.

3. **Step 3: Scalling Data**
    - Applied `MinMaxScaler` to normalize the target columns.

## Pipeline

```mermaid
flowchart TD
    A[Dataset] --> B[Handeling data]
    B --> C[Data Preprocessing Completed]
    C --> D[Deep Learning Models]
    C --> E[Machine Learning Models]

    D --> F{Validation Dataset}
    E --> F
    
    F --> G[Test Dataset]
    G --> H[Final Evaluation]
```
## Models Implemented  

### Machine Learning Models

- **Decision Trees and Ensemble Models**:  
  - XGBoost  
  - Random Forest  

### Deep Learning Models
  - GRU

## Evaluation
We use `MAE` and `RMSE` score as our performance metric.
<div align="center">
  <img src="https://towardsdatascience.com/wp-content/uploads/2021/05/15OQunI-NR-S0gAZFIit1Rw.png" alt="Hisplot"/>
</div>

## Experimental Record
<!-- <div align="center">
  <img src="https://github.com/andrew76214/Kaggle-NLP_with_Disaster_Tweets/blob/main/img/ML1_evaluation.png" alt="Hisplot"/>
</div> -->

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributors

<div align="center">
  <a href="https://github.com/andrew76214/Slope-Detection-Taiwan/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=andrew76214/Slope-Detection-Taiwan" alt="Contributors"/>
  </a>
</div>