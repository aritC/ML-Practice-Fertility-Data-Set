# ML-Practice-On-Fertility-Data-Set
Practicing Various Models on Fertility Data Set

## Abstract ##

100 volunteers provide a semen sample analyzed according to the WHO 2010 criteria. Sperm concentration are related to socio-demographic data, environmental factors, health status, and life habits

-**Data Set Characteristics**: Multivariate
-**Attribute Characteristics**: Real
-**Area**: Life
-**Number Of Attributes**:10
-**Number Of Records**:100

To get the data set for yourself click [here](https://archive.ics.uci.edu/ml/machine-learning-databases/00244/)<br/>To know more about the data click [here](https://archive.ics.uci.edu/ml/datasets/Fertility)

## Data Set Attribute Information ##

- **Season** in which the analysis was performed. 1) winter, 2) spring, 3) Summer, 4) fall. (-1, -0.33, 0.33, 1)
- **Age** at the time of analysis. 18-36 (0, 1)
- **Childish diseases** (ie , chicken pox, measles, mumps, polio) 1) yes, 2) no. (0, 1)
- **Accident or serious trauma** 1) yes, 2) no. (0, 1)
- **Surgical intervention** 1) yes, 2) no. (0, 1)
- **High fevers in the last year** 1) less than three months ago, 2) more than three months ago, 3) no. (-1, 0, 1)
- **Frequency of alcohol consumption** 1) several times a day, 2) every day, 3) several times a week, 4) once a week, 5) hardly ever       or never (0, 1)
- **Smoking habit** 1) never, 2) occasional 3) daily. (-1, 0, 1)
- **Number of hours spent sitting per day** ene-16 (0, 1)
- **Output**: Diagnosis normal (N), altered (O)

## Methodology ##

Used 3 models for now :
- KNN
- LogisticRegression
- SVC

**Procedure**

1. Data was loded into python by using [**Pandas**](https://pandas.pydata.org) library.
2. Data was split into training and testing data using the [**train_test_split**](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) module in the [**model__selection**](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.model_selection) library of [**sklearn**](http://scikit-learn.org)
3. For **KNN** a loop was used to check different ***n_neighbours*** values in between 1 to 40. The **mean error_rate** was plotted and can be seen that for any value greater than 1 the model has least error so taking the least value  of ***n_neigbours i.e. 2***.
4. For **SVC** again from [**model__selection**](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.model_selection) library of [**sklearn**](http://scikit-learn.org) module [**GridSearchCV**](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) is used so as to find the best combination for the SVC parameters ***C*** and ***gamma***.
<br>The best combination of parameters was found to be
>'C': 0.1 'gamma': 0.1<br>
5. Using this estimator data was fit into the SVC model and trained and tested.
6. Lastly for **Logistic Regression** simply the data was fit into the model and values were tested.
7. **Evaluation**  of the models was done by [**sklearn's**](http://scikit-learn.org) [**metrics**](http://scikit-learn.org/stable/modules/classes.html)library. Modules [**classification_report**](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html) and [**confusion_matrix**](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html) were used to check the confidence/accuracy of the model.
9. Accuracy Scores of all the models can be seen as the same as 91%.

## Final Remarks ##
What I think went wrong in this is that the data set doesn't have enough Class 1 data so in the test case as you can see in the confusion matrix <br>
| n=33 | Pred Class 0 | Pred Class 1 |
|---|---|---|
| Actual Class 0| 30 | 3|
|---|---|---|
|Actual Class 1 | 0 | 0|
<br>
So these models might not be that good in predicting True Class 1. Also the data set is very small
  
  
