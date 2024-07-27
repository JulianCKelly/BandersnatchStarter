from sklearn.ensemble import RandomForestClassifier


class Machine:

    def __init__(self, df):
        self.name = "Random Forest Classifier"
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42, bootstrap=False)
        self.model.fit(features, target)

    def __call__(self, pred_basis):
        prediction = (self.model.predict(pred_basis))[0]
        probability = (self.model.predict_proba(pred_basis))[0]
        return prediction, max(probability)

    def save(self, filepath):
        pass

    @staticmethod
    def open(filepath):
        pass

    def info(self):
        return self.model


