from BrowserFunctions.BrowserLoad import BrowserLoad
from BrowserFunctions.BrowserClose import BrowserClose
Loader = BrowserLoad()
fd=Loader.FireFoxLoad('https://github.com')
cd=Loader.ChromeLoad('https://github.com')

Closerf=BrowserClose(fd)
Closerc=BrowserClose(cd)

Closerc.BClose()
Closerf.BClose()

