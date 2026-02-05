from flask import Flask

app = Flask(__name__)
.
.
.
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)

- debug mặc định là False. Khi debug là False, khi thay đổi chương trình đang chạy thì cần khởi động lại chương trình để cập nhật 
các thay đổi. Nếu để debug = True thì khi sau khi ấn lưu, web sẽ cập nhật lại ngay mà không cần chạy lại

- host là địa chỉ IP để truy cập web. Mặc định khi chạy sẽ lấy địa chỉ IP, khi này chỉ laptop này mở được web
- nếu dùng IP mạng đang kết nối thì các thiết bị đang cùng chung một wifi sẽ có thể truy cập web
  window + R -> ipconfig -> Tìm địa chỉ IP
- Nếu host = 0.0.0.0 thì có thể truy cập bằng cả hai cách trên

- port là cổng để kết nối. Mỗi web khi chạy sẽ chiếm dụng một port. Trùng sẽ báo lỗi . Mặc định port của Flask là 5000, ta tạo web thứ hai phải cấu hình
thủ công thành một port nào đó khác 5000 vì web trước đó đã chiếm cổng này

@app.route("/")
def home1():
    return "Hello World!"
- Đây là phần xây dựng web, @app.route() là phần đường dẫn web. nhiều đường dẫn web có thể cùng dẫn đến một hàm  
