import random
def guess(a):
    rand_num=random.randint(1,a)
    guess=0
    while guess!=rand_num:
        guess=int(input("Enter number between 1 to {x}"))
        if guess < rand_num:
            print("sorry Again try ,VAlue is Low")
        elif guess > rand_num:
            print('Sorry Again try ,value is greater')
    print("yes Congrats You have guessed NUmber",rand_num)

#guess(10)
def Computer_guess(a):
    low=1
    high=a
    feedback=''
    while  feedback !='c':
        if low!=high:
            guess1=random.randint(low,high)
        else:
            guess1=lowz
        feedback=input("Is too high (h),Too Low (l),or correct")
        if feedback=='h':
            high=guess1-1
        elif feedback=='l':
            low=guess1+1
    madlib="yey!,congrats guessed  the NUmber"
    print(madlib)


Computer_guess(10)
