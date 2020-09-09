#!/usr/bin/env python
# coding: utf-8

# In[1]:


import smtplib


# In[2]:


from email.mime.multipart import MIMEMultipart


# In[3]:


from email.mime.text import MIMEText


# In[4]:


mail_content ='''
Application is Working Successfully.
'''


# In[5]:


sender_address = 'senderemail@gmail.com'
sender_pass = 'password'
receiver_address = 'receiveremail@gmail.com'


# In[6]:


message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Testing status'


# In[7]:


session = smtplib.SMTP('smtp.gmail.com',587)


# In[8]:


session.starttls()


# In[9]:


session.login(sender_address,sender_pass)


# In[10]:


message.attach(MIMEText(mail_content,'plain'))


# In[11]:


text = message.as_string()


# In[12]:


session.sendmail(sender_address,receiver_address,text)


# In[13]:


session.quit()


# In[14]:


print('Mail Sent')


# In[ ]:





# In[ ]: