# Login

- Create Custom User Model
  
- 기본 사용자 모델을 AbstractUser 모델로 설정
- 기존 인증 기능(username,password)을 이메일을 username으로 사용하기 위해 선정
-  UserProfile 형태로 OneToOne 관계를 추가하고, 이메일 필드를 사용자 인증용 private key로 설정

- admin.py 수정
    - profile이 user 모델의 일부가 되도록 인라인 객체로 정의하고 userAdmin 클래스 튜플에 추가

- python manage.py createsuperuser
    ```
    Email address: admin@google.com
    Username: admin
    First name: test
    Last name: admin
    Password:1234
    Password (again):1234
    ```

- UserSerializer 추가
- DefaultRouter를 이용하므로 User 관련 REST도 제공됨

- JWT 인증 추가
   - settings.py에 'rest_framework.authtoken', 'rest_auth' 추가
   - urls.py에 auth 관련 url 추가
   - 권한 설정을 통해 모든 사용자가 다른 사용자의 프로필에 액세스 할 수 없음
      - 슈퍼계정으로 로그인 또는 유저 로그인하여서 stores, users 에 접근가능
   - permisstions.py 추가

 - 추후에 social login 추가 예정
 
## Requirements 추가

```
Pillow==7.1.0
djangorestframework-jwt==1.11.0
django-rest-auth==0.9.5
```

## Django의 인증과정만 이용하도록 축소