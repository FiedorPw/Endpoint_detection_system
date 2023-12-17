'''
GEN.LOG.2 Aplikacja posiada dwa tryby działania:
GEN.LOG.2.1 Odbierane wiadomości ze zdarzeniami i wypisywanie ich w trybie ciągłym na CLI oraz
zapisywane do plikowej bazy danych sqlite
GEN.LOG.2.2 Odczytywanie historii zdarzeń z plikowej bazy danych sqlite z możliwością
filtrowania
'''
import threading
import click
import os
from click_shell import shell
from nbconvert import export

import networkServer

#variables to signal to network serwer what to do with the logs
print_to_cli = 0
save_to_db = 0



@shell(prompt='ZDZ> ', intro='Starting my app...')
def my_app():
    pass


@my_app.command()
@click.option('--cli','-c', 'cli_argument', is_flag=True,help='print logs to cli as they come from network client',show_default=True)
@click.option('--db','-d', 'db_argument',is_flag=True,help='forward recived logs to database',show_default=True)
def recive_logs(cli_argument,db_argument):

    # odpalenie serwera flask w innym wątku aby mogły działać obok cli
    thread = threading.Thread(target=networkServer.run())
    thread.start()
    # thread.join()
    # while True:
    #     print(networkServer.test_string)


    print_to_cli = cli_argument
    save_to_db = db_argument
    print(print_to_cli)
    print(save_to_db)
    networkServer.printuj()
    networkServer.run()
    print("poszło do serwera")
    printuj()
    # if print_to_cli:
    #     networkServer.print_logs()
    # if

@my_app.command()
def print_response():
    while True:
        print(networkServer.test_string)

if __name__ == '__main__':
    my_app()
