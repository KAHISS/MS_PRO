# sql comands general==========================================
searchAll = 'SELECT * FROM {}'
searchAllForSale = 'SELECT ID, fornecedor, marca, tipo, quantidade, medida, valor_de_compra, valor_de_venda, validade, cliente, método_de_pagamento, {}, modificação FROM {}'
deleteInformation = 'DELETE FROM {} WHERE ID = {}'

# style of tables general ===============================================
styleTableInformationsTreeview = [
    ('BACKGROUND', (0, 1), (-1, 1), '#e8d499'),
    ('BACKGROUND', (0, 2), (-1, -1), '#ffffff'),
    ('TEXTCOLOR', (0, 1), (-1, -1), '#000000'),
    ('FONTSIZE', (0, 1), (-1, 1), 12),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('BOX', (0, 1), (-1, -1), 0.25, '#e8d499'),
    ('INNERGRID', (0, 1), (-1, -1), 0.25, '#e8d499')
]
styleTableInformationsComplementary = [
    ('BACKGROUND', (0, 1), (-1, 1), '#b59b50'),
    ('BACKGROUND', (0, 2), (-1, -1), '#ffffff'),
    ('TEXTCOLOR', (0, 1), (-1, 1), '#000000'),
    ('FONTSIZE', (0, 1), (-1, 1), 12),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('BOX', (0, 1), (-1, -1), 0.25, '#b59b50'),
    ('INNERGRID', (0, 1), (-1, -1), 0.25, '#b59b50')]

# sql comands for scheduling ===================================
registerScheduling = (
    'INSERT INTO Agenda (cliente, serviço, horário, valor, método_de_pagamento, data, profissional, agendamento, código_de_serviço)'
    'VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'
)
searchSchedule = '''SELECT * 
                  FROM Agenda
                  WHERE {} LIKE "%{}%"
                  and serviço LIKE "%{}%"
                  and profissional LIKE "%{}%"
                  and valor LIKE "%{}%"
                  and método_de_pagamento LIKE "%{}%"
                  and data LIKE "%{}%"
                  and horário LIKE "%{}%"
                  and agendamento LIKE "%{}%"
                  and código_de_serviço LIKE "%{}%" ORDER BY {} ASC'''

searchScheduleDate = '''SELECT * 
                  FROM Agenda
                  WHERE {} LIKE "%{}%"
                  and serviço LIKE "%{}%"
                  and profissional LIKE "%{}%"
                  and valor LIKE "%{}%"
                  and método_de_pagamento LIKE "%{}%"
                  and data LIKE "%{}%"
                  and horário LIKE "%{}%"
                  and agendamento LIKE "%{}%"
                  and código_de_serviço LIKE "%{}%" ORDER BY SUBSTR(data, 7, 4) || '-' || SUBSTR(data, 4, 2) || '-' || SUBSTR(data, 1, 2)'''

updateSchedule = '''UPDATE Agenda
                      SET cliente = "{}",
                          serviço = "{}",
                          horário = "{}",         
                          valor = "{}",
                          método_de_pagamento = "{}",
                          data = "{}",
                          profissional = "{}",
                          agendamento = "{}",
                          código_de_serviço = "{}"
                      WHERE ID = {}'''

# tables for schedule informations =================================
tableWithInformationsScheduleTreeview1 = [['', '', '', '', ''], ['    ID    ', '    Cliente    ', '    Serviço    ', '    Profissional   ', '    Valor    ']]
tableWithInformationsScheduleTreeview2 = [['', '', '', '', ''], ['M/Pagamento', 'Data', 'Hrário', 'Agendamento', 'C/Serviço']]
tableWithInformationsComplementarySchedule = [['', '', '', '', '', '', ''], ['Total de clientes', 'T/Cartão', 'T/Dinheiro', 'T/Tranferência', 'T/Nota', 'T/Não pago', 'T/Recebido']]

