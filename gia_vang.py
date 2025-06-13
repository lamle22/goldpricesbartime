import requests
import re
import csv

url = "https://sinhdien.com.vn/gia-vang-ajax-34255318"
res = requests.get(url)
html = res.text

loai_vang = [
    "Nhẫn tròn 999",
    "Nhẫn vỉ 999,9",
    "Vàng 18K",
    "Vàng 610",
    "Vàng 14K",
    "Vàng 10K",
    "Bạc",
    "Thần tài"
]

header = []
data = []

for ten in loai_vang:
    ten_escaped = re.escape(ten)
    match = re.search(rf'<tr><td>{ten_escaped}</td><td>([\d,]+)</td><td>([\d,]+)</td></tr>', html)
    if match:
        mua = match.group(1)
        ban = match.group(2)
    else:
        mua = ban = "Không tìm thấy"
    header.extend([f"{ten} - Mua vào", f"{ten} - Bán ra"])
    data.extend([mua, ban])

match_time = re.search(r'Cập nhật lúc: ([\d: ]+\d{2}/\d{2}/\d{4})', html)
thoigian = match_time.group(1) if match_time else "Không rõ"
header.insert(0, "Thời gian cập nhật")
data.insert(0, thoigian)

with open("gia_vang_mot_hang.csv", mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
