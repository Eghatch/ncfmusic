from django.db import models

def Listen(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=255)
    mp3 = models.FileField(upload_to='/ext/listen')
    songwriter = models.ForeignKey('Contributor')
    producer = models.CharField(max_length=128, null=True, blank=True)
    vocals = models.ManyToManyField('Contributor', null=True)
    instruments = models.ForeignKey('Contributor', null=True)
    release_date = models.DateField(null=True, blank=True)
    album_title = models.CharField(max_length=256, null=True)
    church = models.ForeignKey('Church')
    insert_date = models.DateField(auto_now_add=True)
    
def Watch(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=255)
    description = models.TextField(null=True, blank=True)
    church = models.ForeignKey('Church', null=True)
    date = models.DateField(null=True, blank=True)
    vimeo_embed_code = models.CharField(max_length=512)
    duration = models.CharField(max_length=16)
    insert_date = models.DateField(auto_now_add=True)
    
def Tutorial(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=255)
    date = models.DateField()
    duration = models.CharField(max_length=16)
    author = models.ForeignKey('Contributor')
    church = models.ForeignKey('Church')
    teaser = models.TextField()
    vimeo_embed_code = models.CharField(max_length=512)
    insert_date = models.DateField(auto_now_add=True)
    
def Talk(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=255)
    teaser = models.TextField()
    date = models.DateField()
    author = models.ForeignKey('Contributor')
    church = models.ForeignKey('Contributor')
    duration = models.CharField(max_length=16)
    mp3 = models.FileField(upload_to='/ext/talks')
    
def Article(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=255)
    teaser = models.TextField()
    date = models.DateField()
    author = models.ForeignKey('Contributor')
    church = models.ForeignKey('Church')
    article_body = models.TextField()
    
def Song(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=255)
    songwriter = models.ForeignKey('Contributor')
    church = models.ForeignKey('Church')
    sheet_music = models.FileField(upload_to='/ext/sheet_music', null=True, blank=True)
    slides = models.FileField(upload_to='/ext/slides', null=True, blank=True)
    lyrics = models.FileField(upload_to='/ext/lyrics', null=True, blank=True)
    producer = models.CharField(max_length=256, null=True, blank=True)
    vocals = models.ManyToManyField('Musician', null=True)
    instruments = models.ManyToManyField('Musician', null=True)
    release_date = models.DateField()
    album_title = models.CharField(max_length=256, null=True, blank=True)
    
def Event(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    time = models.CharField(max_length=64)
    church = models.ForeignKey('Church')
    city = models.CharField(max_length=256)
    teaser = models.TextField()
    artile_body = models.TextField()
    photo = models.FileField(upload_to='/ext/events', null=True, blank=True)
    
def Church(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=255)
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=128, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    coords = models.CharField(max_length=128)
    
def Contributor(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=255)
    title = models.CharField(max_length=128)
    church = models.ForeignKey('Church')
    city = models.CharField(max_length=256)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=32)
    website = models.URLField(null=True, blank=True)
    buy_music_url = models.URLField(null=True, blank=True)
    
def Contact(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email_address = models.EmailField()
    insert_date = models.DateField(auto_now_add=True)
    
def Page(models.Model):
    from ncfmusic.apps.heroshots import Image
    
    slug = models.SlugField(max_length=255)
    content = models.TextField(blank=True, null=True)
    heroshot = models.ForeignKey(Image)
    
    
    