# sql comands for clients informations ==============================
registerClient = (
    'INSERT INTO Clientes (nome, nascimento, CPF, filhos, telefone, cliente_desde, endereço, CEP, bairro, cidade, estado, foto, observação)'
    'VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'
)
searchClient = '''SELECT * 
                  FROM Clientes
                  WHERE {} LIKE "%{}%"
                  and nascimento LIKE "%{}%"
                  and CPF LIKE "%{}%"
                  and filhos LIKE "%{}%"
                  and telefone LIKE "%{}%"
                  and cliente_desde LIKE "%{}%"
                  and endereço LIKE "%{}%"
                  and CEP LIKE "%{}%"
                  and bairro LIKE "%{}%"
                  and cidade LIKE "%{}%"
                  and estado LIKE "%{}%"
                  and observação LIKE "%{}%" ORDER BY {} ASC'''
updateClient = '''UPDATE Clientes
                      SET nome = "{}",
                          nascimento = "{}",
                          CPF = "{}",
                          filhos = "{}",
                          telefone = "{}",
                          cliente_desde = "{}",
                          endereço = "{}",
                          CEP = "{}",
                          bairro = "{}",
                          cidade = "{}",
                          estado = "{}",
                          foto = "{}",
                          observação = "{}"
                      WHERE ID = {}'''

# tables for client informations =================================
tableWithInformationsClientTreeview1 = [['', '', '', '', ''], ['    ID    ', '    Nome    ', '    Nascimento    ', '    CPF    ', ' Filhos ', 'Telefone']]
tableWithInformationsClientTreeview2 = [['', '', '', '', ''], ['C/Desde ', ' Endereço ', ' CEP ', ' Bairro ', ' Cidade ', ' Estado ']]
tableWithInformationsComplementaryClient = [['', '', '', ''], ['Total de clientes', 'T/Pais', 'T/Sem filhos', 'T/Moradores', 'T/Visitantes']]

# sql comands for profissional informations ==============================
registerProfessional = (
    'INSERT INTO Profissionais (nome, CPF, admissão, e_mail, telefone, emergência, endereço, CEP, bairro, cidade, estado, foto, observação)'
    'VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'
)
searchProfessional = '''SELECT * 
                  FROM Profissionais
                  WHERE {} LIKE "%{}%"
                  and CPF LIKE "%{}%"
                  and admissão LIKE "%{}%"
                  and e_mail LIKE "%{}%"
                  and telefone LIKE "%{}%"
                  and emergência LIKE "%{}%"
                  and endereço LIKE "%{}%"
                  and CEP LIKE "%{}%"
                  and bairro LIKE "%{}%"
                  and cidade LIKE "%{}%"
                  and estado LIKE "%{}%"
                  and observação LIKE "%{}%" ORDER BY {} ASC'''
updateProfessional = '''UPDATE Profissionais
                      SET nome = "{}",
                          CPF = "{}",
                          admissão = "{}",
                          e_mail = "{}",
                          telefone = "{}",
                          emergência = "{}",
                          endereço = "{}",
                          CEP = "{}",
                          bairro = "{}",
                          cidade = "{}",
                          estado = "{}",
                          foto = "{}",
                          observação = "{}"
                      WHERE ID = {}'''

# tables for client informations =================================
tableWithInformationsProfesiionalTreeview1 = [['', '', '', '', ''], ['    ID    ', '    Nome    ', '    CPF    ', '    Admissão    ', ' E-mail ', 'Telefone']]
tableWithInformationsProfesiionalTreeview2 = [['', '', '', '', ''], [' Emergência ', ' Endereço ', ' CEP ', ' Bairro ', ' Cidade ', ' Estado ']]
tableWithInformationsComplementaryProfesiional = [[''], ['Total de profissionais']]

