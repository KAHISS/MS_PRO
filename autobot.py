from playwright.sync_api import sync_playwright
from time import sleep
from datetime import datetime
import locale
import os
from playwright.sync_api import sync_playwright

os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "0"
class SendMessage:
    def __init__(self):
        # Configuração de locale para datas em PT-BR
        try:
            locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
        except locale.Error:
            try:
                locale.setlocale(locale.LC_TIME, 'pt_BR')
            except locale.Error:
                print("Aviso: Locale pt_BR não encontrado. Datas podem ficar em inglês.")

        self.browser_args = [
            "--no-sandbox",
            "--disable-infobars",
            "--disable-dev-shm-usage",
            "--disable-blink-features=AutomationControlled",
            "--start-maximized",
        ]

    def send_messages(self, contact_list, type_message, custom_message=''):
        """
        contact_list: Lista de contatos no formato esperado (c[1]=nome, c[3]=hora, c[6]=data)
        type_message: 1 (Confirmação), 2 (Próximo agendamento), 3 (Personalizado)
        """
        
        # Cria um diretório para salvar a sessão do WhatsApp (não precisa escanear QR code toda vez)
        user_data_dir = os.path.join(os.getcwd(), "whatsapp_session")

        with sync_playwright() as p:
            # Inicia o navegador com contexto persistente (salva o login)
            print("Abrindo navegador...")
            context = p.chromium.launch_persistent_context(
                user_data_dir,
                channel="chrome",
                headless=False,
                args=self.browser_args,
                viewport=None
            )
            
            page = context.pages[0] if context.pages else context.new_page()
            
            # Abre o WhatsApp Web
            print("Acessando WhatsApp Web...")
            page.goto("https://web.whatsapp.com/")

            # Espera a lista de conversas carregar (sinal que logou)
            # O seletor abaixo procura pelo painel lateral de conversas
            try:
                page.wait_for_selector("div[id='pane-side']", timeout=60000)
                print("WhatsApp carregado com sucesso!")
            except:
                print("Tempo limite excedido. Por favor, escaneie o QR Code se for a primeira vez.")
                # Se for a primeira vez, damos um tempo extra para escanear
                sleep(15) 

            for c in contact_list:
                try:
                    # Lógica de processamento do nome (Mantida do seu código original)
                    raw_name = c[1]
                    phone_or_search_key = ""
                    
                    if '(' in raw_name:
                        phone_or_search_key = raw_name.split(')')[0].replace('(', '')
                    else:
                        phone_or_search_key = raw_name

                    print(f"Buscando contato: {phone_or_search_key}")

                    # 1. Clicar na caixa de busca e limpar
                    # O seletor do campo de busca (pode mudar com updates do WA, mas esse é o padrão atual)
                    search_box = page.wait_for_selector("div[contenteditable='true'][data-tab='3']")
                    search_box.click()
                    search_box.fill(phone_or_search_key)
                    sleep(1.5) # Espera o WhatsApp filtrar

                    # 2. Pressionar Enter para abrir a conversa (seleciona o primeiro resultado)
                    page.keyboard.press("Enter")
                    
                    # Espera a área da conversa abrir
                    sleep(1) # Pequena pausa para garantir renderização da conversa

                    # 3. Preparar a Saudação e Data (Lógica Original)
                    dayWeek = datetime.strptime(c[6], '%d/%m/%Y').strftime('%A')
                    monthYear = datetime.strptime(c[6], '%d/%m/%Y').strftime('%B')
                    
                    hora_atual = float(datetime.now().strftime('%H:%M').replace(':', '.'))
                    if hora_atual < 12.00:
                        salutation = 'Bom dia'
                    elif 12.00 <= hora_atual < 18.00:
                        salutation = 'Boa tarde'
                    else:
                        salutation = 'Boa noite'

                    # 4. Construir a Mensagem (Lógica Original adaptada para variável 'final_message')
                    final_message = ""
                    
                    if type_message == 1:
                        if '(' in raw_name:
                            nameForSend = raw_name.split(")")[0].replace("(", "").title().split(' ')[0]
                            nameScheduled = raw_name.split(")")[1].replace(" ", "", 1).title()
                            final_message = f'{salutation} {nameForSend}, posso confirmar o horário para {nameScheduled.replace("E", "e").replace("Você", "você")} amanhã às {c[3]}?'
                        else:
                            final_message = f'{salutation} {raw_name.title().split(" ")[0]}, posso confirmar o seu horário amanhã às {c[3]}?'
                    
                    elif type_message == 2:
                        if '(' in raw_name:
                            nameForSend = raw_name.split(")")[0].replace("(", "").title().split(' ')[0]
                            nameScheduled = raw_name.split(")")[1].replace(" ", "", 1).title()
                            msg_part1 = f'Oi, {nameForSend}. este é o próximo agendamento para {nameScheduled.replace("E", "e").replace("Você", "você")}.'
                            msg_part2 = f'*{dayWeek.title()} dia {c[6][0:2]} de {monthYear} às {c[3]}*'
                            # Para enviar em duas linhas com Shift+Enter
                            final_message = f"{msg_part1}\n{msg_part2}" 
                        else:
                            final_message = f'*{dayWeek.title()} dia {c[6][0:2]} de {monthYear} às {c[3]}*'

                    elif type_message == 3:
                        if '(' in raw_name:
                            nameFormated = raw_name.split(")")[0].replace("(", "").title().split(' ')[0]
                            final_message = custom_message.replace('()', f'{nameFormated}')
                        else:
                            final_message = custom_message.replace('()', f'{raw_name.title().split(" ")[0]}')

                    # 5. Enviar a mensagem
                    # Campo de texto da mensagem
                    message_box = page.wait_for_selector("div[contenteditable='true'][data-tab='10']")
                    
                    # O Playwright lida com quebras de linha (\n) automaticamente se usar type ou fill
                    # Se for tipo 2 (que tinha Shift+Enter), o \n resolve no Playwright.
                    message_box.fill(final_message)
                    sleep(0.5)
                    page.keyboard.press("Enter")
                    
                    print(f"Mensagem enviada para {phone_or_search_key}")
                    sleep(3) # Intervalo de segurança entre contatos

                except Exception as e:
                    print(f"Erro ao enviar para {c[1]}: {e}")
                    # Limpa a busca para tentar o próximo sem travar
                    try:
                        page.keyboard.press("Escape")
                        page.keyboard.press("Escape")
                    except:
                        pass

            print("Processo finalizado.")
            # context.close() # Pode manter aberto se quiser ver o resultado

# --- Exemplo de uso para teste ---
if __name__ == "__main__":
    bot = SendMessage()
    
    # Simulando os dados que viriam do seu sistema (c[1]=nome, c[3]=hora, c[6]=data)
    # Exemplo: id, nome, email, hora, id, id, data
    mock_contacts = [
        (0, "Salvar", 0, "14:00", 0, 0, "18/02/2026"),
        (0, "Carlos", 0, "15:30", 0, 0, "18/02/2026")
    ]

    # Teste Tipo 1
    bot.send_messages(mock_contacts, type_message=1)