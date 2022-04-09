import pika, os, sys, time
import pandas
import csv
from datetime import datetime
import pandas as pd
def main():
    with open('/data/data2.csv', mode='a') as data:
        data_writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    import pandas as pd
    f = open("/data/data2.csv","a")
    if os.stat('/data/data2.csv').st_size == 0:
       f.write("Date,Sound,Flame,Humidity,Temperature\n")

    f = open("/data/data2.csv","r+")
    def callback(ch, method, properties, body):
        f = open("/data/data2.csv","a")
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
