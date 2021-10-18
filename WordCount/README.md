#Steps for Executing Word Count Program in Hadoop :

Step 1:

 Create a file Input.txt with some data in it to count the words.


Step 2:

Create a mapper.py file that implements the mapper logic. 
Syntax: To Run Command(in my case) cat WordCount/Input.txt.| python3 mapper.py 

Step 3:
Create a reducer.py file that implements the reducer logic. 
Syntax: cat WordCount/Input.txt | python mapper.py | sort -k1,1 | python3 reducer.py

Step 4:

Hadoop daemons with the below command. $ start-all.sh

Create a directory : $ hdfs dfs -mkdir /word_count_python

Copy Input.txt to this folder in our HDFS with help of put command. $ hdfs dfs -put /Documents/Input.txt /WordCount

Executable permission to our mapper.py and reducer.py with the help of the below command. $ chmod 777 word_count_data.txt

Step 5:  $ hadoop jar /home/ubunta/hadoop-3.3.1/share/hadoop/tools/lib/hadoop-streaming-jar-3.3.1 \

    -mapper /home/ubunta/Desktop/WordCountMapReduce/mapper.py -mapper "python3 mapper.py"
    -reducer /home/ubunta/Desktop/WordCountMapReduce/reducer.py -reducer "python3 reducer.py"
    -input /WordCount/Input.txt
    -output /WordCount/output

Now let’s run our python files: $ hdfs dfs -cat /word_count_python/output/part-00000




