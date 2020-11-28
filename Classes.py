def Classes():
    ClassesAlpha = {
        "Void": ['void'],
        "While": ['jabtak'],
        "If": ['agar'],
        'Else': ['warna'],
        'Return': ['return'],
        'Main': ['main'],
        'Class': ['class'],
        'New': ['naya'],
        'Abstract': ['passive'],
        'Or': ['ya'],
        'And': ['aur'],
        "BrkCont": ['roko', 'jari'],  # Break Continue
        "DataType": ["int", "float", "bool", "string", "char"],  # Data types,
        "Keyword": ["main", "class", "return", "function"],  # Keywords
        # Access Modifiers
        "AccMod": ["ijtemai", "infiradi", "protected", "andruni"],
        "VirOver": ['arzi', 'badlo']  # Virtual Override
    }

    classesSymba = {
        'Not': ['!'],
        "PM": ['+', '-'],  # Plus Minus class
        "MDM": ['*', '/', '%'],  # Binary operator class
        # Comparision operator class
        "CompOpr": ["+=", "-=", "*=", "/=", "%="],
        "AssignmentOpr": ['='],  # Assignment operator class,
        "TerminatorOpr": [';'],  # Comparision operator
        "Punc": [''],
        'Equal': ['=']
    }

    return [ClassesAlpha,classesSymba]
