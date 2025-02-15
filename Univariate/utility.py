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