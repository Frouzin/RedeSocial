# core/models.py
from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    seguindo = models.ManyToManyField(User, related_name='seguidores', blank=True)

    def __str__(self):
        return self.user.username

class Postagem(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='postagens/', blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    curtidas = models.ManyToManyField(User, related_name='curtidas', blank=True)

    def __str__(self):
        return f'{self.autor.username} - {self.data_criacao.strftime("%Y-%m-%d %H:%M:%S")}'

class Comentario(models.Model):
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário de {self.autor.username} na postagem {self.postagem.id}'
