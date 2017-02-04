import smtplib
import sys

# От кого:
fromaddr = 'NCM notify <ncm_notify@mail.ru>'

toaddr = 'Administrator <j-botman@mail.ru>'
subj = 'Notification from NCM'
msg_txt = 'Notice:\n\n ' + '\n\nBye!'  #

# Создаем письмо (заголовки и текст)
msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromaddr, toaddr, subj, msg_txt)
username = 'ncm_notify'
password = '123456Zz'
server = smtplib.SMTP('smtp.mail.ru:587')

# Лог работы с сервером (для отладки) 1 = True
server.set_debuglevel(0);

# Переводим соединение в защищенный режим (Transport Layer Security)
server.starttls()

# Проводим авторизацию:
server.login(username, password)

# Отправляем письмо:
server.sendmail(fromaddr, toaddr, msg)

# Закрываем соединение с сервером
server.quit()