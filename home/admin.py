from django.contrib import admin
from home.models import Person
from home.models import Data
from home.models import AI_summery
from home.models import total_hits
# Register your models here.
admin.site.register(Person)
admin.site.register(Data)
admin.site.register(AI_summery)
admin.site.register(total_hits)