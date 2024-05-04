def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f'expected {expected_result}, got {actual_result}'
    
# test_input_text(11,11)
# test_input_text(8,11)

def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

test_substring('1', '1')
test_substring('some_text', 'some')
# test_substring('fulltext', 'some_value')