# Homework03
Welcome to my repo for my Homework03! 🤠

## About CSCMC40BOT! 🤖
My bot supports Biden and is super anti-Trump. 

Check out [this](https://www.reddit.com/r/csci040temp/comments/jm338w/another_debate_post/gasmjyx?utm_source=share&utm_medium=web2x&context=3) fun thread my bot participated in!

<img width="718" alt="Screen Shot 2020-11-04 at 12 04 00 AM" src="https://user-images.githubusercontent.com/70279041/98035974-b6dbfa80-1e32-11eb-8cd8-c778ebffb646.png">


I like this thread because, firstly, my bot started the debate that took place. I like that the NamesBotJamesBot came in and supported by bot. MrCS40-Bot didn't though 😤


## Bot Counter Output
    len(comments)= 1000
    len(top_level_comments)= 76
    len(replies)= 924
    len(valid_top_level_comments)= 76
    len(not_self_replies)= 271
    len(valid_replies)= 924
    ========================================
    valid_comments= 1000
    ========================================
    NOTE: the number valid_comments is what will be used to determine your extra credit

## My Score 🥳

Github Repo = 2 pts
All Tasks Completed = (6*2) = 12 pts 
100 Comments Posted = 2pts = 16/20

Extra: 
Have your bot upvote any comment mentioning your favorite candidate. +1

Have your bot downvote any comment mentioning your favorite candidate. +1

Have your bot upvote any submission mentioning your favorite candidate. +1

Have your bot downvote any submission mentioning your favorite candidate. +1

If your bot writes more than 500 comments, you get this extra credit +1

If your bot writes more than 1000 comments, you get this extra credit +1

TOTAL = **22/20**

## Tasks I didn't complete 😔
Make your bot reply to highly upvoted comments before replying to lower upvoted comments. (HINT: sort the comments_without_replies list by the score of the comment using the key parameter to the sorted function; see the python docs for examples)

Have your bot post new submissions to the /r/csci040 subreddit. These submissions should be from the top submissions of a political subreddit that supports your favorite presidential candidate (e.g. /r/politics or /r/conservative). Your bot must post at least 20 of these submissions to receive the extra credit.

Create an army of at least 10 bots that all upvote posts according to the same criteria. This will let you manipulate which posts/comments are the most upvoted, and therefore the most read. If your bot army contains 30 bots you'll get an additional 2 points of extra credit.

Use the textblob library to measure the sentiment of every comment/submission. If it mentions your favorite candidate with a positive sentiment, then upvote it; if it mentions your favorite candidate with a negative sentiment, then downvote it. Conversely, if it mentions a candidate you don't like with positive sentiment, then downvote it; if it mentions a candidate you don't like with negative sentiment, then upvote it. If you complete this extra credit, you also get both of the 1 point extra credits for upvoting.

Have the responses of your bot somehow depend on what the comment you are replying to is saying. For example, if you are writing a bot that supports Trump, you might detect if the previous comment talks about Biden. If it does, you might reply Biden sucks, Trump is better. Alternatively, you might detect that the previous comment mentioned Trump with a negative sentiment and reply I disagree, Trump is actually really great. The amount of extra credit you get for this will vary depending on the creativity of your idea.

