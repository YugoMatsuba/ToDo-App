from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth import logout
from django.shortcuts import redirect

from django.urls import reverse_lazy

from todoapp.models import Task

# Create your views here.

# htmlを返す関数とかはここに書くしデータベースとやり取りをする仕組みもここに書く！
# 関数じゃなくてもクラスで行けて、いろんなクラスのテンプレートみたいなのがある！
# ListView**はDjangoの汎用ビュー（Generic View）の一つで、データを一覧表示するための機能を持ったクラス
# 関数みたいにHTML返せるん？どうやったらHTML返せる？

# いや関数とは違ってそもそも
# 一覧データを表示するためのビュー　object_list
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    # object_listの名前も変更できる　デフォルトでそれなだけで！
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user = self.request.user)

        searchInputText = self.request.GET.get("search")
        if searchInputText:
            context["tasks"] = context["tasks"].filter(title__icontains = searchInputText)

        context["search"] = searchInputText
        return context


# 特定のデータを表示するためのビュー object
class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = "task"

# データを追加するビュー
class TaskCreate(CreateView):
    model = Task
    fields = ["title", "description", "completed"]
    # クリエイトしたあと（フォームで）どのサイトに行くべきかを指定する！tasksっていう一覧画面にいく　pathでその画面に名前つけているから！
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# これに対応するHTMLのフォームに含めるフィールド
# CreateViewではフォームを使ってデータをテーブルに追加するから。
class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = "__all__"
    # クリエイトしたあと（フォームで）どのサイトに行くべきかを指定する！tasksっていう一覧画面にいく　pathでその画面に名前つけているから！
    success_url = reverse_lazy("tasks")
class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    fields = "__all__"
    # クリエイトしたあと（フォームで）どのサイトに行くべきかを指定する！tasksっていう一覧画面にいく　pathでその画面に名前つけているから！
    success_url = reverse_lazy("tasks")
    context_object_name = "task"

class TaskListLoginView(LoginView):
    fields = "__all__"
    template_name = "todoapp/login.html"

    def get_success_url(self):
        return reverse_lazy("tasks")
    
def logout_view(request):
    logout(request)  # ユーザーをログアウト
    return redirect("login") 

class RegisterAccount(FormView):
    template_name = "todoapp/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)