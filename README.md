# django_3rd
장고 세번째 세션 자료입니다.

## List - 실습
### `index.html`
```html
<!-- for문 템플릿 태그 -->
{% for post in posts %}
<!-- 카드 요소 시작 -->
<div class="card mb-3" style="max-width: 540px;">
    <div class="row no-gutters">
    <div class="col-md-4">
        <img src="{{ post.img.url }}" class="card-img" alt="...">
    </div>
    <div class="col-md-8">
        <div class="card-body">
        <h5 class="card-title">{{ post.title }}</h5>
        <p class="card-text">{{post.summary}}</p>
        <p class="card-text">
            <small class="text-muted">Created at: {{ post.created_at }}</small><br/>
            <small class="text-muted">Updated at: {{ post.updated_at }}</small>
        </p>
        </div>
    </div>
    </div>
</div>
<!-- 템플릿 태그를 끝내는 태그 -->
{% endfor %}
```
### `views.py`
```python
from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request): # posts에 게시글을 전부 담는다.
    posts = Post.objects.all() # posts는 글이 담긴 배열
    return render(request, "posts/index.html", {"posts":posts}) # 템플릿에서 posts로 이용
```

## Pagination - 실습
### `views.py`
```python
from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator # 추가된 코드
# Create your views here.                   # 장고 내장 페이지네이션 기능을 가져온다.
def home(request):
    posts = Post.objects.all() # posts는 게시글이 담긴 배열

    paginator = Paginator(posts, 2) # 페이지네이터 함수 사용 # 추가된 코드
    page_number = request.GET.get("page") # 페이지 넘버 가져오기 # 추가된 코드
    page_posts = paginator.get_page(page_number) # 추가된 코드

    return render(request, "posts/index.html", {"posts":page_posts}) # 변경된 코드
```

### `index.html`
```html
<!-- 페이지네이션 코드 -->
<div class="pagination">
  <span class="step-links">
    {% if posts.has_previous %}
    <a href="?page=1">&laquo; first</a>
    <a href="?page={{ posts.previous_page_number }}">previous</a>
    {% endif %}
     <span class="current">
      Page {{ posts.number }} of {{ posts.paginator.num_pages }}.
    </span>
     {% if posts.has_next %}
    <a href="?page={{ posts.next_page_number }}">next</a>
    <a href="?page={{ posts.paginator.num_pages }}">last &raquo;</a>
    {% endif %}
  </span>
</div>
<!-- 페이지네이션 코드 종료-->
```
