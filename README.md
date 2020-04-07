# SSAFY Bigdata project

## Develop Notes

> [SUB1 정리](SUB1정리.md)  
> SUB2 부터는 기본기능을 제외하고는 계획한 프로젝트 설계에 맞게 진행함

## Meeting Logs

 - Zoom을 활용해서 회의함

    > [0323_월](meetingLog/0323(월).md)  
    > [0326_목](meetingLog/0326(목).md)  
    > [0331_화](meetingLog/0331(화).md)  
    > [0406_월](meetingLog/0406(월).md)  
    > [0407_화](meetingLog/0407(화).md)  


## How to Run

### Sub1

```sh
cd sub1
pip install -r requirements.txt
python parse.py
python analyse.py
python visualize.py
```

### Sub 2

**Backend**

```sh
cd sub2/backend
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py initialize
python manage.py runserver
```

**Frontend**

```sh
cd sub2/frontend
npm install
npm run serve
```
