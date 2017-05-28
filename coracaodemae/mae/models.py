from django.db import models
from django.conf import settings


class Imagens(models.Model):
    image = models.ImageField(upload_to="uploads")
    mae = models.ForeignKey('Mae')

    def __str__(self):
        return self.image.name


class Mae(models.Model):
    animais_choices = (
        ('C', 'Cachorro'),
        ('G', 'Gato'),
        ('P', 'Passaro'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    email = models.EmailField(
        verbose_name='E-mail',
        max_length=255,
        unique=True,
    )
    nome = models.CharField(max_length=250, verbose_name='Nome completo')
    facebook_id = models.IntegerField(verbose_name='Facebook ID')
    ibm_verificado_mulher = models.BooleanField(
        verbose_name='API da IBM verificou se é mulher.')
    ibm_personalidade = models.TextField(verbose_name='IBM Personalidade', default='', blank=True)
    foto_mae_gd = models.ImageField(
        upload_to='uploads', verbose_name="Foto da Mãe grande")
    foto_mae_pq = models.ImageField(
        upload_to='uploads', verbose_name="Foto da Mãe Pequena")
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    endereco = models.CharField(max_length=100, verbose_name='Endereço')
    bairro = models.CharField(max_length=100, verbose_name='Bairro')
    cep = models.IntegerField(verbose_name="CEP")
    aceita_crianca_especial = models.BooleanField(
        verbose_name='Aceita crianças especiais')
    idade_minima_crianca = models.IntegerField(
        verbose_name='Idade mínima da criança', null=False)
    idade_maxima_crianca = models.IntegerField(
        verbose_name='Idade maxima da criança', null=False)
    telefone = models.IntegerField(verbose_name='Telefone')
    valor_hora = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name='Valor/Hora', null=False)
    descricao = models.TextField(verbose_name='Descrição')
    disponivel_segunda = models.BooleanField(verbose_name="Segunda")
    disponivel_terca = models.BooleanField(verbose_name="Terça")
    disponivel_quarta = models.BooleanField(verbose_name="Quarta")
    disponivel_quinta = models.BooleanField(verbose_name="Quinta")
    disponivel_sexta = models.BooleanField(verbose_name="Sexta")
    disponivel_sabado = models.BooleanField(verbose_name="Sábado")
    disponivel_domingo = models.BooleanField(verbose_name="Domingo")
    disponivel_hora_inicio = models.TimeField(
        verbose_name='Hora inicio', blank=True)
    disponivel_hora_fim = models.TimeField(verbose_name='Hora fim', blank=True)
    animal_estimacao = models.CharField(
        max_length=1, choices=animais_choices, verbose_name="Animais de estimação")

    def __str__(self):
        return self.user.username

    def get_all_posts(self):
        _text = ''
        for t in self.posts_set.all():
            _text += t.post
            _text += "\n"

        return _text.encode('utf-8', errors="replace")

    def get_order_watson(self, mae):
        return 1


class Friends(models.Model):
    mae = models.ForeignKey(Mae)
    nome = models.CharField(max_length=250, verbose_name='Nome')

    def __str__(self):
        return self.nome


class Posts(models.Model):
    mae = models.ForeignKey(Mae)
    post = models.TextField(verbose_name='post')

    def __str__(self):
        return self.post


class Filho(models.Model):
    sexo_choices = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    )
    mae = models.ForeignKey(Mae)

    nome = models.CharField(max_length=250, verbose_name='Nome')
    sexo = models.CharField(
        max_length=1, choices=sexo_choices, verbose_name="Sexo")
    crianca_especial = models.BooleanField(
        verbose_name="É criança com cuidados especiais")
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    alergico = models.CharField(
        max_length=250, verbose_name='Alergias', blank=True)
    doencas = models.TextField(verbose_name='Doenças', blank=True)
    escola = models.CharField(max_length=50, verbose_name="Escola", blank=True)
    cep_escola = models.IntegerField(
        verbose_name="Cep Escola", blank=True, null=True)
    natacao = models.BooleanField(verbose_name='Faz natação')
    cep_natacao = models.IntegerField(
        verbose_name='Cep Natação', blank=True, null=True)
    judo = models.BooleanField(verbose_name='Faz judo')
    cep_judo = models.IntegerField(
        verbose_name='Cep judo', blank=True, null=True)
    bale = models.BooleanField(verbose_name='Faz bale')
    cep_bale = models.IntegerField(
        verbose_name='Cep bale', blank=True, null=True)
    ingles = models.BooleanField(verbose_name='Faz ingles')
    cep_ingles = models.IntegerField(
        verbose_name='Cep ingles', blank=True, null=True)

    def __str__(self):
        return self.nome


class ComentarioMae(models.Model):
    created_at = models.DateTimeField("Criado em", auto_now=True)
    comentario = models.TextField(verbose_name='Comentario')
    mae_origem = models.ForeignKey(Mae, related_name="mae_origem_comentario")
    mae_destino = models.ForeignKey(Mae, related_name="mae_destino_comentario")

    def __str__(self):
        return "Comentario para %s" % str(self.mae_destino)


class AvaliacaoMae(models.Model):
    created_at = models.DateTimeField("Criado em", auto_now=True)
    mae_origem = models.ForeignKey(Mae, related_name="mae_origem_avaliacao")
    mae_destino = models.ForeignKey(Mae, related_name="mae_destino_avaliacao")
    avaliacao = models.IntegerField(verbose_name='Avaliacao', blank=True, null=True)

    def __str__(self):
        return "Avaliação para %s" % str(self.mae_destino)


class ApoioMae(models.Model):
    created_at = models.DateTimeField("Criado em", auto_now=True)
    mae_origem = models.ForeignKey(Mae, related_name="mae_origem")
    mae_destino = models.ForeignKey(Mae, related_name="mae_destino")
    data_inicio = models.DateTimeField("Data inicio")
    data_fim = models.DateTimeField("Data final")
    foi_processado = models.BooleanField(verbose_name='Foi processado?')
    qtd_horas = models.IntegerField(verbose_name='Quantidade de horas', blank=True, null=True)
    valor_hora = models.IntegerField(verbose_name='Valor hora', blank=True, null=True)

    def __str__(self):
        return "Apoio da %s para a %s" % (str(self.mae_destino), str(self.mae_origem))


class ApoioMaeFilhos(models.Model):
    apoio_mae = models.ForeignKey(ApoioMae)
    filho = models.ForeignKey(Filho)

    def __str__(self):
        return "%s Filho %s" % (str(self.apoio_mae), str(self.filho))
