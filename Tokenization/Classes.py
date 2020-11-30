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
        'And': ['aur'],
        'Or': ['ya'],
        "BrkCont": ['roko', 'jari'],  # Break Continue
        "DataType": ["int", "float", "bool", "string", "char"],  # Data types,
        "Keyword": ["main", "class", "return", "function"],  # Keywords
        "AccMod": ["ijtemai", "infiradi", "protected", "andruni"],  # Access Modifiers
        "VirOver": ['arzi', 'badlo'],  # Virtual Override
        "Extends": ['extends']          #for inheritance
    }

    classesSymba = {
        'Not': ['!'],
        "PM": ['+', '-'],  # Plus Minus class
        "MDM": ['*', '/', '%'],  # Binary operator class
        "ComAssi": ["+=", "-=", "*=", "/=", "%="],         # Compound Assignment operator
        "RelOp": ['>','<','>=','<=','!=','=='],          #Relational Operators
        "Equal": ['='],  # Assignment operator class,
        "IncOp": ['+o','-o'],   # increment and decrement
        "TerOpr": [';'],        #End of Statement
        "Comma":[','],
        "Dot":['.'],
        "OpenBr":['{'],
        "ClosBr":['{'],
        "OpenPa":['{'],
        "ClosPa":['{']
        
    }

    return [ClassesAlpha,classesSymba]
