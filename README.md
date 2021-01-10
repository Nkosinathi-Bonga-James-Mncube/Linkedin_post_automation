# LinkedIn_automation
<p align="center">
<img height=200 src=https://user-images.githubusercontent.com/50704452/104107731-54d2c200-52c7-11eb-8b5a-b98d9c32ae6a.jpeg>
<img height=200 width=400 src=https://user-images.githubusercontent.com/50704452/104107772-b430d200-52c7-11eb-992b-61265adf89b1.png>
</p>

 - Built a automated task to inform my network what I'm working on LinkedIn.
 - Posts a automated report each month to my [LinkedIn Profile](https://www.linkedin.com/in/nbj-mncube/) using [Github Actions](https://docs.github.com/en/free-pro-team@latest/actions).
 - Additional functionality:
     - [ ] Keeps track of already posted project in .txt file
     - [ ] Emails me if I haven't at least created one project for the month
     - [ ] Attached record of projects for the year

 
----
# Actions used
 - Send email : https://github.com/marketplace/actions/send-email
----
# Table of contents
 - [How it works](#how-it-works)
 - [Installation](#installation)
 - [How to use github action](#how-to-use-github-actions)
 - [Troubleshoot](#troubleshoot)

 # How it works
 (using it github actions)
 - An email is send using `send email` action if no new repo repro has added for the month.
 ## What is Github Actions?
 - Explain artifacts
 - Explain checkout
 - Explain jobs
 - Explain
 - Research :
    - https://github.com/marketplace/actions/github-api-request
    - https://github.com/actions/checkout
    - https://waylonwalker.com/four-github-actions-website
    - https://github.com/actions/download-artifact
    - https://github.com/nektos/act 

 ## What is Yaml?
 - 
 # Installation
 ### Enter email details
 - To enter secrets details for email click on settings
 <p>
<img width= 500 src=https://user-images.githubusercontent.com/50704452/104120644-07933680-5341-11eb-8072-a5f0faa38a42.png>
</p>

 - In the left sidebar, click Secrets.Add the `MAIL_USERNAME`, `MAIL_PASSWORD` , `SEND_TO`,`SEND_FROM` values

<p>
<img width= 500 src=https://user-images.githubusercontent.com/50704452/104120647-1974d980-5341-11eb-9a63-1b2bfb32f7bb.png>
</p>

 # How to use github actions
 # Troubleshoot
  - You experience any issue with sending a email try:
  https://support.google.com/mail/answer/7126229?visit_id=637458707776330290-1687276339&rd=2#cantsignin