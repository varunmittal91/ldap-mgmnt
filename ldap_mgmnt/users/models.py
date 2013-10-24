from django.db import models

class user_list(models.Model):
	uuid   = models.CharField(max_length=64)
        uid    = models.IntegerField(default=0)
        gid    = models.IntegerField(default=0)
        f_name = models.CharField(max_length=10)
        l_name = models.CharField(max_length=10)
        
