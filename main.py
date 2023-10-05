from modules import encounter

count = 20

while True:
    test = encounter.test_encounter('colina','normal','beginner', 'extreme')
    if count > 0:
        print(test)
        print('')
        count = count-1
    else:
        break
