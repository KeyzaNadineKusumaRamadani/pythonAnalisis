import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('nilai_siswa.csv')
# data.info()
# print(data.describe())

# print("Rata-rata:", data['Nilai'].mean())
# print("Median:", data['Nilai'].median())
# print("Modus:", data['Nilai'].mode()[0])

# Matematika = data[data['Matpel'] == 'Matematika']
# print(Matematika)

# data.groupby('Matpel')['Nilai'].agg(['max','min'])

# rata = data.groupby('Matpel')['Nilai'].mean()
# rata.plot(kind='bar', color=["blue", "orange", "green"])
# plt.title('Rata-Rata Nilai per Mapel')
# plt.xlabel('Mata Pelajaran')
# plt.ylabel('Nilai Rata-Rata')
# plt.tight_layout()
# plt.show()

sns.boxplot(x='Matpel', y='Nilai', data=data, palette=['red', 'blue', 'pink'])
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.tight_layout()
plt.show()