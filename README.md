> Please start project if you find it useful :)
# LinkedIn_automation
<p align="center">
<img height=200 src=https://user-images.githubusercontent.com/50704452/104107731-54d2c200-52c7-11eb-8b5a-b98d9c32ae6a.jpeg>
<img height=200 width=400 src=https://user-images.githubusercontent.com/50704452/104107772-b430d200-52c7-11eb-992b-61265adf89b1.png>
</p>

 - Posts a automated report each 1st of the month to my [LinkedIn Profile](https://www.linkedin.com/in/nbj-mncube/) using [Github Actions](https://docs.github.com/en/free-pro-team@latest/actions) (e.g If todays the 1 FEB 2021 it will post all public repos from JAN 2021).
 - The report contains the following:
      - Name of project
      - Description of project
      - Link to project repository
 - Additional functionality:
     - [x] Send me a email report copy of successfully creating at least one public repository for previous month
     - [x] Emails me if I haven't at least created one project for the previous month with a current list of public repos for the year.

 
----
# Packages
- Pandas: https://pypi.org/project/pandas/
- Request: https://pypi.org/project/requests/

# Actions used
 - Send email : https://github.com/marketplace/actions/send-email
 - GitHub Script: https://github.com/marketplace/actions/github-script
----
# Table of contents
 - [How it works](#how-it-works)
 - [Installation](#installation)
 - [How to use github action](#how-to-use-github-actions)
 - [Troubleshoot](#troubleshoot)

 # How it works
  ```python
 def github_request():
```
- The `github_request()` function makes a GET request from Github API for the details of my repository and returns its response object.
```python
def create_dataframe(response):
```
- `create_dataframe()` then convert the response object into json object. To use the data effectively I converted the data into lists from json values( excluding any repos that are forked) to created a dataframe. 



 - `def display_repos()` function is tasked to:
 - Sorting the dataframe in ascending order according to json key "Create_at"(i.e list newest public repository at the top of dataframe)
```python
   df.sort_values(by=['Created_at'],inplace=True,ascending=False)
```
   - Retrieves the current date then return the previous month value. (e.g Todays the 1 FEB 2021 it will return 1 JAN 2021)
```python
   x=datetime.datetime.now()+ pd.DateOffset(months=-1)
```
- The `df.loc` attribute is used to find any repo that was created from the previous months. Then using `.values` to return numpy array . (i.e. Find all repos in JAN)
```python
   each_repo = df.loc[df['Created_at'].dt.month==x.month].values
```
## On failure (i.e No new repositories have been created for the month)
- If `each_repo.size` is 0 that means no public repository have been created for that specific month and `fail_msg()` function is called.
- Creates a numpy array of the current years repositories instead of month for `each_repo`
```python
 each_repo = df.loc[df['Created_at'].dt.year==y.year].values
```
- Afterwards all infomation(Personal message,Current year repos etc.) is written into `fail.txt` to be used by `send_email()` to be sent in email to myself.

<img height=400 width=800 src=https://user-images.githubusercontent.com/50704452/104768621-a7542880-5776-11eb-8fdc-47b14992fc46.png>

## On Success (i.e At least one repository has been created for the month)
- If `each_repo.size` is greater than 0 for that specific month the `display_repos()` 
function is called.
```python
def display_repos(df):
```
- Afterwards all infomation(Personal message,Current months repos etc.) is written into `report.txt` to be used by `send_email()`
to be sent in email to myself.
<img height=400 width=800 src=https://user-images.githubusercontent.com/50704452/104768706-c2269d00-5776-11eb-8bb9-a4481be5e06c.png>

```python
   def linkedin_request(send_textfile):
```

- Lastely , `linkedin_request()` function is used to share a post on my LinkedIn profile using my `linkedin_access_token` and `id_urn`
   > `linkedin_access_token` :

   >`id_urn` : Uniqu




 
- `linkedin_request()`

 # Installation
 ### Create a Github Personal access token
 - https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token
 ### Create a Linkedin token (Clicked on 'Create a app')
 > Please note: It's advise to use your own personal Linkedin profile as there are restrictions on newly created accounts.Please refer to the Troubleshoot section.  
 - https://www.linkedin.com/developers/
  ### Enter email details
   > NB : If you plan to use your gmail account please use a app password instead of default password. To create app password :
   - https://support.google.com/accounts/answer/185833?hl=en

 - To enter secrets details for email click on settings
 <p>
<img width= 500 src=https://user-images.githubusercontent.com/50704452/104120644-07933680-5341-11eb-8072-a5f0faa38a42.png>
</p>




 - In the left sidebar, click Secrets.Add the following secrets :
      - `MAIL_USERNAME` (enter email address)
      - `MAIL_PASSWORD` (enter password)
      - `SEND_TO` (recieving email address)
      - `SEND_FROM` (different email address it sending from)
      - `GITHUB_ACCESS_TOKEN` (Github personal access token)
      - `LINKEDIN_ACCESS_TOKEN` (Linkedin access token)
      - `LINKEDIN_ID_URN` (Linkedin URN id)

<p>
<img width= 500 src=https://user-images.githubusercontent.com/50704452/104120647-1974d980-5341-11eb-9a63-1b2bfb32f7bb.png>
</p>


 # How to use github actions
 # Troubleshoot
  > You experience any issue with sending a email try:
  - https://support.google.com/mail/answer/7126229?visit_id=637458707776330290-1687276339&rd=2#cantsignin
  > If you are having trouble creating a Linkedin company page to get a access token please read
  - https://technoogies.com/how-to-facts-about-linkedin-an-error-has-occurred-please-try-again-later/
