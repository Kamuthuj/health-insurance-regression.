
# Health regression model.

# Project overview.
The goal of this project is to predict the insurance premium a customer should pay based on factors such as age, sex, pre-existing health conditions and location. This is a supervised regression problem where I aim to develop a model that can accurately estimate the premium.

[MyhealthPredictionApp](https://health-insurance-regression-dectbgpdzz3dxxjwguaz5f.streamlit.app/)

# Data cleaning and EDA analysis.
The dataset was well-prepared with no missing values, inconsistencies or incorrect data types. Extreme values were not treated as anomalies because they reflect real-world scenarios, such as high BMI indicating obesity or age being a factor in higher premiums. Given that conditions like smoking, obesity and advanced age are factors influencing higher premiums, I decided to keep the extreme values in the analysis.

# Machine learning and modelling.
The dataset was first partitioned into features (X) and target variable (y), forming the foundation for supervised learning. Multiple regression models were explored, including Simple Linear Regression, Decision Tree Regressor, ensemble methods such as Bagging Regressor, and Random Forest Regressor. These models demonstrated strong performance and generalization capabilities, as validated through cross-validation techniques.
To further capture complex, non-linear patterns in the data, I also implemented a Deep Neural Network with fully connected (dense) layers, aiming to uncover deeper insights from the feature space.

Among all models evaluated, the Random Forest Regressor emerged as the most balanced candidate for deployment. It consistently achieved a strong trade-off between predictive accuracy (as measured by R²) and error metrics (such as MAE). Its performance remained stable across both training and testing datasets, indicating solid generalization.

While the Bagging Regressor also showed promising results, Random Forest provided slightly better interpretability and robustness, especially when dealing with diverse or noisy datasets.

# Deployment.
The random forest regressor model was saved as a pickle file, enabling seamless deployment. I deployed it using streamlit to make prdictions.

