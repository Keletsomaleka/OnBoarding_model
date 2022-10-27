from random import choices
from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

segmentations = (("PROFILE_SEGMENT_LEVEL_2_Emerging Middle Market Adult","PROFILE_SEGMENT_LEVEL_2_Emerging Middle Market Adult"),
                    ("PROFILE_SEGMENT_LEVEL_2_Emerging Middle Market Senior","PROFILE_SEGMENT_LEVEL_2_Emerging Middle Market Senior"),
                    ("PROFILE_SEGMENT_LEVEL_2_Established Middle Market Adult","PROFILE_SEGMENT_LEVEL_2_Established Middle Market Adult"),
                    ("PROFILE_SEGMENT_LEVEL_2_Established Middle Market Senior","PROFILE_SEGMENT_LEVEL_2_Established Middle Market Senior"),
                    ("PROFILE_SEGMENT_LEVEL_2_Established Professional","PROFILE_SEGMENT_LEVEL_2_Established Professional"),
                    ("PROFILE_SEGMENT_LEVEL_2_Established Professional Senior","PROFILE_SEGMENT_LEVEL_2_Established Professional Senior"),
                    ("PROFILE_SEGMENT_LEVEL_2_Lower ELB ","PROFILE_SEGMENT_LEVEL_2_Lower ELB "),
                    ("PROFILE_SEGMENT_LEVEL_2_Other","PROFILE_SEGMENT_LEVEL_2_Other"),
                    ("PROFILE_SEGMENT_LEVEL_2_Upper ELB","PROFILE_SEGMENT_LEVEL_2_Upper ELB"),
                    ("PROFILE_SEGMENT_LEVEL_2_Young Professional","PROFILE_SEGMENT_LEVEL_2_Young Professional"),
                    ("PROFILE_SEGMENT_LEVEL_2_Youth Kids and Teens","PROFILE_SEGMENT_LEVEL_2_Youth Kids and Teens"),
                    ("PROFILE_SEGMENT_LEVEL_2_Youth Upwardly Mobile","PROFILE_SEGMENT_LEVEL_2_Youth Upwardly Mobile"),
                    ("PROFILE_SEGMENT_LEVEL_2_Youth Young Adults","PROFILE_SEGMENT_LEVEL_2_Youth Young Adults"))

Races = (('RACE_Asian','RACE_Asian'),('RACE_Black','RACE_Black'),('RACE_Coloured','RACE_Coloured'),('RACE_Unknown','RACE_Unknown'),('RACE_White','RACE_White'))

class ModelInputs(models.Model):

    nedbank_cc = models.CharField(max_length=10,choices=(("Yes","Yes"),("No","No")))
    money_app = models.CharField(max_length=10,choices= (("Yes","Yes"),("No","No")))
    greenbacks_flag = models.CharField(max_length=60, choices= (("Yes","Yes"),("No","No")))
    profile_segmentation =models.CharField(max_length = 60, choices= segmentations)
    Race = models.CharField(max_length = 60, choices=Races)
    created_at = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    created_by = models.ForeignKey(User,on_delete = models.PROTECT,null=True, blank=True)

    def __str__(self) -> str:
        return str(self.created_by)
