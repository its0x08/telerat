try:
    from pyscreenshot import grab
except ImportError as e:
    print str(e)

def screenshot():
    try:
        im=grab()
        im.save('scr.png')
    except Exception:
        pass


screenshot()
