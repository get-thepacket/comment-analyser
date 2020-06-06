from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics
import pickle
from trainer import extract_words

def loader():

    # Load All Reviews in train and test datasets
    f = open('train.pkl', 'rb')
    comment = pickle.load(f)
    f.close()

    # f = open('test.pkl', 'rb')
    # test = pickle.load(f)
    # f.close()

    # Generate counts from text using a vectorizer.  
    vectorizer = CountVectorizer()
    #Form a matrix with word counts
    train_features = vectorizer.fit_transform([r for r in comment[0]])
    #Same as above for test dataset
    test_features = vectorizer.transform([r for r in test[0]])

    # Fit a naive bayes model to the training data.
    # This will train the model using the word counts we computed, 
    #       and the existing classifications in the training set.
    nb = MultinomialNB()
    nb.fit(train_features, [int(r) for r in comment[1]])

    # Now we can use the model to predict classifications for our test features.
    # predictions = nb.predict(test_features)

# Compute the error.  
# print(metrics.classification_report(test[1], predictions))
# print("accuracy: {0}".format(metrics.accuracy_score(test[1], predictions)))

# while True:
#     sentences = []
#     sentence = input("Please enter a sentence to get sentiment evaluated. Enter \"exit\" to quit.")
#     if sentence == "exit":
#         print("exit program ...")
#         break
#     else:
#         sentences.append(sentence)
#         input_features = vectorizer.transform(extract_words(sentences))
#         prediction = nb.predict(input_features)
#         if prediction[0] == 1 :
#             print("----positive")
#         else:
#             print("----negative")

def naive_predict(sentence):
    sentences = []
    sentences.append(sentence)
    input_features = vectorizer.transform(extract_words(sentences))
    prediction = nb.predict(input_features)
    if prediction[0] == 1 :
        return "positive"
    else:
        return "negative"
