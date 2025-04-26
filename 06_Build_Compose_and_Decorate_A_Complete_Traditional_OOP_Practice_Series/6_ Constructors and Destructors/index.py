class Logger:
    def __init__(self):
        print("📥 Logger object created!")

    def __del__(self):
        print("🗑️ Logger object destroyed!")

# Object create kar rahe hain
log = Logger()

# Ab object ko manually destroy kar dete hain
del log
