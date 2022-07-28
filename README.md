# AffinityAnswers - Degree of Profanity by Twitter Users

PROBLEM STATEMENT :
 Imagine there is a file full of Twitter tweets by various users and you are provided a set of words that indicates racial slurs. Write a program that can indicate the degree of profanity for each sentence in the file. Write in any programming language (preferably in Python)-make any assumptions

SOLUTION :
Goal:
Here we wish to check degree of profanity against black people by twitter users. 

Assumption : 

1. There are 2 csv files :  

      a. Black_Racial_Slurs.csv  

          A file containing racial slurs - profane words with 3 columns :
            1. Racial Words : words commonly used against black people
            2. Ethinicity : 'Black'
            3. Reason-Context : 'Reason of why its a racial slur against blacks'


      b. tweets_blm.csv

          A file contaning tweets with one column 'Tweets'. 
          Each value is of pattern : '@user_id : their tweet'


  2. All racial slurs, user_ids, and tweets are in the English language
  3. Each user has only one tweet.
  4. No null values in both files.
  5. No duplicate values in both files.
  6. No spelling errors in both files.
  7. Each Racial Slur words is just a single word. No combination of two or three words is used as a racial slur word.


Program Files Description :

    1. Black_Racial_Slurs.csv :  File contaning racial slur words against black people.
    2. tweets_blm.csv : All tweets by various users on black lives matter campaign.
    3. preprocess.py :  Splits user_id and their tweet into two columns of a dataframe.
    4. clean_proccess.py :  Cleans tweets : Removes url links from each tweet, removes stopwords, removes punctuations from each tweet.
    5. profanity.py :   profanity score of tweet by each user_id - calculated by : (total number of racial slur words in each tweet / total number words in each tweet) * 100
    6. main.py : main file where the code is to be run and all functions are called.
    7. requirements.txt : All packages to be installed using command 'pip install -r requirements.txt'
    8. degree_of_profanity.csv :
          Final output for degree of profanity(racial slurs used) by various users against black people.
          profanity score range - 0 to 100.
          A score very close to 0 is low level of degree of profanity by an user_id.
          A score very close to 100 is very high level of degree of profanity by an user_id

Limitations of program:
1. The profanity score in final output file for each user doesn't neccessarily mean offensive tweet, as the context of tweet(sentence) is not taken into consideration by the program.
ex : A user might use certain words in different context to refer about an incident where such words were used by a third person.
2. The metric/method used has it's flaws, as it's not the best way to calculate the profainity. Different features can be used on big dataset for more robust     analysis. 
3. The stopwords used for text cleaning should be limited, as removing stopwords like 'not' might change the context of sentence, if a more robust analysis is done
through a different way. 
4. The program doesn't takes into consideration of any spelling/grammatical errors in tweets or racial words.
5. Only csv files are used for tweets file and racial word file. Not adjustment for json file/text file, etc.

