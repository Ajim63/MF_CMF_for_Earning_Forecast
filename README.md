# Are missing values important for earnings forecast? a machine learning perspective
This is an example code for Matrix Factorization and Coupled Matrix Factorization proposed in the paper: 
`Are missing values important for earnings forecast? a machine learning perspective` forthcoming in the Quantitative Finance (https://www.tandfonline.com/toc/rquf20/current)

### **Requirments** 
- numpy >= 1.19
- pandas >= 1.0.1
- sckitlearn >= 0.22.0
- matplotlib >= 3.1.0
- tensorflow == 2.5.0
- keres == 2.3.1



## File Description 
### Data 
The quarterly  financial analysts' forecast of earnings per share (EPS) data is collected from
I/B/E/S, Thomson Reuters. We consider the time from quarter 1, 2000 to quarter 4, 2016. We perform some filtering procedures
1. we only select  firms that appear at least 48 quarters out of the total 68 quarters, which allows us to have sufficient historical records. 
2. we remove  rms with less than ten di erent analysts during the sample period. 
3. we remove analysts who make less than three forecasts in the considered period. 
The  final sample involves 2082 firms and 9785 analysts.

Beacuese this data is propreitory we provided the code with example for only one firm 'Apple Inc' (AAPL). The full data can be accessed from here with a subscription https://wrds-www.wharton.upenn.edu/pages/get-data/ibes-thomson-reuters/ 

The Sample Data used for this code example is available in folder [Data](Data). The csv file [AAPL.csv](Data/AAPL.csv) have the data for anlysts EPS forecast.  The csv file [AAPL_char.csv](Data/AAPL_char.csv) have the data for APPLE firm characteristics, used for CMF. 


### utils
All python codes for all the defination and the imputation models used in the paper are available in the folders [utils](utils)



## Matrix Factorization
The IPython notebook [MF.ipynb](MF.ipynb) provide an example and result comparison for Matrix factorization model proposed in the paper. 






## Coupled Matrix Factorization
The IPython notebook [CMF.ipynb](CMF.ipynb) provide an example and result comparison for Coupled Matrix factorization model proposed in the paper. 








