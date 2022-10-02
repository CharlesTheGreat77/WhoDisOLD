import smtplib, yagmail, smtplib

# CREDENTIALS
# Account Name 'Example@ex.com'
account = 'example@gmail.com'
# Account Password 'Password123'
password = 'Password123'

def Main():
        try:
                print('''
         _________________
        /            __   \                     
        |           (__)  |                             
        |                 |                         WhoDis
        | .-----.   .--.  |                    Spoofer/Spammer        | |     |  /    \ |                             
        | '-----'  \    / |                             
        |           |  |  |              * Educational Purposes Only          
        | LI LI LI  |  |  |              do not use this tool
        | LI LI LI  |  |  |oO            for illegal/annoying
        | LI LI LI  |  |  |`oO           purposes... noob.
        | LI LI LI  |  |  |  oO                 
        |           |  |  |   oO        - DoobTheGoober
        | .------. /    \ |   Oo            version 1.0
        | |      | \    / |   Oo
        | '------'  '-oO  |   oO
        |          .---Oo |   Oo
        |          ||  ||`Oo  oO
        |          |'--'| | OoO
        |          '----' |
        \_________________/
                                                                      ''')

# give a user the option to use an email spoofer, or text spoofer.
                print('''
                [!] Choose an Option:
                        (1) Text Spoofer
                        (2) Email Spoofer
        ''')
                poison = input('text@email: ')
                poison = int(poison)
                # set poison as integer
                if poison == 1:
                        Text()
                else:
                        Email()


        except Exception as e:
                print(str(e))

# text function used or sms spam/spoof
def Text():
        try:
                print('''
                [*] Enter target number + targets_sms gateway
                                [Number]   [SMS gateway]
                        ex: 7025551234@txt.att.net
                        
                        SMS GATEWAYS
                        Sprint @messaging.sprintpcs.com
                        AT&T    @txt.att.net
                        Tmobl   @tmomail.com
                        Verizon @vtext.com

                [+] To obtain a targets sms gateway, go to
                freecarrierlookup.com and type in the target
                number. The results will give you the info
                exactly how it should be formatted (copy & paste)
                
                ''')
                # sleep for 1 second
                time.sleep(1)
        
                # specify target
                target = input('number@gateway: ')
        
                # compose message
                print('[*] Compose Your Message')
                message = input('text@message: ')
        
                # amount to send
                print('[*] Amount to Send')
                amount = input('send@amount: ')
                amount = int(amount)
                
                # email provider
                provider = 'smtp.gmail.com'
                # port number
                port = 587

                # establish connection to server with creds
                server = smtplib.SMTP(provider, port)
                server.starttls()
                server.login(account, password)


                # create variable sent and = to 0
                sent = 0

                # create a for loop to send mail to target from 0, amount.
                for x in range(0, amount):
                        
                        # use sendmail to send the message to target
                        server.sendmail(account, target, message)

                        # increment + 1 for every message sent                        sent +=1

                        # show messages being sent
                        print('[$] Message Sent | Sent ('+str(sent)+')')
                print('[!] ALL Messages Have Been Sent | (' +str(sent)+')')
                time.sleep(3)
                Main()
        except Exception as e:
                print(str(e))



# spoof email function
def Email():
        try:
                # specify target email
                print('[*] Specify target Email Address')
                toaddy = input('address@email: ')

                # specify fake name
                print('[*] Enter A Spoofed Name')
                spoofed_name = input('spoofed@name: ')

                # Subject of email
                print('[*] Compose Subject of Email')
                subject = input('compose@subject: ')

                # Compose body
                print('[*] Compose Body of Email')
                body = input('compose@body: ')

                # amount to send
                print('[*] Amount to Send')
                amount = input('send@amount: ')
                # make amount an integer instead of string
                amount = int(amount)

                # establish connection
                yag = yagmail.SMTP({account:spoofed_name}, password)

                # create sent variable
                sent = 0 
                
                # send message in for loop
                for x in range(0, amount):
                        yag.send(toaddy, subject, body)
                        sent += 1
                        print('[$] Email has Been Sent | Sent (' + str(sent)+ ')')
                print('[!] ALL Emails have been Sent Successfully..')
                time.sleep(3)
                Main()
        except Exception as e:
                print(str(e))

if __name__=='__main__':
        Main()
