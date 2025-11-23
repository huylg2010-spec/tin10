# ============================================
# KHUNG CODE PYTHON TỔNG QUÁT CHO BÀI THI HSG TIN
# ============================================

import sys

# --------------------------------------------
# Cấu hình tên file (thay đổi theo từng bài)
# --------------------------------------------
INPUT_FILE  = "INPUT.INP"   # đổi lại theo đề: SHIPPER.INP, TRAI.INP, ...
OUTPUT_FILE = "OUTPUT.OUT"  # đổi lại theo đề: SHIPPER.OUT, TRAI.OUT, ...

# --------------------------------------------
# Hàm đọc toàn bộ dữ liệu từ file
# Tự động hỗ trợ 3 dạng:
# - Dạng 1: dữ liệu cách nhau bởi khoảng trắng
# - Dạng 2: dữ liệu nhiều dòng riêng biệt
# - Dạng 3: kết hợp cả hai
# --------------------------------------------
def read_all():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        text = f.read()
    return text

# Trả về list token (phù hợp dạng số, chữ)
def read_tokens():
    return read_all().split()

# Trả về list dòng (phù hợp dạng mỗi dòng 1 xâu)
def read_lines():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]


# --------------------------------------------
# Hàm ghi output dạng:
# - Một dòng
# - Nhiều dòng (list)
# --------------------------------------------
def write_output(result):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        if isinstance(result, list):
            f.write("\n".join(str(x) for x in result))
        else:
            f.write(str(result))


# --------------------------------------------
# Hàm solve() – nơi bạn xử lý theo yêu cầu đề bài
# --------------------------------------------
def solve():
    # Tùy bài mà chọn style đọc dữ liệu:
    #
    # tokens = read_tokens()
    # lines  = read_lines()
    # raw    = read_all()
    #
    # Ví dụ:
    # n = int(tokens[0])
    # arr = list(map(int, tokens[1:]))

    # TODO: GHI LOGIC BÀI TOÁN Ở ĐÂY
    result = None
    # result có thể là:
    # - số nguyên
    # - chuỗi
    # - list để in nhiều dòng

    write_output(result)


# --------------------------------------------
# Main
# --------------------------------------------
if __name__ == "__main__":
    solve()