Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.8.5/python-3.8.5-amd64.exe' -OutFile 'python-3.8.5-amd64.exe'
Start-Process -FilePath ".\python-3.8.5-amd64.exe" -Wait -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1 Include_test=0"
Invoke-WebRequest -Uri 'https://github.com/git-for-windows/git/releases/download/v2.28.0.windows.1/Git-2.28.0-64-bit.exe' -OutFile 'Git-2.28.0-64-bit.exe'
Start-Process -FilePath ".\Git-2.28.0-64-bit.exe" -Wait -ArgumentList '"/VERYSILENT" "/NORESTART" "/NOCANCEL" "/SP-" "/CLOSEAPPLICATIONS" "/RESTARTAPPLICATIONS" /LOADINF="GITLOADFILE" /SAVEINF="savefile" /COMPONENTS="icons,ext\reg\shellhere,assoc,assoc_sh"'
$env:Path = [System.Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [System.Environment]::GetEnvironmentVariable('Path','User')
python -m pip install --user --upgrade pip
python -m pip install --user pyenv-win

git clone https://github.com/naka345/madplot.git
cd madplot
python -m pyenv install 3.4.10
python -m pyenv global 3.4.10
python -m pip install -r requirement.txt
python -m setup.py py2exe
dir
