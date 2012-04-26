from datetime import datetime

def event():
    log_file = open('session_dropouts.log', 'a')
    log_file.write(datetime.now().isoformat() + "\n")
    log_file.close()