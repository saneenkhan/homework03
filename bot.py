import praw
import random
import datetime
import time

# Week07 Lab
def generate_comment_0():
    biden_names = [' Joe Biden', ' Vice President Biden', ' Biden', ' Joe', ' VP Biden', 'J Biddy'] 
    biden_name = random.choice(biden_names)
    support = ['endorse', 'support', 'back', 'want']
    support_here = random.choice(support)
    role = ['role', 'office', 'position', 'duty']
    role_word = random.choice(role)
    president = ['president', 'commander in chief', 'prez', 'POTUS', 'leader of the free world']
    president_name = random.choice(president)
    adjective = ['intelligent', 'qualified', 'capable', 'brilliant', 'fabulous']
    adjective_name = random.choice(adjective)
    nation = [' country', ' nation', ' homeland', ' state']
    nation_name = random.choice(nation)
    adjectivetwo = [' strong.', ' prosperous.', ' superior.', ' thriving.']
    adjective_two = random.choice(adjectivetwo)
    text = 'I ' + support_here + biden_name + ' for the ' + role_word + ' of ' + president_name + ' because he is ' + adjective_name + '. He will keep our' + nation_name + adjective_two
    return text 

def generate_comment_1():
    trump = ['Donald Trump', 'President Trump', 'Trump', 'Donald', 'President Donald Trump', 'Cheeto Man']
    trump_name = random.choice(trump)
    adjectiveone = ['worst', 'most terrible', 'most desplicable', 'most idiotic']
    adjective_one = random.choice(adjectiveone)
    president = [' president', ' commander in chief', ' prez', ' POTUS', ' leader of the free world']
    president_name = random.choice(president)
    hate = [' hate', ' dislike', ' do not favor', ' disdain']
    hate_word = random.choice(hate)
    whythough = ['a bad person.', 'a racist.', 'a misogynist', 'a bad leader']
    why_though = random.choice(whythough)
    text = trump_name + ' is the ' + adjective_one + president_name + ' ever.' + ' I' + hate_word + ' him because he is ' + why_though
    return text

def generate_comment_2():
    harris = ['Kamala Harris', 'Harris', 'Kamala', 'Senator Harris', 'Senator Kamala Harris']
    harris_name = random.choice(harris)
    adjectiveone = [' great ', ' super cool ', ' good ', ' strong ']
    adjective_one = random.choice(adjectiveone)
    vicepresident = ['vice president.', 'VP.', 'vice prez.', 'Vice President.']
    vp_name = random.choice(vicepresident)
    adjectivetwo = [' intelligent ', ' determined ', ' well-spoken ', ' accomplished ']
    adjective_two = random.choice(adjectivetwo)
    appreciate = ['appreciate', 'like', 'respect', 'value']
    appreciate_word = random.choice(appreciate)
    text = harris_name + ' would be a' + adjective_one + vp_name + ' She is' + adjective_two + 'and I ' + appreciate_word + ' that.'
    return text

def generate_comment_3():
    biden_names = [' Joe Biden', ' Vice President Biden', ' Biden', ' Joe', ' VP Biden'] 
    biden_name = random.choice(biden_names)
    think = ['think ', 'believe ', 'hope ', 'am hopeful ']
    think_word = random.choice(think)
    president = [' president', ' commander in chief', ' prez', ' POTUS', ' leader of the free world']
    president_name = random.choice(president)
    better = ['better', 'superior than', 'stronger than', 'more intelligent than']
    better_word = random.choice(better)
    trump = [' Donald Trump', ' President Trump', ' Trump', ' Donald', ' President Donald Trump']
    trump_name = random.choice(trump)
    text = 'I ' + think_word + 'that' + biden_name + ' will become' + president_name + '. He is much ' + better_word + trump_name + '.'
    return text

def generate_comment_4():
    trump = ['Donald Trump', 'President Trump', 'Trump', 'Donald', 'President Donald Trump']
    trump_name = random.choice(trump)
    boot = ['booted', 'removed', 'kicked', 'taken', 'voted']
    boot_word = random.choice(boot)
    office = ['office.', 'the presidency.', 'the position of President.', 'the position of POTUS.']
    office_word = random.choice(office)
    adjective = ['an intelligent', 'a qualified', 'a capable', 'a brilliant', 'a good']
    adjective_name = random.choice(adjective)
    president = [' president.', ' commander in chief.', ' prez.', ' POTUS.', ' leader of the free world.']
    president_name = random.choice(president)
    text = trump_name + ' need to be ' + boot_word + ' out of ' + office_word + ' He is not ' + adjective_name + president_name
    return text

