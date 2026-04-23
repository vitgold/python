"""
0402_match_case
"""

value = 2
match value:
    case 1:
        print("one")
    case 2:
        print("two")
    case _:
        print("other")
        
        
if value == 1:
    print("one")
elif value == 2:
    print("two")
else:
    print("other")
    
    
# command = input("Enter command: ")  

# match command:
#     case "start":
#         print("Запуск")
#     case "stop":
#         print("Остановка")
#     case _:
#         print("Команда не распознана")
        
match value:
    case 1 | 2 | 3:
        print("123")
    case 4 | 5 | 6:
        print("456")
    case _:
        print("other")
        
match value:
    case x:
        print(x)
        
# частичное сопотавление



x = 10
match x:
    case n if n > 5: 
        print("n > 5")
    case _:
        print("other")
        
        
match value:
    case int():
        print('intint')
    case float():
        print('floatfloat')