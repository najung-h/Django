from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

# --- Read ---


def index(request):
    """전체 게시글 목록을 조회하여 index.html 페이지를 렌더링"""
    # 1. Article 모델을 통해 DB에 저장된 모든 데이터를 조회
    articles = Article.objects.all()

    # 2. 조회된 데이터를 템플릿에 전달하기 위해 context 딕셔너리에 담음
    #    템플릿에서는 'articles'라는 키로 QuerySet 객체에 접근할 수 있음
    context = {
        'articles': articles,
    }
    # 3. request, 템플릿 경로, context를 render 함수에 전달하여 최종 HTML을 생성하고 사용자에게 응답
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    """특정 pk(Primary Key)를 가진 게시글 하나를 조회하여 detail.html 페이지를 렌더링"""
    # 1. URL로부터 전달받은 pk 값을 사용하여, 해당 pk를 가진 Article 객체 하나를 조회
    article = Article.objects.get(pk=pk)

    # 2. 조회된 단일 게시글 객체를 context에 담아 템플릿에 전달
    context = {
        'article': article,
    }
    # 3. detail.html 템플릿을 렌더링
    return render(request, 'articles/detail.html', context)


# --- Create ---


def new(request):
    """새로운 게시글을 작성할 수 있는 new.html 페이지를 렌더링"""
    # 사용자가 데이터를 입력할 수 있는 빈 form 페이지를 보여주는 역할만 함
    return render(request, 'articles/new.html')


def create(request):
    """사용자가 form을 통해 제출한 데이터를 DB에 저장"""
    # 1. new.html의 form에서 POST 방식으로 전송된 데이터를 추출
    #    request.POST는 form 데이터가 담긴 딕셔너리 유사 객체
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 2. 추출된 데이터를 바탕으로 Article 모델의 새 인스턴스(객체)를 생성
    article = Article(title=title, content=content)
    # 3. .save() 메서드를 호출하여, 인스턴스의 데이터를 DB 테이블에 실제로 저장
    article.save()

    # 4. 데이터 저장이 완료된 후, 사용자를 방금 생성된 게시글의 상세 페이지로 이동시킴
    #    redirect는 클라이언트에게 "이 URL로 다시 요청해 줘!"라고 지시하는 응답
    #    'articles:detail'은 articles 앱의 detail이라는 이름의 URL을 의미
    return redirect('articles:detail', article.pk)


# --- Delete ---


def delete(request, pk):
    """특정 pk를 가진 게시글을 DB에서 삭제"""
    # 1. 삭제할 게시글을 pk를 이용해 조회
    article = Article.objects.get(pk=pk)

    # 2. 조회된 객체의 .delete() 메서드를 호출하여, DB에서 해당 레코드를 삭제(DELETE)
    article.delete()

    # 3. 게시글 삭제 후, 전체 목록 페이지로 이동
    return redirect('articles:index')


# --- Update ---


def edit(request, pk):
    """기존 게시글을 수정할 수 있는 edit.html 페이지를 렌더링"""
    # 1. 수정할 게시글의 기존 데이터를 pk를 이용해 조회
    article = Article.objects.get(pk=pk)

    # 2. 조회된 데이터를 form에 미리 채워넣기 위해 context에 담아 템플릿에 전달
    context = {
        'article': article,
    }
    # 3. edit.html 템플릿을 렌더링
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    """사용자가 form을 통해 제출한 수정 데이터를 DB에 반영(UPDATE)"""
    # 1. 수정할 게시글을 pk를 이용해 조회
    article = Article.objects.get(pk=pk)

    # 2. edit.html의 form에서 POST 방식으로 전송된 새로운 데이터를 추출
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 3. 조회된 인스턴스의 필드 값을 새로운 데이터로 덮어씀
    article.title = title
    article.content = content
    # 4. .save() 메서드를 호출하여, 변경된 내용을 DB에 실제로 반영(UPDATE)
    article.save()

    # 5. 수정이 완료된 후, 해당 게시글의 상세 페이지로 이동
    return redirect('articles:detail', article.pk)
