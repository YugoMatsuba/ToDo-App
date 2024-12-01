from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate, TaskUpdate,TaskDelete, TaskListLoginView, RegisterAccount
from .views import logout_view

#urlの一覧　どのリクエストが来たときにどの関数を返すかをpathを使って書く
urlpatterns = [
    # nameによってそのHTMLのURLを定義する。
    path("", TaskList.as_view(), name="tasks"),
    path("task/<int:pk>/", TaskDetail.as_view(), name = "task"),
    path("create-task/",TaskCreate.as_view(), name = "create-task"),
    path("edit-task/<int:pk>/",TaskUpdate.as_view(), name = "edit-task"),
    path("delete-task/<int:pk>/",TaskDelete.as_view(), name = "delete-task"),

    path("login/",TaskListLoginView.as_view(), name = "login"),
    path("logout/", logout_view, name="logout"),
    path("register/",RegisterAccount.as_view() , name="register"),
    # DetailViewやと、特定のデータをとるから、それは主キーによってどのデータかを識別する！
    # かっこによって動的な主キーの値を使える！
    # これはtask/イントの数字やったらなんでも良いって感じ　でこのintの数字はpkっていう変数なだけ！
]