import pika, os, sys, time
import pandas
import csv
from datetime import datetime
import pandas as pd
def main():
    with open('data2.csv', mode='a') as data:
        data_writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    import pandas as pd
    f = open("data2.csv","a")
    if os.stat('data2.csv').st_size == 0:
       f.write("Date,Sound,Flame,Humidity,Temperature\n")

    f = open("data2.csv","r+")
    def callback(ch, method, properties, body):
        f = open("data2.csv","a")
        msg=body.decode()
        msg1=str(msg[2:33])
        print(" PDF processing")
        print(" [x] Received " + str(msg1))
        f.write(str(msg[2:21])+","+str(msg[22])+","+str(msg[24])+","+str(msg[26:28])+","+str(msg[29:31])+"\n")
        print(" PDF processing finished")
# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
#    url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
    url = os.environ.get('CLOUDAMQP_URL', 'amqps://kacojdss:aUd8wEoKcyHLCK46a1_AifxUBDzjsLHi@beaver.rmq.cloudamqp.com/kacojdss')
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel() # start a channel
    channel.queue_declare(queue='pdfprocess') # Declare a queue

# create a function which is called on incoming messages
    channel.basic_consume('pdfprocess',callback,auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
if __name__ == '__main__':
    try:
        main()
    except: # KeyboardInterrupt:  #OSError: #KeyboardInterrupt: #IOError: # GeneratorExit:  #EOFError: #IOError: #KeyboardInterrupt:
        import pandas as pd
        df=pd.read_csv('data2.csv') #,header=None)
        df['Date']=pd.to_datetime(df['Date'])
        print (type(df['Date'][0]))
   #     print(df)
        df.set_index('Date', inplace=True)
        print(df)
        df4=df.resample('D').mean() #in Cloud
        df4.to_csv("res_data.csv")        
        print(df4)
        import numpy as np       
        import matplotlib.pyplot as plt
        from matplotlib import dates as mpl_dates
        from datetime import datetime, timedelta
        import pandas as pd
        plt.style.use('seaborn')
        data=pd.read_csv('data2.csv')
########### Plotting Temperature Data ################
        data['Date'] = pd.to_datetime(data['Date'])
        data.sort_values('Date', inplace=True)
        price_date = data['Date']
        price_close = data['Temperature']
        f = plt.figure()
        plt.plot_date(price_date, price_close) #, linestyle='solid')
        plt.gcf().autofmt_xdate()
        date_format = mpl_dates.DateFormatter('%H-%M-%S') # y m dfor year.... 
        plt.gca().xaxis.set_major_formatter(date_format)
        plt.tight_layout()
        plt.title('Temprature_data Plotting')
        plt.xlabel('Date')
        plt.ylabel('Temperature')
# Save the scatter plot to two output files (on the Docker host).
        f.savefig("output.pdf", bbox_inches='tight')
        f.savefig("output.png", bbox_inches='tight')
################ Plotting Humidity Data ##############
        import matplotlib.pyplot as plt1
        plt1.style.use('seaborn')
        f1=plt1.figure()
        plt1.plot_date(data['Date'], data['Humidity'])
        date_format = mpl_dates.DateFormatter('%y-%m-%d')
        plt1.gca().xaxis.set_major_formatter(date_format)
        plt1.tight_layout()
        plt1.title('Humidity_data Plotting')
        plt1.xlabel('Date')
        plt1.ylabel('Humidity')
        f1.savefig("output1.png", bbox_inches='tight')
############# Temp & Hum  Data in the same figure ################
        import matplotlib.pyplot as pp
        pp.style.use('seaborn')
        f55=pp.figure()
        pp.plot_date(data['Date'], data['Temperature'], label='Temperature')
        pp.plot_date(data['Date'], data['Humidity'], label='Humudity')
        date_format = mpl_dates.DateFormatter('%y-%m-%d')
        pp.gca().xaxis.set_major_formatter(date_format)
        pp.legend()
        pp.tight_layout()
        pp.title('Temperature_and_Humidity_data Plotting')
        pp.xlabel('Date')
        pp.ylabel('Temperature & Humidity')
        f55.savefig("output55.png", bbox_inches='tight')
################ SubPlotting Data ##################
        import matplotlib.pyplot as pl1
        pl1.style.use('seaborn')
        fig1, (ax1, ax2, ax3)=pl1.subplots(nrows=3, ncols=1, sharex=True) #, figsize=(15,5))
        ax1.plot_date(data['Date'], data['Temperature'], label='Temperature')
        ax2.plot_date(data['Date'], data['Humidity'], label='Humudity')
        ax3.plot_date(data['Date'], data['Temperature'], label='Temperature')
        ax3.plot_date(data['Date'], data['Humidity'], label='Humudity')

        date_format = mpl_dates.DateFormatter('%y-%m-%d')
        pl1.gca().xaxis.set_major_formatter(date_format)
        ax1.legend()
        ax1.set_title('Temperature_data Plotting')
#        ax1.set_xlabel('Date')
        ax1.set_ylabel('Temperature')
        ax2.legend()
        ax2.set_title('Humidity_data Plotting')
       # ax2.set_xlabel('Date')
        ax2.set_ylabel('Humidity')
        ax3.legend()
        ax3.set_title('Temperature & Humidity_data Plotting')
        ax3.set_xlabel('Date')
        ax3.set_ylabel('Temperature &  Humidity ')
        pl1.tight_layout()
        fig1.savefig("output11.png", bbox_inches='tight')
################ Plotting Resampled Humidity Data ################
        import pandas as pd1
        import matplotlib.pyplot as plt2
        data1=pd1.read_csv('res_data.csv')
        data1['Date'] = pd1.to_datetime(data1['Date'])
        data1.sort_values('Date', inplace=True)
        plt2.style.use('seaborn')
        f2=plt2.figure()
        plt2.plot_date(data1['Date'], data1['Humidity'])
        date_format = mpl_dates.DateFormatter('%y-%m-%d')
        plt2.gca().xaxis.set_major_formatter(date_format)
        plt2.tight_layout()
        plt2.title('Resampled_Humidity_data Plotting')
        plt2.xlabel('Date')
        plt2.ylabel('Humidity')
        f2.savefig("output2.png", bbox_inches='tight')
################ Plotting Resampled Temperature Data #########
        import matplotlib.pyplot as plt3
        plt3.style.use('seaborn')
        f3=plt3.figure()
        plt3.plot_date(data1['Date'], data1['Temperature'])
        date_format = mpl_dates.DateFormatter('%y-%m-%d')
        plt3.gca().xaxis.set_major_formatter(date_format)
        plt3.tight_layout()
        plt3.title('Resampled_Temperature_data Plotting')
        plt3.xlabel('Date')
        plt3.ylabel('Temperature')
        f3.savefig("output3.png", bbox_inches='tight')
############# Resampled data in the same figure ################
        import matplotlib.pyplot as p
        p.style.use('seaborn')
        f5=p.figure()
        p.plot_date(data1['Date'], data1['Temperature'], label='Temperature')
        p.plot_date(data1['Date'], data1['Humidity'], label='Humudity')
        date_format = mpl_dates.DateFormatter('%y-%m-%d')
        p.gca().xaxis.set_major_formatter(date_format)
        p.legend()
        p.tight_layout()
        p.title('Resampled_Temperature_and_Humidity_data Plotting')
        p.xlabel('Date')
        p.ylabel('Temperature & Humidity')
        f5.savefig("output5.png", bbox_inches='tight')
################## SubPlotting Resampled Data #######
        import matplotlib.pyplot as pl
        pl.style.use('seaborn')
        f4=pl.figure()
        fig, (ax1, ax2, ax3)=pl.subplots(nrows=3, ncols=1, sharex=True) #, figsize=(15,5))
        ax1.plot_date(data1['Date'], data1['Temperature'], label='Temperature')
        ax2.plot_date(data1['Date'], data1['Humidity'], label='Humudity')
        ax3.plot_date(data1['Date'], data1['Temperature'], label='Temperature')
        ax3.plot_date(data1['Date'], data1['Humidity'], label='Humudity')

        date_format = mpl_dates.DateFormatter('%y-%m-%d')
        pl.gca().xaxis.set_major_formatter(date_format)
        ax1.legend()
        ax1.set_title('Resampled_Temperature_data Plotting')
#        ax1.set_xlabel('Date')
        ax1.set_ylabel('Temperature')
        ax2.legend()
        ax2.set_title('Resampled_Humidity_data Plotting')
       # ax2.set_xlabel('Date')
        ax2.set_ylabel(' Humidity')
        ax3.legend()
        ax3.set_title('Resampled_Temperature & Humidity_data Plotting')
        ax3.set_xlabel('Date')
        ax3.set_ylabel('Temperature &  Humidity ')
        pl.tight_layout()
        fig.savefig("output4.png", bbox_inches='tight')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
