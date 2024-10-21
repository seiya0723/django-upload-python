from django.shortcuts import render,redirect
from django.views import View

from .models import Document
from .forms import DocumentForm

from django.conf import settings
import subprocess

class IndexView(View):
    def get(self, request, *args, **kwargs):

        context                 = {}
        context["documents"]    = Document.objects.all()


        # アップロードされたPythonを実行する。
        document        = Document.objects.filter(id=1).first()

        # アップロードされたPythonプログラムのファイルパスを作成
        program_path    = str(settings.BASE_DIR) + document.file.url

        # 仮想環境のファイルパスを作成(pythonファイルのある場所)
        venv_path       = str(settings.BASE_DIR) + "/venv/bin/"
        
        # 実行結果を出力する。(仮想環境を有効にする)
        result  = subprocess.run(["python", program_path], capture_output=True,text=True , cwd=venv_path)
        print(result.stdout)

        return render(request,"upload/index.html",context)

    def post(self, request, *args, **kwargs):

        form        = DocumentForm(request.POST,request.FILES)

        if not form.is_valid():
            print("バリデーションNG")
            print(form.errors)
            return redirect("upload:document")

        print("バリデーションOK")
        form.save()

        return redirect("upload:index")

index   = IndexView.as_view()


