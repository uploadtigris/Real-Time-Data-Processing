# Install Packages
import subprocess
import sys

# Install APIs
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# yfinance
## https://github.com/ranaroussi/yfinance
install('yfinance')



