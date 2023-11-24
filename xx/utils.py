def find_solution(split_token, test_data, expected, func):
    
    assert func(test_data.split(split_token)) == expected
    
    with open("input.txt") as file:
        data = file.read()
        
    data = data.split(split_token)

    print(func(data))

