import  datetime
from    decouple import config # NB remove + config(api) will be replaced with github secrets
import  pandas as pd
from    pandas.tseries.offsets import DateOffset
import  pprint
import  requests
import  smtplib, ssl
import  sys

def github_request():
    for x in sys.argv[1:]: # for arguments for secrets
      print(x)  
    # Make api request with Github credential token
    headers = {'Authorization': 'token ' + config('api')}
    response = requests.get('https://api.github.com/users/Nkosinathi-Bonga-James-Mncube/repos',headers=headers)
    create_dataframe(response)
    
def create_dataframe(response): # Sort json value from key in API get request
    # pprint.pprint(response.json()[1])
    project_name = [k['name'] for k in response.json() if not k['fork'] == True]
    project_created = [k['created_at'] for k in response.json() if not k['fork'] == True]
    project_description = [k['description'] for k in response.json() if not k['fork'] == True]
    project_url = [k['html_url'] for k in response.json() if not k['fork'] == True]
    
    # Create a dictionary from json values 
    data_df = {
                'Project_name':project_name,
                'Created_at':project_created,
                'Description':project_description,
                'html_url':project_url
    }
    df=pd.DataFrame(data_df,columns=['Project_name','Created_at','Description','html_url'])
    display_repos(df)

def fail_msg(df,x):
  f=open("fail.txt","w")
  f.write(f'***THIS IS A AUTOMATED MESSAGE***\n')
  f.write(f'!!!!! F A I L E D !!!\n')
  f.write(f'\n')
  f.write(f'\nNo new project for the month of {x.strftime("%b")} :( Please contribute more and make public!\n')
  # txt_file.close()
  y=datetime.datetime.now()
  each_repo = df.loc[df['Created_at'].dt.year==y.year].values
  f.write(f'\nContributions for the year so far: {each_repo.shape[0]} repos\n')
  for k in each_repo:
    f.write(f'\n> {k[1].day}-{k[1].strftime("%b")}-{k[1].year}\n Project: {k[0]} - ({k[2]})\n{k[3]}\n')
  f.write(f'\n----------------------------------------------------\nThis report is generated by my own project at :\nhttps://github.com/Nkosinathi-Bonga-James-Mncube/Linkedin_post_automation\n-----------------------------------------------------')
  f.close()
  send_textfile=open("fail.txt","r")
  send_email(send_textfile)
  send_textfile.close()

def display_repos(df):
    # Create dataframe based on dictionary
    df.sort_values(by=['Created_at'],inplace=True,ascending=False)
    df['Created_at']= pd.to_datetime(df['Created_at']) # convert to Date.time.object
    # print(df) # debug
    # x=datetime.datetime.now()+ pd.DateOffset(months=-1) # check previous month (i.e -1)
    x=datetime.date.fromisoformat('2021-01-01')+ pd.DateOffset(months=-1) # debug
    each_repo = df.loc[df['Created_at'].dt.month==x.month].values # find all dates with the previous month in series Created_at
    if each_repo.size == 0:  
      fail_msg(df,x)
    else:
      f=open("report.txt","w")
      f.write(f'***THIS IS A AUTOMATED MESSAGE***\n')
      f.write(f'\nMy Github report\n')
      f.write(f'------------------------------------------\nLatest project for {x.strftime("%b")}-{x.year} \n------------------------------------------\n')
      f.write(f'You have a total of {each_repo.shape[0]} new Projects:\n') # return number of total turples with is total number of projects
      for k in each_repo:
        f.write(f'\n> Project : {k[0]} - ({k[2]})\n{k[3]}\n')
      f.write(f'\n----------------------------------------------------\nThis report is generated by my own project at :\nhttps://github.com/Nkosinathi-Bonga-James-Mncube/Linkedin_post_automation\n-----------------------------------------------------')
      f.close()
      send_textfile=open("report.txt","r")
      linkedin_request(send_textfile.read())
      print('-> Post to linkedin')
      send_email(send_textfile)
      f.close()

def linkedin_request(send_textfile):
    linkedin_access_token=config('linkedin_access_token')
    id_urn=config('linkedin_id_urn')
    data = {
        "author": f'urn:li:person:{id_urn}',
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": f'{send_textfile}'
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    headers = {
      'X-Restli-Protocol-Version': '2.0.0',
      'Content-Type': 'application/json',
      'Authorization': f'Bearer {access_token}'
    }
    response2=requests.post('https://api.linkedin.com/v2/ugcPosts',json=data,headers=headers)
    pprint.pprint(response2.json())

def send_email(send_textfile):
  try:
    context = ssl.create_default_context()
    with smtplib.SMTP('smtp.gmail.com', 587) as server: 

      SUBJECT = "My Github monthly report"   
      TEXT = f'{send_textfile.read()}'
      message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

      server.ehlo()
      server.starttls(context=context)
      server.login(config('sender_email'), config('password'))
      server.sendmail(config('sender_email'), config('receiver_email'), message)
      print('-> Email sent')
  except Exception as e:
    print('Error:',e)
    
github_request()