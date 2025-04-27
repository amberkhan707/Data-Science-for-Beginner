# statistical analysis of data
import pandas as pd


#######################################################################

#correlations for a dataframe

df1 = pd.DataFrame([(18, 118,45), (18,120,42),(19, 132,46), (18,109,44),
                    (17,110,42),(17, 115,50), (20, 141,46),(21,135,47),
                    (21,143,42),(17,130,44),(19,128,45),(20,130,48)],
                    columns=['age', 'height', 'weight'])
print("\nData is ")
print(df1)
print()

correlations = df1.corr(method='pearson')
print(correlations)



####################################################################



# csv file does not contain the column header. Hence define it.
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

# read data
print("Reading Data from csv file")
data = pd.read_csv("pima-diabetes-data.csv", names=names)

print("Data Snapshot")
print(data.head(5))
print()


#########################################################################

# correlation between columns
# Pearson correlation
# value between -1 and +1. value = 0 means no correlation
# negative values = negative correlation
# positive values means positive correlation

print("\nPearson Correlation output")
correlations = data.corr(method='pearson')
print(correlations)
print()

input("Press Enter")
# plotting the correlations
import matplotlib.pyplot as plt

# plot correlation results
fig = plt.figure()
ax = fig.add_subplot(111)   # create a sub plot

#Plot the values of a 2D matrix or array as color-coded image.
cax = ax.matshow(correlations, cmap='coolwarm', vmin=-1, vmax=1)
# Add a colour bar next to the plot
fig.colorbar(cax)
# add other features of the plot
ax.set_title("Correlation Plot")
ticks = range(0,len(data.columns),1)
ax.set_xticks(ticks)
#plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(data.columns)
ax.set_yticklabels(data.columns)
plt.show()

input("Press Enter to continue")


