from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import joblib
import os

def train_models(train,test,features):
    
    X_train=train[features]
    Y_train=train["Direction"]

    X_test=test[features]
    Y_test=test["Direction"]

    scaler=StandardScaler()
    X_train_scaled=scaler.fit_transform(X_train)
    X_test_scaled=scaler.transform(X_test)

    log_model=LogisticRegression()
    log_model.fit(X_train_scaled,Y_train)
    log_pred=log_model.predict(X_test_scaled)

    rf_model=RandomForestClassifier(
          n_estimators=300,
          max_depth=6,
          min_samples_leaf=20,
          random_state=42,
          n_jobs=-1
    )
    rf_model.fit(X_train,Y_train)
    rf_pred=rf_model.predict(X_test)

    print("\nLogistic Accuracy: ",accuracy_score(Y_test,log_pred))
    print("Random Forest Accuracy: ",accuracy_score(Y_test,rf_pred))

    os.makedirs("models",exist_ok=True)
    joblib.dump(log_model,"models/logistic.pkl")
    joblib.dump(rf_model,"models/rf.pkl")
    joblib.dump(scaler,"models/scaler.pkl")

    return log_model, rf_model, scaler