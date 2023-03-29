# 장고 프로젝트 가이드
## 1. 가상환경 설정
- 가상환경 만들기
```bash
python -m venv venv 
```
- 가상환경 실행하기
```bash
# MacOS 기준
source venv/bin/activate
```
- 장고 설치하기
```bash
pip install django==3.2.18
```
- 의존성 파일 생성
```bash
# 패키지 설치시 마다 갱신
# 이름을 꼭 requirement.txt로 할 것
pip freeze > requirement.txt
```
## 2. 장고 설정
- 프로젝트 만들기
```bash
django-admin startproject pjt .
```
- 앱 만들기
```bash
python manage.py startapp todos
```
- 앱 등록
```py
# pjt/settings.py
INSTALLED_APPS = [
    'todos',
]
```
## 3. DB 설정

