from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

def EnuRegression(train_x,train_y):
	# Linear Regression
    reg = LinearRegression()
    reg.fit(train_x,train_y)
    
    # Decision Tree Regressor
    Dtree = DecisionTreeRegressor()
    Dtree.fit(train_x,train_y)
    
    # Random Forest Regressor
    
    rf = RandomForestRegressor()
    rf.fit(Train_x,train_y)
