from unicodedata import name
from django.contrib import admin
from django.urls import path
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    # html form을 이용해 블로그 객체 만들기
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    # django form을 이용해 블로그 객체 만들기
    path('formcreate/', views.formcreate, name='formcreate'),

    # django modelform을 이용해 블로그 객체 만들기
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),

    # 127.0.0.1:8000/detail/1
    path('detail/<int:blog_id>', views.detail, name='detail')

]

# media 파일에 접근할 수 있는 url도 추가해주어야 함
# 관례적인 코드이므로 암기 추천
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