# sql comands for services informations ==============================
registerServices = (
    'INSERT INTO Serviços (serviço, valor)'
    'VALUES ("{}", "{}")'
)
searchServices = '''SELECT * 
                  FROM Serviços
                  WHERE {} LIKE "%{}%"
                  and valor LIKE "%{}%" ORDER BY {} ASC'''

updateService = '''UPDATE Serviços
                      SET serviço = "{}",
                          valor = "{}"
                      WHERE ID = {}'''

# tables for client informations =================================
tableWithInformationsServiceTreeview = [['', '', ''], ['    ID    ', '    Serviço    ', 'Valor']]
tableWithInformationsComplementaryService = [[''], ['Total de Serviços']]

# sql comands for services informations ==============================
registerBarCode = (
    'INSERT INTO Código_de_barras (profissional, serviço, código, foto, observação)'
    'VALUES ("{}", "{}", "{}", "{}", "{}")'
)
searchBarCode = '''SELECT * 
                  FROM Código_de_barras
                  WHERE {} LIKE "%{}%"
                  and serviço LIKE "%{}%" 
                  and código LIKE "%{}%"
                  and observação LIKE "%{}%" ORDER BY {} ASC'''

updateBarCode = '''UPDATE Código_de_barras
                      SET profissional = "{}",
                          serviço = "{}",
                          observação = "{}"
                      WHERE ID = {}'''

# tables for client informations =================================
tableWithInformationsBarCodeTreeview = [['', '', '', ''], ['    ID    ', '  Profissional  ', '  Serviço  ', '  Código  ']]
tableWithInformationsComplementaryBarCode = [[''], ['Total de Serviços']]

# sql comands for services informations ==============================
registerInformationsOfStock = (
    'INSERT INTO {} ({})'
    'VALUES ("{}")'
)
searchInformationsOfStock = '''SELECT * 
                  FROM {}
                  WHERE {} LIKE "%{}%" ORDER BY {} ASC'''

updateInformationsOfStock = '''UPDATE {}
                      SET {} = "{}"
                      WHERE ID = {}'''

# sql comands for usage stock ==============================
registerUsageStock = (
    'INSERT INTO Estoque_de_uso (fornecedor, marca, tipo, quantidade, medida, valor, validade, saída, restante, entrada, modificação, foto, observação)'
    'VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'
)
searchUsageStock = '''SELECT * 
                  FROM Estoque_de_uso
                  WHERE fornecedor LIKE "%{}%"
                  and marca LIKE "%{}%"
                  and tipo LIKE "%{}%"
                  and quantidade LIKE "%{}%"
                  and medida LIKE "%{}%"
                  and valor LIKE "%{}%"
                  and validade LIKE "%{}%"
                  and saída LIKE "%{}%"
                  and restante LIKE "%{}%"
                  and entrada LIKE "%{}%"
                  and modificação LIKE "%{}%" 
                  and observação LIKE "%{}%" ORDER BY {} ASC'''

updateUsageStock = '''UPDATE Estoque_de_uso
                      SET fornecedor = "{}",
                          marca = "{}",
                          tipo = "{}",
                          quantidade = "{}",
                          medida = "{}",
                          valor = "{}",
                          validade = "{}",
                          saída = "{}",
                          restante = "{}",
                          entrada = "{}",
                          modificação = "{}",
                          foto = "{}",
                          observação = "{}"
                      WHERE ID = {}'''

# tables for client informations =================================
tableWithInformationsUsageStockTreeview1 = [['', '', '', '', '', ''], ['ID', 'Fornecedor', 'Marca', 'Tipo', 'Quantidade', 'Medida']]
tableWithInformationsUsageStockTreeview2 = [['', '', '', '', ''], ['Valor', 'Validade', 'Saída', 'Q/Restante', 'Entrada', 'Modificação']]
tableWithInformationsComplementaryUsageStock = [['', '', '', ''], ['Produtos', 'Valor total', 'Vencidos', 'Acabados']]
# message informations usage stock ===============================
messageUseStock = ('Total de produtos = {}\n'
                   'Valor total = {}\n'
                   'Vencidos = {}\n'
                   'Acabados = {}')

