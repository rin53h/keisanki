import os
import sys
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)   

import pickle 

file_path = os.path.join(project_root_path, "testeiei.pkl")
a =[1,2,3,4]
with open(file_path, "wb") as f:
    pickle.dump(a, f)