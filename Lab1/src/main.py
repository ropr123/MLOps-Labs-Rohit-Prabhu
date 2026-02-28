from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

if __name__ == '__main__':
    cancer = load_breast_cancer()
    X, y = cancer.data, cancer.target

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = LogisticRegression(max_iter=2000, solver="liblinear", random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, 'breast_cancer_model.pkl')

    print("The model training was successful")
