from django.db import models

class Album(models.Model):

    photo       = models.ImageField(verbose_name="フォト",upload_to="upload/album/photo/")

class Document(models.Model):

    file        = models.FileField(verbose_name="ファイル",upload_to="upload/document/file/")

