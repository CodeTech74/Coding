import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset('Titanic')
sns.barplot(x = "who", y = "fare", data = df)
plt.show()