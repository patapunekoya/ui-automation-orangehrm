
# UI Automation Testing – OrangeHRM

## Giới thiệu
Dự án này thực hiện **UI Automation Testing** cho trang [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/)  
Sử dụng **Python + Selenium + Pytest** và xuất báo cáo HTML.

## Cấu trúc thư mục
```
ui-automation-orangehrm/
│── src/
│   ├── pages/              # Page Object Model (Login, Dashboard, PIM,...)
│   ├── tests/              # Test cases (login, logout, PIM)
│   ├── utils/              # Cấu hình, hàm tiện ích
│   └── __init__.py
│
│── reports/                # Thư mục chứa báo cáo HTML sau khi chạy test
│── requirements.txt        # Thư viện cần cài
│── README.md               # Tài liệu này
```

## Cài đặt
1. **Clone repo**  
```bash
git clone <repo-url>
cd ui-automation-orangehrm
```

2. **Tạo virtual env & cài thư viện**  
```bash
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

3. **Cấu hình thông tin**  
Kiểm tra file `src/utils/config.py`:
```python
BASE_URL = "https://opensource-demo.orangehrmlive.com/"
USERNAME = "Admin"
PASSWORD = "admin123"
HEADLESS = True   # chạy ẩn trình duyệt
```

## Chạy test
```bash
pytest -v --html=reports/index.html --self-contained-html
```

Sau khi chạy xong, mở báo cáo:
```
reports/index.html
```

## GitHub Actions CI
File CI: `.github/workflows/ci.yml`  
- Tự động cài Python, Chrome, Selenium.  
- Chạy test headless.  
- Upload báo cáo HTML lên GitHub Actions Artifact.

## Công nghệ sử dụng
- Python 3.11
- Selenium 4
- Pytest + Pytest-HTML
- GitHub Actions CI/CD
