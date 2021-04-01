# model_that_checks_the_authenticity_of_given_news

![alt text](https://assets.teenvogue.com/photos/5dae2cb156a2b0000860086a/16:9/w_2560%2Cc_limit/Pol_Fake-News_10-21_PROMO.jpg)

This web-application is based on scikit-learn's Random Forest Classifier.
For more on this click the link below.

[Classifier model based on sklearn RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)


## Project Overview

With the widespread use of social media, so did the spread of fake news.
According to researchers from the Massachusetts Institute of Technology, fake news is more likely to be spread than their true counterpart.
We believed that a pre-trained model that can distinguish real news from fake news can assist people verify what is real and what is fake.

*   [BBC-Fake news 'travels faster', study finds](https://www.bbc.com/news/technology-43344256)


## Packages and Frameworks that were used

*   nltk (3.5)
*   scikit-learn (0.24.1)
*   Django (3.1.7)
*   Python (3.8.5)


## Deployment

We used Heroku to deploy the project.
While deploying the project, we ran into an error where the application failed to download the nltk data.
To resolve this error, there needs to be an 'nltk.txt' in the base directory of the application specifying the nltk data that the user wishes to download.
The documentation to this issue can be found in the link below

*   [Using NLTK Data with Heroku Python](https://devcenter.heroku.com/articles/python-nltk)

*   [Web-app deployed on Heroku](https://check-if-news-is-fake.herokuapp.com/)


## Limitations

The model can only distinguish English songs as it was only trained on English data.


## Data From

*   [Fake and real news dataset](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)


## Reference

*   [Fake News Detection (99.5% acc)](https://www.kaggle.com/sachinrajput17/fake-news-detection-99-5-acc)


## Authors

*   Adam Lee, ubrain0624@gmail.com, [github](https://github.com/yoonhoelee)
*   Taeheon Kim, kimth3403@gmail.com, [github](https://github.com/Kimtaeheon95)
