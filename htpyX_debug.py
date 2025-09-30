class Debug:
    enabled = True
    
    @classmethod
    def log(cls, *args):
        if cls.enabled:
            print("[htpyX]", *args)
    
    @classmethod  
    def error(cls, msg):
        if cls.enabled:
            print(f"[htpyX ERROR] {msg}")
        raise Exception(msg)

# Shortcut
debug = Debug.log