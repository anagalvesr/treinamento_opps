import json
import requests
import urllib.request
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def acessar_pagina_dinamica(link):
    #definir navegador simulado 
    navegador = webdriver.Chrome (service=ChromeService(ChromeDriverManager().install()))
    # abrir o link no navegador simulado
    navegador.get(link)
    # clicar na pasta de cada ano
    # <ul class="dom-list ">
    # <li class="directory collapsed">
    anos = navegador.find_element(By.XPATH,"//ul[@class='dom-list ']").find_elements(By.XPATH,"//li[@class='directory collapsed']")
    # anos = navegador.find_element(By.XPATH,"//ul[@class='dom-list ']").click()
    # <a class="dropfile-file-link" href="#" data-id="849">
    # pdfs = navegador.find_element(By.XPATH,"//li[@class='ext pdf']").click()
    print (len(anos))
    # clicar nos links do pdf
    for ano in anos:
        ano.click()
        sleep(5)
        pdfs = navegador.find_elements(By.XPATH,"//li[@class='ext pdf']//a[@class=dropfile-file-link]").get_attribute("data-id")
        print (len(pdfs))
        print (pdfs)
        for pdf in pdfs:
            pdf.find_element(By.XPATH,"//a[@class='dropfile-file-link']").click()
            sleep(2)
            tag_link = pdf.find_element(By.XPATH,"//div[@class='extra-downloadlink']//a[@class='downloadlink']")
            link_pdf = tag_link.get_attribute("href")
            print(link_pdf)
            sleep(3)
            botao_fechar = pdf.find_element(By.XPATH,"//div[@class='dropblock dropfiles-dropblock-content']//a[@class='dropfiles-close']")
            botao_fechar.click()
            sleep(2)
            continue


    sleep(3)

    
    
def main():
    link = "https://jeriquara.sp.gov.br/dom/"
    acessar_pagina_dinamica(link)
    
    
    
if __name__ == "__main__":
    main()