# sql comands for sale stock ==============================
registerSaleStock = (
    'INSERT INTO Estoque_de_venda (fornecedor, marca, tipo, quantidade, medida, valor_de_compra, valor_de_venda, validade, cliente, método_de_pagamento, entrada, foto, observação, modificação)'
    'VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'
)
searchSaleStock = '''SELECT ID, fornecedor, marca, tipo, quantidade, medida, valor_de_compra, valor_de_venda, validade, cliente, método_de_pagamento, entrada, modificação
                  FROM Estoque_de_venda
                  WHERE fornecedor LIKE "%{}%"
                  and marca LIKE "%{}%"
                  and tipo LIKE "%{}%"
                  and quantidade LIKE "%{}%"
                  and medida LIKE "%{}%"
                  and valor_de_compra LIKE "%{}%"
                  and valor_de_venda LIKE "%{}%"
                  and validade LIKE "%{}%"
                  and cliente LIKE "%{}%"
                  and método_de_pagamento LIKE "%{}%"
                  and entrada LIKE "%{}%"
                  and observação LIKE "%{}%" ORDER BY {} ASC'''

updateSaleStock = '''UPDATE Estoque_de_venda
                      SET fornecedor = "{}",
                          marca = "{}",
                          tipo = "{}",
                          quantidade = "{}",
                          medida = "{}",
                          valor_de_compra = "{}",
                          valor_de_venda = "{}",
                          validade = "{}",
                          cliente = "{}",
                          método_de_pagamento = "{}",
                          entrada = "{}",        
                          foto = "{}",
                          observação = "{}",
                          modificação = "{}"
                      WHERE ID = {}'''

# tables for client informations =================================
tableWithInformationsSaleStockTreeview1 = [['', '', '', '', '', ''], ['ID', 'Fornecedor', 'Marca', 'Tipo', 'Quantidade', 'Medida']]
tableWithInformationsSaleStockTreeview2 = [['', '', '', '', ''], ['V/compra', 'V/Venda', 'Validade', 'Cliente', 'Entrada', 'Modificação']]
tableWithInformationsComplementarySaleStock = [['', '', '', ''], ['Produtos', 'Vt/Compra', 'Vt/Venda', 'Reservados', 'Vencidos']]
# message informations usage stock ===============================
messageSaleStock = ('Total de produtos = {}\n'
                    'Valor total de compra = {}\n'
                    'Valor total de venda  = {}\n'
                    'Reservados = {}\n'
                    'Vencidos = {}')

# sql comands for usage stock ==============================
registerUsageStockUnusable = (
    'INSERT INTO Estoque_de_inutilizáveis (fornecedor, marca, tipo, quantidade, medida, valor, validade, saída, restante, data_de_saída, modificação, foto, observação)'
    'VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'
)
searchUsageStockUnusable = '''SELECT * 
                  FROM Estoque_de_inutilizáveis
                  WHERE fornecedor LIKE "%{}%"
                  and marca LIKE "%{}%"
                  and tipo LIKE "%{}%"
                  and quantidade LIKE "%{}%"
                  and medida LIKE "%{}%"
                  and valor LIKE "%{}%"
                  and validade LIKE "%{}%"
                  and saída LIKE "%{}%"
                  and restante LIKE "%{}%"
                  and data_de_saída LIKE "%{}%"
                  and modificação LIKE "%{}%" 
                  and observação LIKE "%{}%" ORDER BY {} ASC'''

updateUsageStockUnusable = '''UPDATE Estoque_de_inutilizáveis
                      SET fornecedor = "{}",
                          marca = "{}",
                          tipo = "{}",
                          quantidade = "{}",
                          medida = "{}",
                          valor = "{}",
                          validade = "{}",
                          saída = "{}",
                          restante = "{}",
                          data_de_saída = "{}",
                          modificação = "{}",
                          foto = "{}",
                          observação = "{}"
                      WHERE ID = {}'''

