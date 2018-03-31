# from django.http import HttpResponse
# from .models import Board,Topics,Post
# from django.shortcuts import render,get_object_or_404,redirect
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from .forms import NewTopicForm
#
#
# def home(request):
#     boards = Board.objects.all()
#     # boards_names = list()
#     #
#     # for board in boards:
#     #     boards_names.append(board.name)
#     #
#     # response_html = '<br>'.join(boards_names)
#     #
#     # return HttpResponse(response_html)
#     return render(request,'home.html',{'boards':boards})
#
# def board_topics(request,pk ):
#     try:
#         board = Board.objects.get(pk = pk)
#     except Board.DoesNotExist:
#         raise Http404
#     return render(request,'topics.html',{'board':board})
#
#
# # def new_topic(request, pk):
# #     board = get_object_or_404(Board, pk=pk)
# #
# #     if request.method == 'POST':
# #         subject = request.POST['subject']
# #         message = request.POST['message']
# #
# #         user = User.objects.first()  # TODO: 获取当前登录的用户
# #
# #         topic = Topics.objects.create(
# #             subject=subject,
# #             board=board,
# #             starter=user
# #         )
# #
# #         post = Post.objects.create(
# #             message=message,
# #             topic=topic,
# #             create_by=user
# #         )
# #
# #         return redirect('board_topics', pk=board.pk)  # TODO: 重定向到已创建的主题页
# #
# #     return render(request, 'new_topic.html', {'board': board})
#
# @login_required   #Django有一个内置的视图装饰器来避免用户没有登录，就看到页面和表单
# def new_topic(request,pk):
#     board = get_object_or_404(Board,pk = pk)
#     user =User.objects.first() # TODO 获取当前用户
#     if request.method == 'POST':
#         form = NewTopicForm(request.POST)
#         if form.is_valid():
#             topic = form.save(commit = False)
#             topic.board = board
#             topic.starter = request.user
#             topic.save()
#             Post.objects.create(
#                 message = form.cleaned_data.get('message'),
#                 topics = topics,
#                 created_by = request.user
#             )
#             return redirect('board_topics',pk = board.pk) #TODO 重定向到新建主题页面
#
#     else:
#         form = NewTopicForm()
#     return render(request,'new_topic.html',{'board':board,'form':form})
#


from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .forms import NewTopicForm
from .models import Board, Topics, Post
from django.contrib.auth.decorators import login_required

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})

@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    # user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user
            )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})



def topic_posts(request,pk,topic_pk):
    topic = get_object_or_404(Topics,board__pk= pk,pk =topic_pk)  #取信息id
    return render(request,'topic_posts.html',{'topic':topic})
