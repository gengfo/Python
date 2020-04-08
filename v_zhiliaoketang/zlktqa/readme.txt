virtualenv venv



pip freeze >requirements.txt
pip install -r requirements.txt

下载css
https://v3.bootcss.com/getting-started/#download

https://www.bootcdn.cn/jquery/

导航条
https://v3.bootcss.com/components/#navbar  //制作主页面



pip install flask_sqlalchemy
pip install flask_script
pip install mysql
pip install MySQL-python


C:\Users\gengf>C:\"Program Files"\MySQL\"MySQL Server 5.5"\bin\mysql -uroot -p
oxxx1xxxxx

create database zlktqa_demo charset utf8;


cd C:\GengFO\MyProgs\GitHub\Python\v_zhiliaoketang\zlktqa

python manage.py db init
python manage.py db migrate
python manage.py db upgrade //生成user 表

