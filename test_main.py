from main import documents, directories, add_element, delete, search_name, search_shelf


def test_search_shelf():
    expected_result = '1'
    assert search_shelf(directories, '11-2') == expected_result


def test_search_name():
    expected_result = 'Геннадий Покемонов'
    assert search_name(documents, '11-2') == expected_result


def test_add_element():
    add_element(directories, documents, '1', '1', '1', '3')
    assert '1' in directories['3']


def test_delete():
    delete(directories, documents, '11-2')
    assert '11-2' not in directories['1'], documents[1]
