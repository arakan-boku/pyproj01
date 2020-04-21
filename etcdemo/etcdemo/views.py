from django.shortcuts import render
from . import form as fm
from django.template.context_processors import csrf
from .functions import functions as func


"""
学習済のWORD2VECモデルを利用して、入力単語の計算や近い言葉の表示を行うデモ
"""


def demo01(request):
    word2vec = func.Demo01Functions()
    if request.method == 'POST':
        # テキストボックスに入力されたメッセージ
        plusinput = request.POST["textplus"]
        minusinput = request.POST["textminus"]
        results, expstr = word2vec.get_result(plusinput, minusinput)
        # 描画準備
        form = fm.Demo01Form(label_suffix='：')
        c = {
            'form': form,
            'expstr': expstr,
            'result1': str(results[0][0]),
            'result2': str(results[0][1])
        }
    else:
        # フォームの初期化
        form = fm.Demo01Form(label_suffix='：')
        c = {'form': form}
        c.update(csrf(request))
    return render(request, 'similar.html', c)


def demo02(request):
    model = func.Demo02Function()
    if request.method == 'POST':
        img = request.POST["areaone"]
        ans, base64_img = model.predict_from_base64(img)
        c = {
            'base64text': img,
            'decodeimg': base64_img,
            'enlabel': ans['en'],
            'jplabel': ans['jp'],
            'pplabel': ans['pp'],
        }
    else:
        form = fm.Demo02Form(label_suffix='：')
        c = {'form': form}
        c.update(csrf(request))
    return render(request, 'dragdrop.html', c)
