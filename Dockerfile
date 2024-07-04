FROM python:3.10
EXPOSE 5000
WORKDIR /app
RUN pip install flask 
COPY . .
CMD ["flask", "run", "--host","0.0.0.0"]

#Each line from the above is a seperate layer and can be cached seperately 
#COPY . . Everything from the current directory. If I make changes again in the files the docker will make the changes and build the image again 