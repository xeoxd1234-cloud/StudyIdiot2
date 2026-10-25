"""Naive Bayes spam classifier example.

Install dependencies with: python -m pip install scikit-learn
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

EMAILS = [
    "Win money now",
    "Free prize claim",
    "Meeting at 10 am",
    "Project update",
    "Claim your reward",
    "Lunch tomorrow",
]
LABELS = [1, 1, 0, 0, 1, 0]  # 1 = spam, 0 = not spam


def main():
    x_train, x_test, y_train, y_test = train_test_split(
        EMAILS, LABELS, test_size=0.33, random_state=1
    )
    vectorizer = CountVectorizer()
    x_train_vectorized = vectorizer.fit_transform(x_train)
    x_test_vectorized = vectorizer.transform(x_test)

    model = MultinomialNB().fit(x_train_vectorized, y_train)
    predictions = model.predict(x_test_vectorized)
    print("Accuracy:", accuracy_score(y_test, predictions))
    print("Prediction:", model.predict(vectorizer.transform(["free money offer"])))


if __name__ == "__main__":
    main()
