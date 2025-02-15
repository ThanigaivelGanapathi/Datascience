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
        tble = pd.DataFrame(index = ["Mean","Median","Mode"],columns = quan)
        for column in quan:             
            tble[column]["Mean"] = dataset[column].mean() 
            tble[column]["Median"] = dataset[column].median() 
            tble[column]["Mode"] = dataset[column].mode()[0]
        return tble    