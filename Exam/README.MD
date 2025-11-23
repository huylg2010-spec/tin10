# Hướng dẫn thiết lập môi trường Python (Windows / PowerShell)

- Kiểm tra Python đã cài:
	- `py --version` hoặc `python --version`
	- Nếu không có, tải và cài từ https://www.python.org/downloads/ — khi cài, tích `Add Python to PATH`.

- Tạo và kích hoạt virtual environment:
 1. Chuyển vào thư mục dự án: `Set-Location D:\Tin10\Exam`
 2. Tạo venv: `py -3 -m venv .venv`
 3. Kích hoạt (PowerShell): `.\.venv\Scripts\Activate.ps1`

- Cập nhật pip và cài dependency:
	- `python -m pip install --upgrade pip`
	- Nếu dự án có `requirements.txt`: `pip install -r requirements.txt`

- Chạy chương trình:
	- Thông thường: `python exam.py`
	- Nếu cần redirect input: `python exam.py < input.inp`

Khắc phục sự cố phổ biến:
- Lỗi không nhận `py`/`python`: kiểm tra PATH hoặc cài lại Python kèm `Add to PATH`.
- Lỗi khi kích hoạt `Activate.ps1`: PowerShell có thể chặn script, chạy `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` rồi thử lại.
- Muốn dùng phiên bản Python cụ thể: `py -3.10 -m venv .venv` (thay `3.10` bằng phiên bản mong muốn).
- Một số package cần công cụ build (Visual C++ Build Tools) — xem thông báo lỗi pip để biết chi tiết.

Gợi ý thêm:
- Để lưu cài đặt phụ thuộc, tạo file `requirements.txt` bằng `pip freeze > requirements.txt` khi venv đã cài xong.
- Để tắt venv: chạy `deactivate`.

Hướng dẫn cho VS Code (debug)

Nếu bạn dùng Visual Studio Code, làm theo các bước sau để dễ debug `exam.py`:

1) Cài extension Python: mở VS Code → Extensions → tìm `Python` (Microsoft) và cài.

2) Chọn Python interpreter của dự án:
	 - Mở Command Palette (`Ctrl+Shift+P`) → `Python: Select Interpreter` → chọn interpreter trong `.venv` (ví dụ: `.venv\Scripts\python.exe`).

3) Tạo cấu hình debug (file `launch.json`):
	 - Mở tab Run and Debug (`Ctrl+Shift+D`) → Create a launch.json → chọn `Python File`.
	 - Hoặc tạo thủ công file `.vscode\launch.json` với nội dung sau:

```json
{
	"version": "0.2.0",
	"configurations": [
		{
			"name": "Python: Debug exam.py",
			"type": "python",
			"request": "launch",
			"program": "${workspaceFolder}/exam.py",
			"console": "integratedTerminal",
			"cwd": "${workspaceFolder}"
		}
	]
}
```

4) Chạy debug:
	 - Đặt breakpoint trong `exam.py`, chọn cấu hình `Python: Debug exam.py` và bấm Start Debugging (F5).
	 - Cấu hình trên dùng `integratedTerminal`, nên nếu chương trình cần input từ file (`input.inp`) bạn có hai lựa chọn:
		 - Trước khi bấm F5, mở Integrated Terminal và chạy `python exam.py < input.inp` trực tiếp (không debug nhưng test nhanh stdin).
		 - Hoặc debug như bình thường (F5) và khi chương trình dừng ở điểm chờ input, dán/copy nội dung `input.inp` vào terminal.

Ghi chú:
- VS Code không hỗ trợ redirect STDIN từ file trực tiếp thông qua `args` trong `launch.json` (dấu `<` là tính năng của shell). Nếu bạn muốn debug với nội dung file tự động, sửa `exam.py` để khi có `sys.argv[1]` thì đọc từ file đó.
- Thêm `"env": {"PYTHONUNBUFFERED": "1"}` trong cấu hình nếu cần output realtime.

---
File này được viết để giúp chạy `exam.py` nhanh trên Windows với PowerShell.

