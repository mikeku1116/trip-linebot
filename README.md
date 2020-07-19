# trip-linebot #

## 專案介紹 ##

本專案利用Django框架來建置LINE Bot旅遊景點機器人，並且連接PostgreSQL資料庫，當使用者發送地區訊息給LINE Bot旅遊景點機器人時，它會讀取PostgreSQL資料庫中該地區的景點，回覆給使用者，可以搭配[[Python+LINE Bot+PostgreSQL教學]一篇搞懂LINE Bot讀取資料庫的方法](https://www.learncodewithmike.com/2020/07/python-line-bot-connect-postgresql.html)部落格文章來進行學習。

## 前置作業 ##

將專案複製(Clone)下來後，假設沒有pipenv套件管理工具，可以透過以下指令來進行安裝：

`$ pip install pipenv`

有了pipenv套件管理工具後，就可以執行以下指令，來安裝專案所需的套件：

`$ pipenv install --ignore-pipfile`

接著，登入虛擬環境，執行Django Migration(資料遷移)：

`$ pipenv shell`

`$ python manage.py makemigrations`

`$ python manage.py migrate`

## 執行畫面 ##

<img src="https://1.bp.blogspot.com/-pWJU4hLsDTs/XxQcNVZISrI/AAAAAAAADn8/IllMA7bL6-ENHBVLq4bwaq4MsVYBZ--jgCPcBGAsYHg/s2048/python_line_bot_connect_postgresql.jpg" width="350" height="700" />