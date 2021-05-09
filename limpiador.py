def clearScreen():
    """
    limpia la pantalla independientemente del sistema operativo
    """
    import os
    os.system(['clear','cls'][os.name == 'nt'])