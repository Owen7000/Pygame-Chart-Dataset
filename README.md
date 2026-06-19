# Pygame Chart Dataset
![GitHub top language](https://img.shields.io/github/languages/top/owen7000/Pygame-Chart-Dataset?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/owen7000/Pygame-Chart-Dataset?style=for-the-badge)

A dataset helper class for Pygame-Chart charts

## Usage
Usage of the dataset is as follows
```py
from PyChartDataset.dataset import Dataset

ds = Dataset("Test Dataset")

ds.append(1) # The dataset now contains [1]
ds.append(2) # The dataset now contains [1,2]

print(len(ds)) # Output: 2
print(ds.data) # Output: [1,2]

ds.clear() # The dataset now contains []

```

And that's it!
More documentation will be available soon.