from PyChartDataset.dataset import Dataset

def test_dataset_creation_no_data():
    assert Dataset("dataset name").data == []

def test_dataset_length_no_data():
    assert len(Dataset("dataset name")) == 0

def test_dataset_length_5_data():
    test_dataset = Dataset("dataset name")

    for x in range(0, 5):
        test_dataset.append(x)

    assert len(test_dataset) == 5

def test_dataset_data_property_without_data():
    test_dataset = Dataset("dataset name")
    comparison_data = []

    assert test_dataset.data == comparison_data

def test_dataset_data_property_with_data():
    test_dataset = Dataset("dataset name")
    comparison_data = []

    for x in range(0, 5):
        comparison_data.append(x)
        test_dataset.append(x)

    assert test_dataset.data == comparison_data

def test_dataset_clear_no_starting_data():
    test_dataset = Dataset("dataset name")

    assert len(test_dataset) == 0
    test_dataset.clear()
    assert len(test_dataset) == 0

def test_dataset_clear_with_starting_data():
    test_dataset = Dataset("dataset name")

    for x in range(0, 5):
        test_dataset.append(x)

    assert len(test_dataset) == x + 1
    test_dataset.clear()
    assert len(test_dataset) == 0

def test_dataset_append_below_max():
    maximum_length = 10
    test_dataset = Dataset("dataset name", maximum_length)

    assert len(test_dataset) == 0
    test_dataset.append(1)
    assert len(test_dataset) == 1

def test_dataset_append_more_than_max():
    maximum_length = 10
    test_dataset = Dataset("dataset name", maximum_length)

    assert len(test_dataset) == 0

    for x in range(0, maximum_length * 2):
        test_dataset.append(x)

    assert len(test_dataset) == maximum_length