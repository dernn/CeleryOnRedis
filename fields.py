# Non-project [study]
from django.db import models

# Fields
object_id = models.AutoField()
boolean = models.BooleanField(default=False)
small_string = models.CharField(max_length=64,
                                default="Default value")
some_data = models.DateField(auto_now_add=True)
some_datetime = models.DateTimeField(auto_now_add=True)
personal_email = models.EmailField()
file_field = models.FileField()
file_path = models.FilePathField()
price = models.FloatField(default=0.99)
user_avatar = models.ImageField()
count = models.IntegerField(default=0)
article_text = models.TextField()
tea_time = models.TimeField()
link = models.URLField()

# Relations
# some_model — это модель, к которой строится связь
one_to_one_relation = models.OneToOneField(some_model)
one_to_many_relation = models.ForeignKey(some_model)
many_to_many_relation = models.ManyToManyField(some_model)

