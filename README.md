![alt](https://www.uit.edu.vn/sites/vi/files/banner_uit.png)
# CS406.O11
- Tên môn học : Xử lý ảnh và ứng dụng
- Lớp : CS406.O11
- Giảng viên: Cáp Phạm Đình Thắng 
## Thực hiện bởi nhóm: **Forever20**
|STT|Thành viên|MSSV|
|:-:|:--|:-:|
|1|[Bui Huynh Kim Uyen](https://github.com/uyenbhku)|21521659|
|2|[Nguyen Nguyen Giap](https://github.com/Paignn)|21522025|
|3|[Nguyen Bui Thanh Mai](https://github.com/mainbt)|21522320|
|4|[Le Thi Nhu Y](https://github.com/lethinhuy20)|21522818|

## Mô tả đồ án 


## Repo tree
```bash
.
├── webthoitrang/ (tạm gọi là root của Django Project này)
│   ├── app/
│   ├──   ├── faiss_retrieval/
│   ├──   ├── static/
│   ├──   ├── utils/
│   ├──   ├── templates/
│   ├──   └── *.py files 
│   ├── webthoitrang/
│   ├── media/
│   ├──   ├── train/
│   ├──   ├── test/
│   ├──   └── uploaded-images/
│   ├── db.sqlite3
│   ├── manage.py
│   └── requirements.txt
└── README.md
 ```


## Cách cài đặt 
### Setup
- Cài đặt Python version `>= 3.10`
- Vào thư mục root của Django project 
    ```
    cd webthoitrang/
    ```
- Thiết lập môi trường ảo
    + Windows and MacOS
        ```
        python -m venv venv
        source venv/Scripts/activate
        ```
    + Others: Updating..........
- Install các packages cần thiết
    ```
    pip install -r requirements.txt
    ```
- Unzip `train_set.zip` và `test_set.zip` trong thư mục `media`
    ```
    cd media/
    unzip -q train_set.zip
    unzip -q test_set.zip
    ```
### Thực thi server 
- Chạy server (tại thư mục root của Django project này)
    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver 
    ```


