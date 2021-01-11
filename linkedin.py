import sys
import requests
from decouple import config
import pandas as pd
import pprint
from datetime import date

def github_request():
    for x in sys.argv[1:]: # for arguments for secrets
      print(x)
    
    # Make api request with Github credential token
    headers = {'Authorization': 'token ' + config('api')}
    response = requests.get('https://api.github.com/users/Nkosinathi-Bonga-James-Mncube/repos',headers=headers)
    # pprint.pprint(response.json()[0]) # testing purposes
    # print('-----------------------------------------')
    # pprint.pprint(response.json()[1])
    
    # Sort json value from key in API get request
    project_name = [k['full_name'] for k in response.json() if not k['fork'] == True]
    project_created = [k['created_at'][:10] for k in response.json() if not k['fork'] == True]
    project_id = [k['id'] for k in response.json() if not k['fork'] == True]
    project_url = [k['html_url'] for k in response.json() if not k['fork'] == True]
    
    # Create a dictionary from json values 
    data_df = {
                'Project_name':project_name,
                'Created_at':project_created,
                'Id':project_id,
                'html_url':project_url
    }
    # Create dataframe based on dictionary
    df=pd.DataFrame(data_df,columns=['Project_name','Created_at','Id','html_url'])
    df.sort_values(by=['Created_at'],inplace=True,ascending=False)
    print(df)
    # print(df[['Project_name','Id']])
github_request()