def generate_comment_5():
    biden_names = [' Joe Biden', ' Vice President Biden', ' Biden', ' Joe', ' VP Biden'] 
    biden_name = random.choice(biden_names)
    think = ['think', 'believe', 'argue', 'hope']
    think_word = random.choice(think)
    deserve = [' deserves to be', ' should be', ' is the best candidate for']
    deserve_word = random.choice(deserve)
    president = [' president.', ' commander in chief.', ' prez.', ' POTUS.', ' President of the United States.']
    president_name = random.choice(president)
    trump = ['Donald Trump.', 'President Trump.', 'Trump.', 'Donald.', 'President Donald Trump.']
    trump_name = random.choice(trump)
    text = 'I ' + think_word + ' that ' + biden_name + deserve_word + president_name + ' He is a much better choice than ' + trump_name
    return text

def generate_comment():
    '''
    This function should randomly select one of the 6 functions above,
    call that function, and return its result.
    '''
    comments = [generate_comment_0, generate_comment_1, generate_comment_2, generate_comment_3, generate_comment_4, generate_comment_5] 
    text = random.choice(comments)()
    return text

for i in range(10):
    print(generate_comment())

# Connect to Reddit 
reddit = praw.Reddit('bot')

# Connect to debate thread
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jm338w/another_debate_post/'
submission = reddit.submission(url=reddit_debate_url)

# Loop
start_time = datetime.datetime.now()

# Loop
while True:
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

# Task 0
    submission.comments.replace_more(limit=None) 
    # for limit None, goes through entire comment tree
    # for limit = 1, will go that level deep
    all_comments = []
    
    all_comments = submission.comments.list()
    print('len(all_comments)=',len(all_comments))
    # print(type(all_comments))

# Task 1
    not_my_comments = []
    my_comments = []
    for comment in all_comments:
        if comment.author == 'cs40cmcbot':
            my_comments.append(comment)
        else:
            not_my_comments.append(comment)

    print('len(not_my_comments)=',len(not_my_comments))
    print('len(my_comments)=',len(my_comments))

    has_not_commented = len(not_my_comments)

# Task 2
    if has_not_commented == len(all_comments):
        try:
            submission.reply(generate_comment())
        except: 
            print('exception found')
            print('starting to sleep')
            time.sleep(60) 
            print('done sleeping')

        print(generate_comment())

 
# Task 3

    else:
        comments_without_replies = []
        for comment in not_my_comments:
            replied = True
            for comment.reply in not_my_comments: 
                if comment.author == 'cs40cmcbot':
                     replied = True
                     break 
                if comment.author != 'cs40cmcbot':
                    replied = False 
            if replied:
                continue
            else:
                comments_without_replies.append(comment)         

        print('len(comments_without_replies)=',len(comments_without_replies))
        
# Task 4
        try:
            try:
                comment = reddit.comment(id=random.choice(comments_without_replies))
                print('comment_id =', random.choice(comments_without_replies))
                comment.reply(generate_comment())
            except:
                pass
        except: #AssertionError
            print('exception found')
            print('starting to sleep')
            time.sleep(60)
            print('done sleeping')

# Task 5
    result = random.random()
    all_submissions = []
    if result >= 0.5:
        print('original submission')
        submission = reddit.submission(url='https://www.reddit.com/r/csci040temp/comments/jm338w/another_debate_post/')
        submission.reply(generate_comment())
    if result < 0.5:
        print('top subreddit submission')
        # print(type(all_submissions))
        # for submission in reddit.subreddit("csci040").top("month"):
        for submission in reddit.subreddit("csci040temp").top("day"):

            all_submissions.append(submission)

        submission_choice = random.choice(all_submissions)
        submission = reddit.submission(id=submission_choice)
        print('submission_id =',submission_choice)
        print(submission_choice.title)

# Extra Credit 
# Upvote any comment mentioning  fav candidate
    for comment in submission.comments.list():
        if 'biden' in comment.body.lower():
            comment.upvote()
            print('Comment Upvoted!')

    # Downvote any comment mentioning the opposition
    for comment in submission.comments.list():
        if 'trump' in comment.body.lower():
            comment.downvote()
            print('Comment Downvoted!')

    for submission in reddit.subreddit('csci040temp'):

        # Upvote any submission mentioning  fav candidate
        if 'Biden' in submission.title.lower():
            submission.upvote()
            print('Submission Upvoted!')

        # Downvote any submission mentioning the opposition
        if 'Trump' in submission.title.lower():
            submission.downvote()
            print('Submission Downvoted!')

