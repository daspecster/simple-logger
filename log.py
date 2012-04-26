from datetime import datetime

def event(msg):
    log_file = open('session_dropouts.log', 'a')
    log_file.write(datetime.now().isoformat() + " : " + msg + "\n")
    log_file.close()
