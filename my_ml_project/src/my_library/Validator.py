import sklearn.metrics as metrics
import pickle

class Validator:
    def __init__(self):
        self.model = None  # モデルを格納するインスタンス変数を初期化
        self.X = None  # 前処理済みの検証データを格納するインスタンス変数を初期化
        self.y = None  # 検証データのラベルを格納するインスタンス変数を初期化

    def load_data(self, file_path):
        with open(file_path, 'rb') as f:
            self.X, self.y = pickle.load(f)        
        return self.X, self.y

    def load_model(self, file_path):
        with open(file_path, 'rb') as f:
            self.model = pickle.load(f)

    def evaluate_model(self):
        y_pred = self.model.predict(self.X)
        accuracy = metrics.accuracy_score(self.y, y_pred)
        precision = metrics.precision_score(self.y, y_pred)
        recall = metrics.recall_score(self.y, y_pred)
        return accuracy, precision, recall