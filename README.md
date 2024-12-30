
# Health regression model.

# Project overview.
The goal of this project is to predict the insurance premium a customer should pay based on factors such as age, sex, pre-existing health conditions and location. This is a supervised regression problem where I aim to develop a model that can accurately estimate the premium.

# Data cleaning and EDA analysis.
The dataset was well-prepared with no missing values, inconsistencies or incorrect data types. Extreme values were not treated as anomalies because they reflect real-world scenarios, such as high BMI indicating obesity or age being a factor in higher premiums. Given that conditions like smoking, obesity and advanced age are factors influencing higher premiums, I decided to keep the extreme values in the analysis.

# Machine learning and modelling.
The dataset was split into features (X) and target (y). Feature selection was performed using a variance threshold, confirming no significant collinearity issues so all features were retained. I tested various regression algorithms, all of which performed well on both the training and testing datasets, indicating that overfitting was not an issue. To further reduce model variance, I utilized XGBoost and conducted grid search to fine-tune the hyperparameters. Finally, I implemented cross-validation across multiple folds to ensure the model’s ability to generalize to unseen data, and the results confirmed that the model performed well.

# Deployment.
The model was saved as a pickle file, enabling seamless deployment to a production environment for real-time predictions.