> Please note: The script is for learning purposes and not for any malicious intent

> Please star project if you find it useful :)
# LinkedIn_automation
<p align="center">
<img height=200 src=https://user-images.githubusercontent.com/50704452/104107731-54d2c200-52c7-11eb-8b5a-b98d9c32ae6a.jpeg>
<img height=200 width=400 src=https://user-images.githubusercontent.com/50704452/104107772-b430d200-52c7-11eb-992b-61265adf89b1.png>
</p>

 - Posts a automated report each 1st of the month to my [LinkedIn Profile](https://www.linkedin.com/in/nbj-mncube/) using [Github Actions](https://docs.github.com/en/free-pro-team@latest/actions) (e.g If todays the 1 JAN 2021 it will post all public repos created in DEC 2020).
 - The report contains the following:
      - Name of project
      - Description of project
      - Link to project repository
 - Additional functionality:
     - [x] Sends me a email report when I successfully create at least one public repository in the previous month.
     - [x] Emails me if I haven't at least created one project for the previous month with a current list of public repos for the year.

 
----
# Packages
- Pandas: https://pypi.org/project/pandas/
- Request: https://pypi.org/project/requests/

# Actions used

 - GitHub Script: https://github.com/marketplace/actions/github-script
----
# Table of contents
 - [How it works](#how-it-works)
 - [Installation](#installation)
 - [Github action yaml](#github-action-yaml)
 - [Troubleshoot](#troubleshoot)

 # How it works
  ```python
 def github_request():
```
- `github_request()` function makes a GET request from Github API for the details of my repository and returns its response object.
```python
def create_dataframe(response):
```
- `create_dataframe()` then convert the response object into json object. To use the data effectively I converted the data into lists from json values( excluding any repos that are forked) to created a dataframe. 

```python
def display_repos(df):
```
 - `def display_repos()` function is tasked to:
   - Sorting the dataframe in ascending order according using json key "Created_at"(i.e list newest public repository at the top of dataframe)
   - Retrieves the current date then return the previous offset month value(e.g If todays the 1 JAN 2021 it will return 1 DEC 2020)
   - Find any repo that was created from the previous months(e.g Find all repos in DEC)

## On failure (i.e No new repositories have been created for the month)
```python
 each_repo = df.loc[df['Created_at'].dt.month==x.month].values
```
- If `each_repo.size` is 0 that means no public repository have been created for that specific month and `fail_msg()` function is called.
```python
def fail_msg(df,x):
```
- `fail_msg()` sends all infomation(personal message,current year repos etc.) to be written into `fail.txt` to be used by `send_email()` to send an email to myself.

<img height=400 width=600 src=https://user-images.githubusercontent.com/50704452/104844489-2f524380-58d9-11eb-929c-440088605977.png>

## On Success (i.e At least one repository has been created for the month)
```python
each_repo = df.loc[df['Created_at'].dt.month==x.month].values
```
- If `each_repo.size` is greater than 0 then: 

- All infomation(personal message,current months repos etc.) is written into `report.txt` to be used by `send_email()`
to send an email to myself.


<img height=400 width=600 src=https://user-images.githubusercontent.com/50704452/104844632-1007e600-58da-11eb-80ab-d9c5cf797858.png>

```python
   def linkedin_request(send_textfile):
```

- Lastely , `linkedin_request()` function sends a request to share a post on my LinkedIn profile using my `linkedin_access_token` and `id_urn`.

<img height=400 width=400 src=https://user-images.githubusercontent.com/50704452/104778499-1a18d000-5786-11eb-9eb5-f2518fe13286.png>

 # Installation
 ### Create a Github Personal access token
 - https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token
 ### Create a Linkedin token (Click on 'Create a app')
 > Please note: It's advise to use your own personal Linkedin profile as there are restrictions on newly created accounts.Please refer to the Troubleshoot section.  
 - https://www.linkedin.com/developers/
  ### Enter secrets
   > NB : If you plan to use your gmail account please use a app password instead of default password. To create app password :
   - https://support.google.com/accounts/answer/185833?hl=en

 - To enter secrets details for email click on settings
 <p>
<img width= 500 src=https://user-images.githubusercontent.com/50704452/104120644-07933680-5341-11eb-8072-a5f0faa38a42.png>
</p>




 - In the left sidebar, click Secrets.Add the following secrets :
      - `SEND_TO` (enter email address)
      - `SEND_FROM` (enter email address i.e sending it to myself)
      - `MAIL_PASSWORD` (enter password)
      - `API` (Github personal access token)
      - `LINKEDIN_ACCESS_TOKEN` (Linkedin access token)
      - `LINKEDIN_ID_URN` (Linkedin URN id)

<p>
<img width= 500 src=https://user-images.githubusercontent.com/50704452/104120647-1974d980-5341-11eb-9a63-1b2bfb32f7bb.png>
</p>


 # Github action yaml
 - Script should automatically run on the 1st of each month set by `cron`. `Checkout` action was used for testing purposes (testing on push event).
 ```yaml
 name: LinkedIn post automation

on: 
  schedule:
    - cron: "0 0 1 * *"
      
jobs:
  LinkedInActions:
    runs-on: ubuntu-latest
    steps:
     - name: Checkout repo
       uses: actions/checkout@v2
       
     - name: Setup python
       uses: actions/setup-python@v2
       with:
          python-version: 3.8

       
     - name : Run LinkedIn script
       env:
              SEND_TO: ${{secrets.SEND_TO}}
              SEND_FROM: ${{secrets.SEND_FROM}}
              MAIL_PASSWORD: ${{secrets.MAIL_PASSWORD}}
              API: ${{secrets.API}}
              LINKEDIN_ACCESS_TOKEN: ${{secrets.LINKEDIN_ACCESS_TOKEN}}
              LINKEDIN_ID_URN: ${{secrets.LINKEDIN_ID_URN}}
       run: |
          pip install -r requirements.txt
          python src/main.py  $SEND_TO $SEND_FROM $MAIL_PASSWORD $API $LINKEDIN_ACCESS_TOKEN $LINKEDIN_ID_URN
 ```
 # Troubleshoot
  ## Gmail
  > You experience any issue with sending a email try:
  - https://support.google.com/mail/answer/7126229?visit_id=637458707776330290-1687276339&rd=2#cantsignin
  
  ## LinkedIn
  > If you are having trouble creating a Linkedin company page to get a access token please read
  - https://technoogies.com/how-to-facts-about-linkedin-an-error-has-occurred-please-try-again-later/
