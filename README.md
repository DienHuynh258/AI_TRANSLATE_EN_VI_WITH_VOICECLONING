# AI Assistant - Django + Tailwind CSS

Một ứng dụng web AI Assistant được xây dựng bằng Django và Tailwind CSS với giao diện đẹp và hiện đại.

## Tính năng

### 🎨 Giao diện
- **Dark/Light Mode**: Chuyển đổi giữa chế độ sáng và tối
- **Responsive Design**: Tương thích với mọi thiết bị
- **Modern UI**: Giao diện đẹp với Tailwind CSS
- **Sidebar Navigation**: Menu điều hướng bên trái
- **Header với User Menu**: Menu người dùng ở góc trên bên phải

### 🔧 Chức năng chính
- **Home**: Trang chủ với tổng quan hệ thống
- **Speech to Text**: Chuyển đổi giọng nói thành văn bản
- **Transcript**: Tạo bản ghi chép từ file âm thanh/video
- **AI Chat**: Trò chuyện với AI (đang phát triển)

## Cài đặt và chạy

### Yêu cầu hệ thống
- Python 3.8+
- Node.js 14+
- npm hoặc yarn

### Bước 1: Clone repository
```bash
git clone <repository-url>
cd django_tailwind_project
```

### Bước 2: Tạo virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### Bước 3: Cài đặt dependencies
```bash
# Cài đặt Python dependencies
pip install -r requirements.txt

# Cài đặt Node.js dependencies
npm install
```

### Bước 4: Chạy migrations
```bash
python manage.py migrate
```

### Bước 5: Build CSS
```bash
npm run build
```

### Bước 6: Chạy server
```bash
python manage.py runserver
```

Truy cập http://localhost:8000 để xem ứng dụng.

## Cấu trúc dự án

```
django_tailwind_project/
├── core/                          # App chính
│   ├── templates/
│   │   ├── base.html             # Template cơ sở
│   │   └── core/
│   │       ├── index.html        # Trang chủ
│   │       ├── speech_to_text.html # Trang Speech to Text
│   │       └── transcript.html   # Trang Transcript
│   ├── views.py                  # Views
│   └── models.py                 # Models
├── myproject/                    # Cấu hình Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/                       # Static files
│   ├── css/
│   │   └── output.css           # CSS đã build
│   └── src/
│       └── input.css            # CSS source
├── tailwind.config.js           # Cấu hình Tailwind
├── package.json                 # Node.js dependencies
└── manage.py                    # Django management
```

## Tính năng chi tiết

### 🏠 Trang chủ (Home)
- Dashboard tổng quan
- Quick actions cho các chức năng chính
- AI Assistant Console với input/output
- Hiển thị hoạt động gần đây

### 🎤 Speech to Text
- Ghi âm trực tiếp
- Tải file âm thanh
- Cài đặt ngôn ngữ và chất lượng
- Hiển thị kết quả với độ chính xác

### 📝 Transcript
- Tải file âm thanh/video
- Tùy chọn xử lý (timestamps, speaker diarization)
- Progress bar khi xử lý
- Xuất file TXT/SRT
- Lịch sử transcript

### 🌙 Dark Mode
- Tự động lưu preference
- Chuyển đổi mượt mà
- Hỗ trợ system preference

## Phát triển

### Build CSS trong development
```bash
npm run build:watch
```

### Tạo superuser
```bash
python manage.py createsuperuser
```

### Chạy tests
```bash
python manage.py test
```

## Công nghệ sử dụng

- **Backend**: Django 4.2+
- **Frontend**: Tailwind CSS 3.0+
- **JavaScript**: Vanilla JS
- **Icons**: Heroicons
- **Build Tool**: PostCSS

## Đóng góp

1. Fork repository
2. Tạo feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Tạo Pull Request

## License

MIT License - xem file LICENSE để biết thêm chi tiết.

## Hỗ trợ

Nếu có vấn đề hoặc câu hỏi, vui lòng tạo issue trên GitHub.
