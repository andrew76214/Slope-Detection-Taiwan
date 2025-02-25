# Slope-Detection-Taiwan

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
Key characteristics of the dataset include:
- date_time
- E, H, N
- E_Move, H_Move, N_Move

## Dataset Overview
All details of the datas are in [README_Dataset.md](Data\README_Dataset.md)

We only use the first data from each city:
- Kaohsiung/g2.csv
- Nantou/cn01.csv
- Taipei/h23-g1.csv

## Dataset EDA
(with and without Handling Outlier Values)

Kaohsiung/g2 
![image](img/Kaohsiung_g2_original.png)
![image](img/Kaohsiung_g2_remove.png)

Nantou/cn01
![image](img/Nantou_cn01_original.png)
![image](img/Nantou_cn01_remove.png)

Taipei/h23-g1
![image](img/Taipei_h23-g1_original.png)
![image](img/Taipei_h23-g1_remove.png)

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
Taipei
![image](img/Evaluation_EMove_Taipei_h23.png)
![image](img/Evaluation_NMove_Taipei_h23.png)
![image](img/Evaluation_HMove_Taipei_h23.png)

Nantou
![image](img/Evaluation_EMove_Nantou_cn01.png)
![image](img/Evaluation_NMove_Nantou_cn01.png)
![image](img/Evaluation_HMove_Nantou_cn01.png)

Kaohsiung
![image](img/Evaluation_EMove_Kaohsiung_g2.png)
![image](img/Evaluation_NMove_Kaohsiung_g2.png)
![image](img/Evaluation_HMove_Kaohsiung_g2.png)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributors

<div align="center">
  <a href="https://github.com/andrew76214/Slope-Detection-Taiwan/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=andrew76214/Slope-Detection-Taiwan" alt="Contributors"/>
  </a>
</div>

Made with [contrib.rocks](https://contrib.rocks).