Code by Artur Pimentel de Oliveira
Assignment 1 - Social Sensing/Cyber Physical Systems
http://www3.nd.edu/~dwang5/courses/spring16/assignments/A1/Assignment1_SocialSensing.html

1. Intro
In the of the directories task1, task2 and task3 are the codes and respective results for every task of this assignment. Note that task3 has two codes and two results texts. "tweets_data_crawler.py" gather tweets that have one of thew words in the pair ['Indiana', 'weather']. Its result is shown in the file "result.txt". "tweets_data_crawler_geo.py" gather tweets around the region of South Bend, IN.

2. Commands and Code
Attention: You should put your own pairs of consumer and access keys in the rigth variables (code is commented on that) before running any code

For the codes related to the tasks 1 and 2, the command
> python data_crawler.py
or
> friends_data_crawler.py
will be enough. Both make the result files from the inside

For the codes in task 3, run the command
> python tweets_data_crawler.py
or
> python tweets_data_crawler_geo.py
if you want to see the results in the console. If you want a textfile, make sure to use
> python tweets_data_crawler.py > result.txt
or
> python tweets_data_crawler_geo.py > result_geo.txt

3. Final considerations
I tried to be as much specific as I could to the last task, but it seems that it takes too long for the code to filter any tweets exactly between the coordinates of South Bend whereabouts. You can test this by uncommenting the indicated code in "tweets_data_crawler_geo.py"