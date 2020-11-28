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
        "AccMod": ["ijtemai", "infiradi", "protected", "andruni"],  # Access Modifiers
        "VirOver": ['arzi', 'badlo']  # Virtual Override
    }

    classesSymba = {
        'Not': ['!'],
        "PM": ['+', '-'],  # Plus Minus class
        "MDM": ['*', '/', '%'],  # Binary operator class
        "CompOpr": ["+=", "-=", "*=", "/=", "%="],         # Comparision operator class
        "AssignmentOpr": ['='],  # Assignment operator class,
        "TerminatorOpr": [';'],  # Comparision operator
        "OpenBr":['{'],
        "ClosBr":['{'],
        "OpenPa":['{'],
        "ClosPa":['{'],
        "OpenBr":['{'],
        "OpenBr":['{'],
        "OpenBr":['{'],
        "OpenBr":['{'],
        "OpenBr":['{'],
        'Equal': ['=']
    }

    return [ClassesAlpha,classesSymba]