# tables for client informations =================================
tableWithInformationsUsageStockUnusableTreeview1 = [['', '', '', '', '', ''], ['ID', 'Fornecedor', 'Marca', 'Tipo', 'Quantidade', 'Medida']]
tableWithInformationsUsageStockUnusableTreeview2 = [['', '', '', '', ''], ['Valor', 'Validade', 'Saída', 'Q/Restante', 'D/Saída', 'Modificação']]
tableWithInformationsComplementaryUsageStockUnusable = [['', '', '', ''], ['Produtos', 'Valor total', 'Vencidos', 'Acabados']]

# sql comands for sale stock ==============================
registerSaleStockUnusable = (
    'INSERT INTO Estoque_de_vendidos (fornecedor, marca, tipo, quantidade, medida, valor_de_compra, valor_de_venda, validade, cliente, método_de_pagamento, venda, foto, observação, modificação)'
    'VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'
)
searchSaleStockUnusable = '''SELECT ID, fornecedor, marca, tipo, quantidade, medida, valor_de_compra, valor_de_venda, validade, cliente, método_de_pagamento, venda, modificação 
                  FROM Estoque_de_vendidos
                  WHERE fornecedor LIKE "%{}%"
                  and marca LIKE "%{}%"
                  and tipo LIKE "%{}%"
                  and quantidade LIKE "%{}%"
                  and medida LIKE "%{}%"
                  and valor_de_compra LIKE "%{}%"
                  and valor_de_venda LIKE "%{}%"
                  and validade LIKE "%{}%"
                  and cliente LIKE "%{}%"
                  and método_de_pagamento LIKE "%{}%"
                  and venda LIKE "%{}%"
                  and observação LIKE "%{}%" ORDER BY {} ASC'''

updateSaleStockUnusable = '''UPDATE Estoque_de_vendidos
                      SET fornecedor = "{}",
                          marca = "{}",
                          tipo = "{}",
                          quantidade = "{}",
                          medida = "{}",
                          valor_de_compra = "{}",
                          valor_de_venda = "{}",
                          validade = "{}",
                          cliente = "{}",
                          método_de_pagamento = "{}",
                          venda = "{}",
                          foto = "{}",
                          observação = "{}",
                          modificação = "{}"
                      WHERE ID = {}'''

# tables for stock informations =================================
tableWithInformationsSaleStockUnusableTreeview1 = [['', '', '', '', '', ''], ['ID', 'Fornecedor', 'Marca', 'Tipo', 'Quantidade', 'Medida']]
tableWithInformationsSaleStockUnusableTreeview2 = [['', '', '', '', ''], ['V/compra', 'V/Venda', 'Validade', 'Cliente', 'venda', 'Modificação']]
tableWithInformationsComplementarySaleStockUnusable = [['', '', '', ''], ['Produtos', 'Vt/Compra', 'Vt/Venda', 'Reservados', 'Vencidos']]
# sql comands for cash ==============================
registerCashManagement = (
    'INSERT INTO {} (t_clientes, t_produtos, t_cartão, t_dinheiro, t_transferência, t_nota, s_cartão, s_dinheiro, s_transferência, s_nota, a_receber, t_recebido, {}, status, observação)'
    'VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'
)
searchCashManagement = '''SELECT *
                  FROM {}
                  WHERE t_clientes LIKE "%{}%"
                  and t_produtos LIKE "%{}%"
                  and t_cartão LIKE "%{}%"
                  and t_dinheiro LIKE "%{}%"
                  and t_transferência LIKE "%{}%"
                  and t_nota LIKE "%{}%"
                  and {} LIKE "%{}%"
                  and a_receber LIKE "%{}%"
                  and t_recebido LIKE "%{}%"
                  and {} LIKE "%{}%"
                  and status LIKE "%{}%"
                  and observação LIKE "%{}%" ORDER BY {} ASC'''

