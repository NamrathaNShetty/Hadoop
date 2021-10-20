

Create a directory to save all the files related to word length program.

mkdir Matrix

Create a text file inside the created directory to store data in it.

touch input.txt nano input.txt. To edit the txt file

Create a mapper.py file to write the map function code.

nano mapper.py

Execute the mapper.py file

cat input.txt| python3 mapper.py

Create a reducer.py file to write the reduce function code.

nano reducer.py

Execute the mapper.py and reducer.py file

cat input.txt| python3 mapper.py | sort | python3 reducer.py

Start all apache hadoop daemons

start-all.sh

Create a directory in hadoop

hadoop fs -mkdir /Matrix

Copy the data file from local system to hadoop system

hadoop fs -put /home/ubuntu/Documents/Map Reduce/Matrix/Input1.txt /Matrix

Use the jar file, mapper and reducer file to execute the program

hadoop jar Hadoop jar/home/ubuntu/hadoop-3.3.1/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file  /home/ubuntu/Documents/Map Reduce/Matrix//mapper.py -mapper "python3 mapper.py"
-file  /home/ubuntu/Documents/Map Reduce/Matrix//reducer.py -reducer "python3 reducer.py"
-input /Matrix/input.txt
-output /Matrix/Output

Use cat command to check the output file

hadoop fs -cat /Matrix/Output/part-00000

