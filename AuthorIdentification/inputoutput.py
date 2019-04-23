#input-output test

def input_output(input_test):
    test_text = input_test
    test_output=""

    if 'baobao' in test_text:
        test_output='baobao is very good'
    elif 'lulu' in test_text:
        test_output='lulu is nice'
    elif 'love' in test_text:
        test_output='baobao love lulu and lulu love baobao'
    else:
        test_output='test response is none'
    
    return test_output