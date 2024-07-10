import os
import sys
project_root_path = os.path.dirname(os.path.dirname( os.path.abspath(__file__) )) 
sys.path.append(project_root_path)

from my_library.Trainer import Trainer

logs_path = "_logs/pre1"

# preprocessed_train_data_path = input("Enter the path for the preprocessed data:") 
# model_dump_path_base = input("Enter the path for the directory to save the models:")
preprocessed_train_data_path = os.path.join(logs_path, "data/train_preprocessed.pkl")
model_dump_path_base = os.path.join(logs_path, "models")

trainer = Trainer()
X, y = trainer.load_data(preprocessed_train_data_path)

# train with SVM
hyperparameters = [0.1,1,10,100,1000]
for h in hyperparameters:
    print(f">>> doing: train SVM with hyperparameter = {h}")
    model_dump_path = os.path.join(model_dump_path_base , "SVM_"+str(h)+".pkl") 
    trainer.train_SVM(h, X, y)
    trainer.dump_model(model_dump_path)

# train with RF
hyperparameters = [1,10,100,1000]
for h in hyperparameters:
    print(f">>> doing: train RF with hyperparameter = {h}")
    model_dump_path = os.path.join(model_dump_path_base , "RF_"+str(h)+".pkl") 
    trainer.train_RF(h, X, y)
    trainer.dump_model(model_dump_path)