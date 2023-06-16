# 23 06 16 프로젝트

## Project Settings
1. `venv` 활용
1. project name: mtv_practice
2. directory settings
    - `MTV_PRACTICE/` (Project dir)
        - `mtv_practice/` (master app)
        - `blog/` (app)
            - `templates/`
                - `blog/`
                    - `new.html`
                    - `index.html`
                    - `detail.html`
                    - `edit.html`
            - `models.py`
            - `views.py`
            - `urls.py`
            - `...`
        - `templates/`
            - `base.html`
        - `manage.py`
        - `.gitignore`
        - `README.md`
        - `...`

## App `blog/`

## Modeling
### `class Posting`
|column|type|
|---|---|
|`title`|CharField(100)|
|`content`|TextField|
|`rank`|IntegerField|
|`created_at`|DateTimeField|
|`updated_at`|DateTimeField|


### URL pattern - View function name
1. `/blog/new/` => `new`
    - 새로운 Posting 작성용 HTML
    - `new.html`
2. `/blog/create/` => `create`
    - 새로운 Posting 저장
    - `POST` 요청 방식으로 동작
3. `/blog/` => `index`
    - 모든 Posting 조회
    - `index.html`
4. `/blog/1/` => `detail`
    - 단일 Posting 조회
    - `detail.html`
5. `/blog/1/edit/` => `edit`
    - 단일 Posting 수정용 HTML
    - `edit.html`
6. `/blog/1/update/` => `update`
    - 수정된 Posting 저장
    - `POST` 요청 방식으로 동작
7. `/blog/1/delete/` => `delete`
    - 단일 Posting 삭제
    - `POST` 요청 방식으로 동작


### Template
- 모두 Bootstrap을 사용하며, Nav Bar 가 존재해야함.
- `<form>` 은 Bootstrap Form control 활용
- 게시글 목록은 다양한 컴포넌트(card/table)를 활용해 보자
