# UI Automation – OrangeHRM (Selenium + Python)

- Page Object Model (POM)
- Test flow: Login, Logout, PIM search
- Pytest + pytest-html report
- Headless by default, CI với GitHub Actions

## Cài đặt
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
cp .env.example .env   # chỉnh BASE_URL/USERNAME/PASSWORD nếu cần
