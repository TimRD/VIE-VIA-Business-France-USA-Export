from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import xlsxwriter

def findofferusa():
    options = Options()
    options.headless = False
    #replace your file path to the chrome driver, to download it go to : https://sites.google.com/chromium.org/driver/
    DRIVER_PATH = '/Users/timotheemarguier/Downloads/chromedriver'
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    #replace this link with the filters you need to use on mon-vie-via.businessfrance.fr
    driver.get('https://mon-vie-via.businessfrance.fr/en/offres/recherche?query=&gerographicZones=2&countriesIds=62')
    time.sleep(1)
    driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
    time.sleep(2)

    #We cath the number of results
    offersnumbertext = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/main/section[2]/div[2]/p').text
    #Transform the text to keep only the int numer
    offersnumber = [int(i) for i in offersnumbertext.split() if i.isdigit()]

    # print result
    print("Number of offers : ", offersnumber[0])

    #We use it at a limit to know when wa have to stop
    nbannoncesmax = offersnumber[0]+1
    nbannonces = 0
    #We check that the max offers can't be overdue
    while nbannonces<nbannoncesmax:
        try:
            element = driver.find_element(By.CSS_SELECTOR, ".see-more-btn")
            driver.execute_script("arguments[0].click();", element)
            nbannonces = nbannonces+6
            #ensure that the click is not interpreted as a double-click
            time.sleep(0.2)
            print(nbannonces)
        except NoSuchElementException:
            print('End')
            nbannonces = nbannoncesmax


    time.sleep(1)

    #To get all locations
    offercity = driver.find_elements(By.CSS_SELECTOR, 'p.location')

    #To get all details
    annonces = driver.find_elements(By.CSS_SELECTOR, '.figure-item')


    #
    workbook = xlsxwriter.Workbook('export-vie.xlsx')

    # The workbook object is then used to add new
    # worksheet via the add_worksheet() method.
    worksheet = workbook.add_worksheet()

    # Use the worksheet object to write
    # data via the write() method.
    worksheet.write('A1', 'City')
    worksheet.write('B1', 'Details')

    # Finally, close the Excel file
    # via the close() method.
    row = 1

    for z in offercity:

        worksheet.write(row, 0, z.text)
        row += 1
    print('nb de villes', row)
    row=1
    for i in annonces:
        worksheet.write(row, 1, i.text)
        row += 1
    print('nb d annonces', row)

    driver.quit()

    workbook.close()



findofferusa()
