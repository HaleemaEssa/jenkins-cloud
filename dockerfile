FROM python:3
WORKDIR /usr/app/
COPY . .
#########
#########
RUN apt-get clean
##########
RUN python3 -m pip install pika --upgrade
RUN pip install --no-cache-dir numpy matplotlib
RUN pip3 install pandas
#COPY . .
#COPY rnh.py .
#CMD ["r.py"]
#COPY data.csv .
#CMD ["rnhbooth.py"]
#CMD ["rnhbth.py"]
#CMD ["arr.py"]
#CMD ["onec.py"]
#CMD ["msg.py"]
#CMD ["msght.py"]
#CMD ["msght1.py"]
#CMD ["aprod1.py"]
#CMD ["acon.py"]
#CMD ["aacon1.py"]
#CMD ["plot.py"]
CMD ["rec-cloud.py"]
ENTRYPOINT ["python3"]
#CMD ["python","./aacon1.py"]
