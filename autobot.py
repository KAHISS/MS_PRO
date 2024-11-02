import pyautogui
from keyboard import write
from time import sleep
from datetime import datetime
import locale


class SendMessage:
    def __init__(self):
        pyautogui.PAUSE = 2
        pyautogui.FAILSAFE = True

    @staticmethod
    def open_whatsapp():
        pyautogui.hotkey('win', 's')
        pyautogui.write('whatsapp')
        pyautogui.press('enter')

    @staticmethod
    def pause(file):
        while True:
            abriu = pyautogui.locateCenterOnScreen(file)
            if abriu:
                break
            else:
                continue

    @staticmethod
    def whatsapp(contact, type_message, message=''):
        salutation = ''
        locale.setlocale(locale.LC_TIME, 'pt_BR')
        if type_message != 3:
            for c in contact:
                pyautogui.hotkey('ctrl', 'f')
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.press('backspace')
                if '(' in c[1]:
                    write(c[1].split(')')[0].replace('(', ''))
                else:
                    write(c[1])
                sleep(1.5)
                pyautogui.press('down')
                pyautogui.press('enter')
                pyautogui.click(x=946, y=988)

                dayWeek = datetime.strptime(c[6], '%d/%m/%Y').strftime('%A')
                monthYear = datetime.strptime(c[6], '%d/%m/%Y').strftime('%B')
                if float(datetime.now().strftime('%H:%M').replace(':', '.')) < 12.00:
                    salutation = 'Bom dia'
                elif 12.00 <= float(datetime.now().strftime('%H:%M').replace(':', '.')) < 18.00:
                    salutation = 'Boa tarde'
                else:
                    salutation = 'Boa noite'
                sleep(1.5)
                if type_message == 1:
                    if '(' in c[1]:
                        nameForSend = c[1].split(")")[0].replace("(", "").title()
                        nameForSend = nameForSend.split(' ')[0].title()
                        nameScheduled = c[1].split(")")[1].replace(" ", "", 1).title()
                        write(f'{salutation} {nameForSend}, posso confirmar o horário para {nameScheduled.replace("E", "e").replace("Você", "você")} amanhã às {c[3]}?')
                    else:
                        write(f'{salutation} {c[1].title().split(" ")[0]}, posso confirmar o seu horário amanhã às {c[3]}?')
                elif type_message == 2:
                    if '(' in c[1]:
                        nameForSend = c[1].split(")")[0].replace("(", "").title()
                        nameForSend = nameForSend.split(' ')[0].title()
                        nameScheduled = c[1].split(")")[1].replace(" ", "", 1).title()
                        write(f'Oi, {nameForSend}. este é o próximo agendamento para {nameScheduled.replace("E", "e").replace("Você", "você")}.')
                        pyautogui.hotkey('shift', 'enter')
                        write(f'*{dayWeek.title()} dia {c[6][0:2]} de {monthYear} às {c[3]}*')
                    else:
                        write(f'*{dayWeek.title()} dia {c[6][0:2]} de {monthYear} às {c[3]}*')
                pyautogui.press('return')
                sleep(1)
        else:
            for c in contact:
                pyautogui.hotkey('ctrl', 'f')
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.press('backspace')
                if '(' in c[1]:
                    write(c[1].split(")")[0].replace("(", "").title())
                else:
                    write(c[1])
                sleep(1.5)
                pyautogui.press('down')
                pyautogui.press('enter')
                pyautogui.click(x=946, y=988)
                sleep(1.5)
                if '(' in c[1]:
                    nameFormated = c[1].split(")")[0].replace("(", "").title()
                    nameFormated = nameFormated.split(' ')[0].title()
                    write(message.replace('()', f'{nameFormated}'))
                else:
                    write(message.replace('()', f'{c[1].title().split(" ")[0]}'))
                pyautogui.press('return')
                sleep(1)
