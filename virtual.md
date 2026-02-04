python -m venv venv  //Lệnh này tạo ra thư mục venv chứa bộ "đồ nghề" sạch hoàn toàn

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser  //Cấp quyền (nếu bị lỗi SecurityError

.\venv\Scripts\activate  //Dấu hiệu thành công: Xuất hiện tiền tố (venv) ở đầu dòng lệnh.

pip install Flask

pip freeze > requirements.txt

 
