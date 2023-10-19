"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {'Jill':
            {'age':26,
             'job':'biologist',
             'connection':
             {'partner':'John',
              'friend':['Zalika'],
              'landlord': None,
              'cousin':None,     
             }
            },
            'John':
            {'age':27,
             'job':'writer',
             'connection':
             {'partner':'Jill',
              'friend':[],
              'landlord': None,
              'cousin':'Nash',     
             }
            },
            'Zalika':
            {'age':28,
             'job':'artist',
             'connection':
             {'partner': None,
              'friend':['Jill'],
              'landlord': 'Zalika',
              'cousin':None,     
             }
            },
            'Nash':
            {'age':34,
             'job':'Chef',
             'connection':
             {'partner':None,
              'friend':[],
              'landlord': None,
              'cousin':None,     
             }
            },
           }


