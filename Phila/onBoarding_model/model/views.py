import re
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ModelInputForm
from xgboost import XGBClassifier 
import pandas as pd
import numpy as np
from joblib import load

def yes_no(cc,money_app,greenbacks):

    if cc =="Yes":
        cc = 'NEDBANK_CC'
    else:
        cc = 0
        
    if money_app =="Yes":
        money_app = 'NEDBANK_CC'
    else:
        money_app = 0
        
    if greenbacks =="Yes":
        greenbacks = 'NEDBANK_CC'
    else:
        greenbacks = 0
    
    return [cc,money_app,greenbacks] 


def signup(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')

    else:
        form = UserCreationForm()
    return render(request, 'model/signup.html',{'form':form})

@login_required
def model_view(request):

    if request.method == "POST":

        form  = ModelInputForm(request.POST)
        if form.is_valid():
            form.save()

            nedbank_cc = str(request.POST['nedbank_cc'])
            money_app = str(request.POST['money_app'])
            greenbacks_flag = str(request.POST['greenbacks_flag'])
            profile_segmentation = str(request.POST['profile_segmentation'])
            Race = str(request.POST['Race'])

            model = load(r"C:\Users\NB322079\Documents\Phila\onBoarding_model\model\base_xgb_no_campaign_v3.joblib.dat")

            boolist = yes_no(nedbank_cc,money_app,greenbacks_flag)

            nedbank_cc = boolist[0]
            money_app = boolist[1]
            greenbacks_flag = boolist[2]

            column_list = ['NEDBANK_CC','MONEY_APP_FLAG','GREENBACKS_MEMBER_FLAG','PROFILE_SEGMENT_LEVEL_2_Emerging Middle Market Adult',
                'PROFILE_SEGMENT_LEVEL_2_Emerging Middle Market Senior','PROFILE_SEGMENT_LEVEL_2_Established Middle Market Adult',
                    'PROFILE_SEGMENT_LEVEL_2_Established Middle Market Senior','PROFILE_SEGMENT_LEVEL_2_Established Professional',
                    'PROFILE_SEGMENT_LEVEL_2_Established Professional Senior','PROFILE_SEGMENT_LEVEL_2_Lower ELB','PROFILE_SEGMENT_LEVEL_2_Other',
                    'PROFILE_SEGMENT_LEVEL_2_Upper ELB','PROFILE_SEGMENT_LEVEL_2_Young Professional','PROFILE_SEGMENT_LEVEL_2_Youth Kids and Teens',
                    'PROFILE_SEGMENT_LEVEL_2_Youth Upwardly Mobile','PROFILE_SEGMENT_LEVEL_2_Youth Young Adults',
                    'RACE_Asian','RACE_Black','RACE_Coloured','RACE_Unknown','RACE_White']

            value_list = [nedbank_cc,money_app,greenbacks_flag,profile_segmentation,Race]

            encode = [1 if i in value_list else 0 for i in column_list]


            df = pd.DataFrame(columns=column_list)

            df.loc[len(df)] = encode

            for i in df.columns:
    
                df[[i]] = df[[i]].apply(pd.to_numeric)

            prediction = model.predict_proba(df)

            print(prediction)



            field_dict = {
                "nedbank_cc":nedbank_cc,
                "money_app":money_app,
                "greenbacks_flag":greenbacks_flag,
                "profile_segmentation":profile_segmentation,
                "Race":Race
            }

            df = pd.DataFrame(field_dict, index=[0])
            print(df)

        return render(request, 'model/result.html',{'result':round(prediction[0][1]*100,2)})

    

    else:

        form = ModelInputForm()

    return render(request,'model/home.html', {'form':form})