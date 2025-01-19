# DVC-Data-Versoning

## Step1:
Create git repository and clone it to the local

## Step2:
Create a python file (copy.py) and add code to it (i.e it will save a csv file to a new data folder).

## Step3:
Do the git add and commit before initializing the DVC

## Step4:
pip install dvc
Initalize the DVC. Do "dvc init" (creates .dvcignore, .dvc)

## Step5:
Now make directory S3 "mkdir S3"

## Step6:
Store dataset remotely in S3 "dvc remote add -d myremote S3"

## Step7:
Track your dataset "dvc add data/"

Note:
To stop tracking from Git:
git rm -r --cached 'data'
git commit -m "stop tracking data"

Now track again the dataset with "dvc add data/"
To track changes with git "git add .gitignore data.dvc"
To enable auto staging run "dvc config core.autostage true"

## Step8:
Commit and push with "dvc commit" and "dvc push"

## Step9:
Do git add, commit and push to mark this stage as first version of data.

## Step10:
Try to make changes to my_code.py to append new row in the data, check changes via "dvc status"

## Step11:
Again commit and push with "dvc commit" and "dvc push"

## Step12:
Do git add, commit and push to mark this stage as second version of data.

## Step13:
Check dvc/git status, everything should be up to date

## Step14:
Now repeat steps 10-12 to this stage as third version of data