updateCashManagement = '''UPDATE {}
                      SET t_clientes = "{}",
                          t_produtos = "{}",
                          t_cartão = "{}",
                          t_dinheiro = "{}",
                          t_transferência = "{}",
                          t_nota = "{}",
                          {} = "{}",
                          a_receber = "{}",
                          t_recebido = "{}",
                          {} = "{}",
                          status = "{}",
                          observação = "{}"
                      WHERE ID = {}'''

# tables for client informations =================================
tableWithInformationsCashManagementTreeview1 = [['', '', '', '', '', '', '', ''], ['ID', 'T/Clientes', 'T/Produtos', 'T/Cartão', 'T/Dinheiro', 'T/Transferência', 'T/Nota', 'S/Cartão']]
tableWithInformationsCashManagementTreeview2 = [['', '', '', '', '', '', ''], ['S/Dinheiro', 'S/Transferência', 'S/Nota', 'A receber', 'T/Recebido', 'Status']]
tableWithInformationsComplementaryCashManagement = [['', '', '', '', ''], ['T/Clientes', 'T/Produtos', 'T/Recebido', 'T/Saída']]
# message informations cash day ===============================
messageCashManagement = ('{}= {}\n'
                         'Total de clientes = {}\n'
                         'Total de produtos  = {}\n'
                         'Total recebido = {}\n'
                         'Total de Saida = {}')

# sql comands for payments ==============================
registerCashPayment = (
    'INSERT INTO Gerenciador_de_pagamentos (profissional, mês_de_pagamento, t_clientes, faturamento, porcentagem, pagamento, método_de_pagamento, data_de_pagamento, observação)'
    'VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'
)
searchCashPayment = '''SELECT *
                  FROM Gerenciador_de_pagamentos
                  WHERE profissional LIKE "%{}%"
                  and mês_de_pagamento LIKE "%{}%"
                  and t_clientes LIKE "%{}%"
                  and faturamento LIKE "%{}%"
                  and porcentagem LIKE "%{}%"
                  and pagamento LIKE "%{}%"
                  and método_de_pagamento LIKE "%{}%"
                  and observação LIKE "%{}%" ORDER BY {} ASC'''

updateCashPayment = '''UPDATE Gerenciador_de_pagamentos
                      SET profissional = "{}",
                          mês_de_pagamento = "{}",
                          t_clientes = "{}",
                          faturamento = "{}",
                          porcentagem = "{}",
                          pagamento = "{}",
                          método_de_pagamento = "{}",
                          observação = "{}"
                      WHERE ID = {}'''

# tables for client informations =================================
tableWithInformationsCashPaymentTreeview1 = [['', '', '', '', ''], ['ID', 'Profissional', 'M/Pagamento', 'T/Clientes', 'Faturamento']]
tableWithInformationsCashPaymentTreeview2 = [['', '', '', ''], ['%', 'Pagamento', 'Mt/Pagamento', 'D/Pagamento']]
tableWithInformationsComplementaryCashPayment = [['', '', ''], ['Pagamentos', 'T/Clientes', 'T/Faturamento']]
# message informations cash day ===============================
messageCashPayment = ('Profissionais = {}\n'
                      'Total de clientes = {}\n'
                      'Total de Faturamento  = {}')

# sql comands for users ==============================
registerUsers = (
    'INSERT INTO Usuários (nome, senha, nivel)'
    'VALUES ("{}", "{}", "{}")'
)
searchUsers = '''SELECT *
                  FROM Usuários
                  WHERE nome LIKE "%{}%"
                  and nivel LIKE "%{}%"'''
updateUsers = '''UPDATE Usuários
                      SET nome = "{}",
                          senha = "{}",
                          nivel = "{}"
                      WHERE ID = {}'''