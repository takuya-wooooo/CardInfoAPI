from django.contrib import admin
import sys
sys.path.append('../')
from cards.models import CreditCard

admin.site.register(CreditCard)
