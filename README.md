# On-Startup-Watchdog 🕵️🐕

Ignorando a temática de cachorro, esse projeto é um template de watchdog que roda assim que o windows inicializa.

## Setup

1. rodar `pyinstaller --add-data 'cachorro.jpg;.' --noconsole --onedir --icon=cachorro.jpg main.py` no terminal da sua venv
   * opcionalmente renomear o main.exe para cachorro.exe, pra ficar temático

2. criar um atalho do executável
3. colocar o atalho no caminho `C:\Users\<usr>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`


## Uso

Se você não alterar nenhum valor no programa, ele criará 2 pastas no Desktop.

Clicando com o botão direito no ícone que aparece na *system tray* você pode usar a opção 'cachorro' para criar um .txt genêrico, o mesmo vai ser criado na pasta 1 e depois movido pra pasta 2.

Todas ações de movimentação são logadas no arquivo **autodog.txt**.

Para fechar o cachorro.exe é só mandar ele dormir.

## O que mudar

Se você quer só usar a funcionalidade de ler uma pasta e jogar os arquivos dela em outra, mude os paths dentro do main.py.

Para outras funcionalidades você pode só reaproveitar a estrutura das funções, eu acho.

![alt text](https://github.com/nerdoswmp/OnStartupWatchdog/blob/master/cachorro.jpg)
