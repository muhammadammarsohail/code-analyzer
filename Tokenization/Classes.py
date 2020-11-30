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
        'AndOr': ['aur','ya'],
        "BrkCont": ['roko', 'jari'],  # Break Continue
        "DataType": ["int", "float", "bool", "string", "char"],  # Data types
        "AccMod": ["ijtemai", "infiradi", "protected", "andruni"],  # Access Modifiers
        "VirOver": ['arzi', 'badlo'],  # Virtual Override
        "Extends": ['extends']
    }

    classesSymba = {
        'Not': ['!'],
        "PM": ['+', '-'],  # Plus Minus class
        "MDM": ['*', '/', '%'],  # Binary operator class
        "CompOpr": ["+=", "-=", "*=", "/=", "%="],         # Comparision operator class
        "Equal": ['='],  # Assignment operator class,
        "IncOp": ['+o','-o'],
        "TerminatorOpr": [';'],  # Comparision operator
        "Comma":[','],
        "Dot":['.'],
        "OpenBr":['{'],
        "ClosBr":['}'],
        "OpenPa":['('],
        "ClosPa":[')'],
        "OpenSq":['['],
        "ClosSq":[']'],
        'Equal': ['=']
    }

    return [ClassesAlpha,classesSymba]
