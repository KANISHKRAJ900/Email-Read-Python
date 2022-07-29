import easyimap as e

user="fellon0312@gmail.com"
password="9931091882"

server=e.connect("imap.gmail.com",user,password)

server.listids()

email=server.mail(server.listids()[3])

#for title
print(email.title)
#for the sender’s email address
print(email.from_addr)
#for the main content of the email
print(email.body)
#for any type of attachment
print(email.attachments)

server.quit()