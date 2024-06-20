# ここにコードを挿入してください。

# プロジェクトのルートパスを取得
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# プロジェクトのルートパスをシステムパスに追加
sys.path.append(project_root_path)

# ライブラリをインポート
import my_library.load_input_data as input_loader
import my_library.load_dictionary as dictionary_loader
import my_library.count_statistics as counter
import my_library.predict_polarity as predictor
import my_library.manage_output as output_manager

# 入力データをロード
sentence_arrays = input_loader.load("../data/processed_data_v1.txt")

# 辞書をロード
d1 = dictionary_loader.load("../extlib/dictionary1.txt")
d2 = dictionary_loader.load("../extlib/dictionary2.txt")

# 結果を格納するための空のリストを作成
result = []

# 入力データの各文に対して統計を計算し、結果を予測
for i in range(len(sentence_arrays)):
    sentence = sentence_arrays[i]
    count_statistics = counter.count(d1, d2, sentence)
    result.append(predictor.predict(count_statistics))

# 結果を出力
output_manager.output(sentence_arrays, result)
