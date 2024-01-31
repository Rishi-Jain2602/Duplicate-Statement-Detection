# Duplicate-Statement-Detection
A Website made using streamlit which compare 2 statement and predict whether statements are duplicate or different.



https://github.com/Rishi-Jain2602/Duplicate-Statement-Detection/assets/118871883/861c9204-c0e4-474e-b9c8-a25bf4a42789



## Requirements
- Python 3.x
- Jupyter Notebook
- Python Libraries - Numpy, sklearn, tensorflow , pickle , streamlit, fuzzywuzzy, distance, bs4

***

## Installation
1. Clone the Repository
``` bash
git clone https://github.com/Rishi-Jain2602/Duplicate-Statement-Detection.git
```
2. Install the Project dependencies
```bash
pip install -r requirements.txt
```
3. Download train.csv.zip file which already been uploaded in this repository.

4. Download two pickle files i.e. modal.pkl & cv.pkl  

5. Download app.py & helper.py file from repository

In the terminal write 

```bash
streamlit run app.py
```

This will open the website where we have to give 2 statements and it will predict whether the statment is duplicate or not.

***

## Model Training

### Knowlege Required
- Natural Language Processing (NLP)
- Python Libraries -  Numpy, sklearn, tensorflow , pickle , streamlit, fuzzywuzzy, distance, bs4

### Tools
- Vs code

### Data Cleaning
- Text is converted to lowercase
- Replace certain special characters with their string equivalent and Decontracting words
- Removing HTML tags and URLs
- Removing Stopwords


### Text Vectorization
- It map words or phrases from vocabulary to a corresponding vector of real numbers which used to find word predictions, word similarities/semantics. 
- The process of converting words into numbers are called Vectorization.

### Modelling
*Random Forest Classification algorithm, Machine Learning algorithm was used to train the model*
- It is basically belongs to Family of Decision tree
- A decision tree is a flowchart-like structure where each internal node represents a decision based on the value of a particular feature, each branch represents the outcome of that decision, and each leaf node represents the final prediction or decision.
#### Advantage
- It can handle Overfitting and non-linearity.
- Can be applied to various type of data including Numerical and categorical data
#### Limitation
- Higher the number of trees lead to better performance but upto a certain extent.
***


### Result

![result](https://github.com/Rishi-Jain2602/Duplicate-Statement-Detection/assets/118871883/0544b316-ebcf-44c7-aa2a-844c530e5b39)




***

## Note
1. Make sure you have Python 3.x installed
2. It is recommended to use a virtual environment to avoid conflict with other projects.
3. For deep learning, a laptop with a powerful GPU, a high-performance CPU, at least 8GB of RAM, a fast SSD, and an efficient cooling system is recommended.
4. If you encounter any issue during installation or usage please contact rishijainai262003@gmail.com or rj1016743@gmail.com
 
