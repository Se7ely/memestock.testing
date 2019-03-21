from GeneralUtilities.BrowserFunctions import BrowserLoad
from GeneralUtilities.BrowserFunctions import BrowserClose

Loader = BrowserLoad()
fd=Loader.FireFoxLoad('https://www.reddit.com')
cd=Loader.ChromeLoad('https://www.reddit.com')

Closerf=BrowserClose(fd)
Closerc=BrowserClose(cd)

Closerc.BClose()
Closerf.BClose()

