#Classification
#importing libraries and retrieving our dataset
import pandas as pd  
import numpy as np  
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus
from sklearn import svm
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

def dt():
    #import matplotlib.pyplot as plt
    #get_ipython().run_line_magic('matplotlib', 'inline')
    dataset=pd.read_csv("mixdataset.csv")
    df=pd.DataFrame(dataset)


    dataset.shape

    print("dataframe:    ",df)
    # In[3]:


    dataset.head()


    # In[4]:



    #To divide data into attributes and labels
    # X variable contains all the columns from the dataset, except the "Class" column, which is the label.
    #The y variable contains the values from the "Class" column.
    #The X variable is our attribute set and y variable contains corresponding labels.
    X = dataset.drop('Class', axis=1)
    y = dataset['Class']


    # In[5]:


    #The final preprocessing step is to divide our data into training and test sets.
    #The model_selection library of Scikit-Learn contains train_test_split method
    #which we'll use to randomly split the data into training and testing sets.
    #In the code above, the test_size parameter specifies the ratio of the test set,
    #which we use to split up 20% of the data in to the test set and 80% for training.

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)


    # In[6]:


    #the final step is to train the decision tree algorithm on this data and make predictions.
    #Since we are going to perform a classification task here, we will use the DecisionTreeClassifier class for this example
    #the fit method of this class is called to train the algorithm on the training data

    classifier = DecisionTreeClassifier()
    classifier.fit(X_train, y_train)


    # In[7]:


    #let's make predictions on the test data
    y_pred = classifier.predict(X_test)
    X_test


    # In[8]:


    y_pred


    # In[9]:



    dtree=DecisionTreeClassifier()
    res=dtree.fit(X_train,y_train)


    # In[10]:



    dot_data = StringIO()
    export_graphviz(res, out_file=dot_data,
                    filled=True, rounded=True,
                    special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    #print(graph)
    Image(graph.create_png())


    # In[11]:


    inputt=pd.read_csv("newdata.csv")
    X1 =inputt.iloc[:,:17]
    X1
    y1=inputt.iloc[[634], [17]]
    y1
    pop1=pd.DataFrame(inputt)
    #print(inputt)
    #pop1.shape


    # In[12]:


    print(X1)


    # In[13]:


    print(y1)


    # In[14]:


    #a=pop1.iloc[-1:]
    #print(a)
    #X1.shape
    y1.shape


    # In[15]:


    y1=pop1.Class

    dtree=DecisionTreeClassifier()
    res1=dtree.fit(pop1,y1)
    #res2=dtree.predict()
    #print(res2)
    #predictions=res1.predict(a)
    #print(predictions)


    # In[16]:


    y1.shape


    # In[17]:


    print(res1)


    # In[18]:


    #res2=dtree.predict(pop1)
    #print(res2)
    #res3=dtree.predict(X)
    #rint(res3) #res3)


    # In[19]:


    dot_data = StringIO()
    export_graphviz(res1, out_file=dot_data,
                    filled=True, rounded=True,
                    special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    Image(graph.create_png())


    # In[20]:


    print(y1)


    # In[21]:



    model=svm.SVC()
    model.fit(X_train,y_train)
    y_pred= model.predict(X_test)

    print(metrics.accuracy_score(y_test,y_pred))
    print(confusion_matrix(y_test,y_pred))
    print(classification_report(y_test,y_pred))
    yp=model.predict(X1)
    print(yp)

    # In[22]:


    leng=len(yp)
    print("Length:",leng)
    print("return value:",yp[leng-1])
    # In[23]:


    #yp[leng]


    # In[24]:


    #print(yp[leng])

    return yp[leng-1]

#dt()
