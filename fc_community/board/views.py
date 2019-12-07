from django.shortcuts import render, redirect
from django.http import Http404
from django.core.paginator import Paginator
from .models import Board
from fcuser.models import Fcuser
from tag.models import Tag
from .form import BoardForm

# Create your views here.


def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')

    return render(request, 'board_detail.html', {'board': board})


def board_writer(request):

    if not request.session.get('user'):
        return redirect('/fcuser/login/')

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)

            board = Board()
            board.title = form.cleaned_data.get('title')
            board.contents = form.cleaned_data.get('contents')
            board.writer = fcuser
            board.save()

            tags = form.cleaned_data.get('tags').split(',')
            for tag in tags:
                if not tag:
                    continue

                # _tag, created = Tag.objects.get_or_create(name=tag)
                # 사용하지 않는 값은 _으로 사용한다.
                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)

            return redirect('/board/list/')

    else:
        form = BoardForm()

    return render(request, 'board_writer.html', {'form': form})


def board_list(request):
    all_boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('curPage', 1))
    paginator = Paginator(all_boards, 3)
    boards = paginator.get_page(page)
    return render(request, 'board_list.html', {'boards': boards})
