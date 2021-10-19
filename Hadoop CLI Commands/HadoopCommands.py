import subprocess

def run_cmd(args_list):
        """
        Description:
                run linux commands.
        Parameter: 
                it takes args_list as parameter.
        Return:
                it returns s_return, s_output, s_err.
        """
        print('Running system command: {0}'.format(' '.join(args_list)))
        proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        s_output, s_err = proc.communicate()
        s_return =  proc.returncode
        return s_return, s_output, s_err 

if __name__ == "__main__":
    #Run Hadoop mkdir command in python
    mkdir = run_cmd(['hdfs', 'dfs', '-mkdir', '/Hadoop'])
    print(mkdir)
    
    #Run Hadoop ls command in Python
    ls = run_cmd(['hdfs', 'dfs', '-ls', '/Hadoop'])
    print(ls)

    #Run Hadoop put command in Python
    put = run_cmd(['hdfs', 'dfs', '-put', '/home/ubuntu/Documents/WordCount/Input.txt', '/Hadoop'])
    print(put)

    #Run Hadoop copyFromLocal command in Python
    copyFromLocal = run_cmd(['hdfs', 'dfs', '-copyFromLocal', '/home/ubuntu/Documents/WordCount/Input.txt', '/Hadoop'])
    print(copyFromLocal)

    #Run Hadoop get command in Python
    get = run_cmd(['hdfs', 'dfs', '-get', '/Hadoop/Input.txt', '/home/ubuntu/Documents/CopyFromHadoop'])
    print(get) 

    #Run Hadoop copyToLocal command in Python
    copyToLocal = run_cmd(['hdfs', 'dfs', '-copyToLocal', '/Hadoop/WordCountData.txt', '/home/ubuntu/Documents/CopyFromHadoop'])
    print(copyToLocal)

    #Run Hadoop cat command in Python
    cat= run_cmd(['hadoop', 'fs', '-cat', '/Hadoop/Input.txt'])
    print(cat)

    #Run Hadoop moveFromLocal command in python
    moveFromLocal = run_cmd(['hdfs', 'dfs', '-moveFromLocal', '/home/ubuntu/Documents/WordCount/WordCountData.txt', '/Hadoop'])
    print(moveFromLocal)
   