import json
import os.path
from final_project import settings
from django.core.management.base import BaseCommand
class Command(BaseCommand):
  help = 'import data into the database'
  
  def add_arguments(self,parser):
    pass
  
  def handle(self,**args, **options):
    path = os.path.join(settings.BASE_DIR, 'menus.json')
    