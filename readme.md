# <To Do List>
  

## Web App with Python and Flask

#### 황준하 / Joon Ha Hwang    2022.05.08


## 1. 목적

: Pyton 과 Flask 를 사용하여 Web App 생성

  
  
## 2. 구조

- 사용 툴 : Python, Flask, Flask_Sqlalchemy, render_templates, url_for, flash, wtforms, Jinja template, html, Sqlite

  
  * /templates : html 코드
  
  
  1. app.py 를 통해 실행
  2. route.py 내에 각 route('/index', '/edit', '/delete' 등)에 대한 정의 및 정보들 존재
  3. forms.py 내에 class 'AddTaskform', 'DeleteTaskFrom' 정의
  4. models.py 내에 사용되는 db(Sqlite)에 대한 구조 정의
  5. data.db 내에 입력한 Task 들이 
  
  
## 3. Web App 기능

To Do List

- 기능 : 입력, 수정, 삭제
  
![스크린샷 2022-05-09 오후 2 05 54](https://user-images.githubusercontent.com/104884525/167344094-dbc4dcec-4207-4256-804e-b5475c7b5154.png)

: 하고자 하는 Task 를 Add 하여 목록에 추가

  
![스크린샷 2022-05-09 오후 2 07 11](https://user-images.githubusercontent.com/104884525/167344186-75e644be-be86-4a05-b7d7-cd74114c53ad.png)

: "Task added to the database" 라는 문구와 함께 입력한 Task 가 <Tasks> 에 추가
  
  
![스크린샷 2022-05-09 오후 2 08 48](https://user-images.githubusercontent.com/104884525/167344350-5b1982be-6bdc-4ef5-b03b-01a0915a5e3d.png)

: edit 버튼을 통해 입력했던 Task 를 수정할 수 있음
  
  
![스크린샷 2022-05-09 오후 2 09 38](https://user-images.githubusercontent.com/104884525/167344418-e19079b8-6075-4502-8954-268814e33bb0.png)
  
: "Task has been updated" 라는 문구와 함께 입력한 Task 가 수정됨
  
  
![스크린샷 2022-05-09 오후 2 10 25](https://user-images.githubusercontent.com/104884525/167344487-de7efdac-5261-4788-a103-332a1e606409.png)

: delete 버튼을 통해 입력했던 Task 를 삭제 가능 / 해당 Task 를 삭제할 것이냐는 확인 문구

  
![스크린샷 2022-05-09 오후 2 11 12](https://user-images.githubusercontent.com/104884525/167344568-633e6233-9fc3-4494-897f-e9b7da885f59.png)

: "Task has been deleted" 라는 문구와 함께 입력한 Task 가 삭제됨
