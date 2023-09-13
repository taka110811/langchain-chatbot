import csv

# CSVファイルの名前
csv_file = "demo_data.csv"

# サンプルデータを持つリスト
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 28, "Chicago"],
    ["David", 22, "San Francisco"],
]

# CSVファイルを書き込みモードで開く
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # データをCSVファイルに書き込む
    writer.writerows(data)

print(f"{csv_file} が作成されました。")
