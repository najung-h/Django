from django import forms
from .models import Article

# Ariticle로 해도 상관없음, 기존에 model의 article과 구분하기 위함일 뿐.
# class ArticleForm(forms.Form): 
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea) #Text Fields 없음. # 위젯 기능
    

class ArticleForm(forms.ModelForm):
    class Meta:  # 메타데이터 # 데이터에 대한 데이터 / 데이터를 설명하는 데이터 / 사진
        model = Article
        fields = '__all__'
    # 데이터 제약 조건, 웨젯, 필드 정해준 적 없어요. 근데 알아서 지정해주었어요.
    # 왜냐하면, models.py에 이만큼을 알고 있는거에요.
        