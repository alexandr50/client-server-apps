import platform
import subprocess
from chardet import detect

urls = ['yandex.ru', 'youtube.com']
code = '-n' if platform.system().lower() == 'windows' else '-c'

for i in urls:
    args = ['ping', code, '4', i]
    res = subprocess.Popen(args, stdout=subprocess.PIPE)
    for j in res.stdout:
        result = detect(j)
        print(result)
        j = j.decode(result['encoding']).encode('utf-8')
        print(j.decode('utf-8'))