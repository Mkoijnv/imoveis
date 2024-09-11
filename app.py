import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime


driver = webdriver.Chrome()
driver.get("https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&id_cidade%5B%5D=21&finalidade=&dormitorio=&garagem=&vmi=&vma=&ordem=4")

#/html/body/section/div/div[3]/div[1]/div/div/div[1]/div[5]

#//div[@class='card-valores']/div
precos = driver.find_elements(By.XPATH, "//div[@class='card-valores']/div")
links = driver.find_elements(By.XPATH, "//a[@class='carousel-cell is-selected']")

workbook = openpyxl.load_workbook(filename="imoveisPY.xlsx")
wokbook_preco = workbook['Página1']

for preco,link in zip(precos,links):
    print(preco.text)
    preco_formatado = preco.text.split(" ")[1]
    link_pronto = link.get_attribute("href")
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    wokbook_preco.append([preco_formatado, link_pronto, data_atual])


workbook.save(filename="imoveisPY.xlsx")
