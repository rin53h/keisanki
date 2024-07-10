import sklearn.svm as SVM
import sklearn.ensemble as Ensemble
import pickle
import numpy

class Trainer:
    def __init__(self):
        self.model = None  # モデルを格納するインスタンス変数を初期化

    def load_data(self, file_path):
        with open(file_path, 'rb') as f:
            X, y = pickle.load(f)        
        return X, y
        
    def dump_model(self, file_path):
        with open(file_path, 'wb') as f:
            pickle.dump(self.model, f)

    def train_SVM(self, hyperparameter, X, y):
        self.model = SVM.SVC(C=hyperparameter)
        self.model.fit(X,y)

    def train_RF(self, hyperparameter, X, y):
        self.model = Ensemble.RandomForestClassifier(max_depth=hyperparameter)
        self.model.fit(X,y)