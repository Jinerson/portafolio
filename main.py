from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
from selenium import webdriver
import time, os
import pandas as pd

user = "standard_user"
password = "secret_sauce"

def main():
    service = Service(EdgeChromiumDriverManager().install())
    options = webdriver.EdgeOptions()
    driver = Edge(options, service)
    driver.get("https://www.saucedemo.com/")
    time.sleep(1)

    box_user = driver.find_element(By.ID, value = "user-name" )
    box_user.send_keys(user)
    time.sleep(1)

    box_password = driver.find_element(By.ID, value = "password" )
    box_password.send_keys(password)
    time.sleep(1)

    btn_login = driver.find_element(By.ID, value = "login-button" )
    btn_login.click()
    time.sleep(1)

    items = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item']")
    precios = []
    nombres = []
    desc = []

    for i in items:
        nombres.append(i.find_element(By.XPATH, ".//div[@class = 'inventory_item_name ']").text)
        precios.append(i.find_element(By.XPATH, ".//div[@class = 'inventory_item_price']").text)
    time.sleep(5)

    salida = {
        "Producto":nombres,
        "Precio":precios
    }
    a = pd.DataFrame(salida)
    a.to_csv(os.path.join(os.getcwd(),"a.csv"), index=0)
    driver.quit()

if __name__ == "__main__":
    main()