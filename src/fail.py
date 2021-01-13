import  datetime

def fail_msg(df):
    txt_file = open('src/ascii.txt','r')
    print(txt_file.read())
    print('No new project :( Please contribute more and make public!')
    x=datetime.datetime.now()
    print(f'\nPast record for {x.year}:\n')
    each_repo = df.loc[df['Created_at'].dt.year==x.year].values
    for k in each_repo:
      print(f'{k[1]} {k[3]}')