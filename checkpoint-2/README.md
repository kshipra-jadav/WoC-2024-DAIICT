# Checkpoint 2

For this particular checkpoint, I have trained **Logistic Regression**, **Naive Bayes**, **Support Vector Machine** and **Random Forest Classifier** models on the processed dataset.

The train data just included the word embeddings that were created as a part of checkpoint-1 and the labels which were taken directly from the dataset itself.

Just to aid the models, I have normalized the embeddings using the `MinMaxScaler` from `scikit-learn` library and I have also performed label encoding by using the `LabelBinarizer` class from `scikit-learn` too.

Finally, I trained the models on the training data and evaluated them using the testing data. I used a train-test-split size of **80-20**. That means 80% of the data went to the training and 20% of the data went for testing.

Below are the compiled results of all the models - 

| Model Name              | Accuracy | Precision | Recall |
|-------------------------|----------|-----------|--------|
| Logistic Regression     | 0.58     | 0.58      | 0.58   |
| Naive Bayes             | 0.56     | 0.56      | 0.56   |
| Support Vector Machine  | 0.62     | 0.62      | 0.62   |
| Random Forest Classifier| 0.57     | 0.57      | 0.57   |

> Important to note here that the precision and recall values are the average values of precision and recall for the respective classes.

Looking at the results above, we can see that **Support Vector Machine** model is better at classifying the text embeddings as compared to all the other models.

I have also exported each model in a pickel format, and you will be able to find it in this same directly with the naming convention - `model-name.joblib`
