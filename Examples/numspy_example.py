from numspy import Way2sms
from credentials import username,password,mobile_number
w2s = Way2sms()

# login
w2s.login(username,password)

# send sms
w2s.send(mobile_number,'hello numspy testing')

# find details
w2s.details(8053356052)

# logout

w2s.logout()
