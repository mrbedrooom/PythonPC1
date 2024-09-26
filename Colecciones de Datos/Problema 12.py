# MIME de tu archivo

mime_types={
    '.gif' : 'image/gif',
    '.jpg' : 'image/jpeg',
    '.jpeg' : 'image/jpeg',
    '.png' : 'image/png',   
    '.pdf' : 'application/pdf',
    '.txt' : 'text/plain',
    '.zip' : 'application/zip'
    }

archivo= input('Escribe el nombre de tu archivo: ')

extension= '.' + archivo.split(".")[-1].lower() if '.' in archivo else ''

MIME= mime_types.get(extension, 'application/octect-stream')
print(f"Tipo de MIME detectado: {MIME}")