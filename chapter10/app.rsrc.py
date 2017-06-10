{'application':{'type':'Application',
          'name':'Minimal',
    'backgrounds': [
    {'type':'Background',
          'name':'bgMin',
          'title':'Apartment Complex List',
          'size':(729, 639),

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit\tAlt+X',
                   'command':'exit',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'StaticText', 
    'name':'stest', 
    'position':(318, 85), 
    'text':'StaticText', 
    'visible':False, 
    },

{'type':'Button', 
    'name':'bsubmit', 
    'position':(120, 231), 
    'label':'Submit', 
    },

{'type':'StaticText', 
    'name':'sroom', 
    'position':(45, 189), 
    'font':{'style': 'bold', 'faceName': u'Sans', 'family': 'sansSerif', 'size': 12}, 
    'text':'Room:', 
    },

{'type':'TextField', 
    'name':'room', 
    'position':(120, 181), 
    },

{'type':'StaticText', 
    'name':'title', 
    'position':(210, 13), 
    'font':{'style': 'bold', 'faceName': u'Sans', 'family': 'sansSerif', 'size': 14}, 
    'text':'Apartment Complex Check in', 
    },

{'type':'TextField', 
    'name':'lname', 
    'position':(120, 128), 
    'size':(170, 31), 
    },

{'type':'StaticText', 
    'name':'slname', 
    'position':(9, 140), 
    'font':{'style': 'bold', 'faceName': u'Sans', 'family': 'sansSerif', 'size': 12}, 
    'text':'Lastname:', 
    },

{'type':'StaticText', 
    'name':'sfame', 
    'position':(7, 85), 
    'font':{'style': 'bold', 'faceName': u'Sans', 'family': 'sansSerif', 'size': 12}, 
    'text':'Firstname:', 
    },

{'type':'TextField', 
    'name':'fname', 
    'position':(121, 78), 
    'size':(170, 31), 
    },

] # end components
} # end background
] # end backgrounds
} }
