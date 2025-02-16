import pandas as pd
class Univariate:
    def qualQuan(self,dataset):
        qual = []
        quan = []
        for column in dataset.columns:   
            if(dataset[column].dtypes == "object"):
                qual.append(column)
            else:
                quan.append(column)
        return qual,quan

    def getMeanMedianMode(self,dataset,quan):
        tble = pd.DataFrame(index = ["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","Q4:100%","IQR","1.5Rule","Lesser","Greater","Minimum","Maximum"],columns = quan)
        for column in quan:             
            tble[column]["Mean"] = dataset[column].mean() 
            tble[column]["Median"] = dataset[column].median() 
            tble[column]["Mode"] = dataset[column].mode()[0]
            tble[column]["Q1:25%"]  = dataset.describe()[column]["25%"]
            tble[column]["Q2:50%"]  = dataset.describe()[column]["50%"]
            tble[column]["Q3:75%"]  = dataset.describe()[column]["75%"]
            tble[column]["Q4:100%"]  = dataset.describe()[column]["max"]
            tble[column]["IQR"]  = tble[column]["Q3:75%"] - tble[column]["Q1:25%"]
            tble[column]["1.5Rule"]  = 1.5 * tble[column]["IQR"]
            tble[column]["Lesser"]  = tble[column]["Q1:25%"] - tble[column]["1.5Rule"]
            tble[column]["Greater"]  = tble[column]["Q3:75%"] + tble[column]["1.5Rule"]
            tble[column]["Minimum"] = dataset[column].min()
            tble[column]["Maximum"] = dataset[column].max()
        return tble    
 