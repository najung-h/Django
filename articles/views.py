from django.shortcuts import render

# Create your views here.

# views.py
# 메인 페이지를 응답하는 함수

# 아래 내용은 쓰고 말고의 고민의 대상이 아니라, 그냥 써야하는 내용임.
# 약속 : 모든(필수) view 함수는 첫 번째 인자로 요청 객체를 필수적으로 받음
def index(request): # 매개변수 이름은 request가 아니어도 되지만 관례적으로 request로 작성함
    return render(request, 'articles/index.html') #templates는 약속한거라 안 써도 됨.



