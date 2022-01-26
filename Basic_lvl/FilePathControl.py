import os
import datetime

data_input_catalog = 'c:\\temp\\data_input'
data_output_catalog = 'C:\\Temp\\data_output'

today = datetime.date.today()
todayOutputCatalog = os.path.join(data_output_catalog, today.strftime('%y-%m-%d'))

isInputCatalogOk = os.path.isdir(data_input_catalog)
isOutputCatalogOk = os.path.isdir(data_output_catalog)
isTodayOutputCatalogOk = not os.path.isdir(todayOutputCatalog) and not os.path.isfile(todayOutputCatalog)

if isInputCatalogOk and isOutputCatalogOk and isTodayOutputCatalogOk:
    print('Conditions met! We can continue')
else:
    if not isInputCatalogOk:
        print('Error - Input catalog does not exist')
    elif not isOutputCatalogOk:
        print('Error - Output catalog does not exist')
    else:
        print('Error - Today catalog exist.')

