



ivan = { 'height':
             { 'me': ["186"],
               'my_sister': ['180'],
               'wife': ['173']

},
        'favourite': {'me': ['koffee'],
                      'my_sister': ['milk'],
                      'wife': ['mountains']

         },
         'color': {
             'me': ['green'],
             'my_sister': ['blue'],
             'wife': ['red']

         },

}
def main():

    try:
        ivan_names = list(ivan.keys())
        for t, l in enumerate(ivan_names):
            print(f'{t}. {l}')


        m = int(input('what information would you like to know. please select from the list above: '))
        if m == 0:
            m = 'height'
        elif m == 1:
            m = 'favourite'
        elif m== 2:
            m = 'color'
        else:
            print('this is not a valid number')

        outcome = ivan.get(m)
        outcome = dict(outcome)

        if m == 'height':
            check_height(m, outcome)
        elif m == 'favourite':
            check_favourite(m, outcome)
        elif m == 'color':
            check_color(m, outcome)
    except ValueError as ve:
        print(f'please enter a valid number! {ve} is not a number')
    except TypeError:
        print('please enter a correct number')





def check_height(m, outcome):

    for idx, m in enumerate(outcome.keys(), start=1):
        t = 0
        print(f'{idx}. {m}')

    k = int(input('whos height you would like to check: '))
    if k == 1:
        idx = k-1
        x = list(outcome.values())
        print(f'ivan is {x[idx]}height')

    elif k == 2:
        idx = k-1
        m = list(outcome.values())

        print(f'his sister is {m[idx]}height')

    elif k == 3:
        idx = k-1
        z = list(outcome.values())
        print(f'his wife is {z[idx]}height')



def check_favourite(m, l):

    for idx, m in enumerate(l.keys()):
        t = 0
        print(f'{idx}. {m}')
    k = int(input('whos favourite you would like to check: '))
    if k == 1:
        idx = k-1
        x = list(l.values())
        print(f'ivan`s favourite is: {x[idx]}. mmmmmm')
    elif k == 2:
        idx == k-1
        m = list(l.values())
        print(f'ivan`s sister favourite is: {m[idx]}')
    elif k == 3:
        idx ==k-1
        z = list(l.values())

        print(f'ivan`s wife favourite is, {z[idx]} climbing')

def check_color(m, outcome):

    for idx, m in enumerate(outcome.keys()):
        print(f'{idx}. {m}')
        t = 0
    k = int(input('whos color you would like to check: '))

    if k == 1:
        idx = k-1
        x = list(outcome.values())
        print(f'ivan loves {x[idx]}')
    elif k == 2:
        idx = k-1
        m = list(outcome.values())

        print(f'my sister loves {m[idx]}')
    elif k == 3:
        idx = k-1
        z = list(outcome.values())

        print(f'my wife loves {z[idx]}')


if __name__ == '__main__':
    main()