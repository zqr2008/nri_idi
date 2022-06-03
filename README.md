### It is a python package for NRI(net reclassification imporvement) and IRI(Integrated Discrimination Improvement)
It is a package built for the purpose of calculating Net Reclassification Indices(NRI) and Integrated Discrimination Improvement(IRI) 



The ``nri`` function does all the math. You can import ``nri`` function from ``nri_f.py``. And use it as the following:

``nri(df,"old_model","new_model","gold_std")
``
###  where :
>        example (dataframe): dataframe contains all information
        
>        old (string): the colunm name of the old model prediction 
>        new (string): the colunm name of the new model prediction 
>        gold (string):  the colunm name of the real status 
        
It will return the calculated result：

![1654231056(1)](https://user-images.githubusercontent.com/73268508/171787186-c5357dd2-c2c6-4cdc-9f06-e36003eb0077.png)
![1654231065(1)](https://user-images.githubusercontent.com/73268508/171787198-9f49d835-0c82-4598-8981-670785ac5c3e.png)
