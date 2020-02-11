import urllib.request
import time
from datetime import date

#Valor do end_Time e sleepTime devem ser apresentados em segundos
end_time = time.time() + 1800
countTimer = 0
sleepTime = 600

dataAtual = date.today()
year = dataAtual.year

while time.time() < end_time:
    contador = 0
    print('File Download Start')
    url = 'http://www.mdic.gov.br/balanca/bd/comexstat-bd/ncm/EXP_'+str(year)+'.csv'
    urllib.request.urlretrieve(url, 'Exportação_'+str(year)+'.csv')
    contador += 1
    print ('File Download Over... Version:', contador)
    time.sleep(sleepTime)
    countTimer += sleepTime
    
print('Fim do sistema')
