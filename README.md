# Django

> 앞으로 기본 CRUD 로직은 지금 작성된 구조로 균일하게 작성 예정입니다.



* Django Article CRUD
* Django Auth
* Django 1:N
  * Article - Comment
  * User - Article



## 추가 라이브러리

* [django-bootstrap4](https://django-bootstrap4.readthedocs.io/en/latest/index.html)

* 활용하기 위해서 반드시 설치를 진행하셔야 합니다.
* 해당 문서를 보고 직접 설치, 등록을 해보세요 :)

## 이미지 업로드

### 1. ImageField

* 단순 ImageField를 활용하기 위해서는 `pillow` 패키지가 반드시 필요하다.

```bash
$ pip install pillow
```

### 2. resizing

* Resizing을 위해서는 `pilkit`, `django-imagekit` 패키지가 필요하다.

```bash
$ pip install pilkit django-imagekit
```
