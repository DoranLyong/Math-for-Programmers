# coding = <utf-8>

import sys
import os 
import os.path as osp 
import logging 
from math import sqrt, log
import argparse
from pathlib import Path
#sys.path.insert(0, osp.abspath(__file__))


import coloredlogs
import numpy as np 
from scipy import stats
import matplotlib.pyplot as plt


coloredlogs.install(level="INFO", fmt="%(asctime)s %(filename)s %(levelname)s %(message)s")

savePath = osp.join(os.getcwd(), "outputs")
SAVE_DIR = Path(savePath)
SAVE_DIR.mkdir(parents=True, exist_ok=True)




def market_movements():
    logging.info('1.1.1 Predicting financial market movements')

    """ input data 
    """

    ys = [30] # initial_position
    xs = range(0, 501)  #  0, 1, ..., 500

    np.random.seed(seed=42)   # 국룰 시드 42 

    for delta in np.random.normal(0, 0.5, 500):  # (mean=0, std=0.5) @sampling 500  
        ys.append(ys[-1] + delta) 

    plt.plot(xs, ys, 'tab:blue')
    plt.ylabel('Stock Price ($)')
    plt.xlabel('Elapsed Time (min)')
    plt.savefig("outputs/01_stock_price_over_time.svg")  # (ref) svg  vs. png: https://ithub.tistory.com/75



    """ Linear regression 
    """
    r = stats.linregress(xs, ys)  # (ref) https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html
    line = [r.slope * x + r.intercept for x in xs]  # Y = aX + b

    std = np.std( [(y-y0) for y,y0 in zip(ys,line)] )   # ground_truth - prediction 

    top = [y + std for y in line]
    bottom = [y - std for y in line]

    plt.plot(xs, ys, 'tab:blue')    # true line 
    plt.plot(xs, line, 'r')  # regression line 
    plt.plot(xs, top, 'g')   # top line 
    plt.plot(xs, bottom, 'm')# bottom line 
    plt.ylabel('Stock Price ($)')
    plt.xlabel('Elapsed Time (min)')
    plt.savefig('outputs/02_regression.svg')


    plt.annotate('Buy here', xy=(280, 27), xytext=(300, 24),
            arrowprops=dict(facecolor='black', shrink=0.05))         # (ref) https://matplotlib.org/3.3.3/tutorials/text/annotations.html
    plt.annotate('Sell here', xy=(330, 33.5), xytext=(300, 36),
            arrowprops=dict(facecolor='black', shrink=0.05))         # (ref) https://matplotlib.org/3.3.3/tutorials/text/annotations.html
    plt.savefig('outputs/03_regression_anno.svg')
    
    plt.close()



def price(mileage): 
    """ See the equation in the book at page 6.
    """
    return 26500 * (0.905 ** mileage) 

def finding_good_deal():
    logging.info('1.1.2 Finding a good deal')

    """ input data 
    """
    mileages = [4.1429, 8.9173, 6.5, 6.0601, 12.3, 6.2, 2.5782, 0.9, 1.7, 13.1045, 24.7, 9.2699, 17.2, 10.0, 10.0, 2.8, 12.3773, 19.6, 7.3397, 2.1178, 12.9886, 10.9884, 16.9, 6.0, 12.9, 8.1936, 10.5, 8.0713, 1.7, 10.0, 15.6097, 17.0, 16.7, 5.6, 11.3, 19.9, 9.6, 21.6, 20.3]
    prices = [16980.0, 15973.0, 9900.0, 15998.0, 3900.0, 12540.0, 21688.0, 17086.0, 23000.0, 8900.0, 3875.0, 10500.0, 3500.0, 26992.0, 17249.0, 19627.0, 9450.0, 3000.0, 14999.0, 24990.0, 7967.0, 7257.0, 4799.0, 13982.0, 5299.0, 14310.0, 7800.0, 12250.0, 23000.0, 14686.0, 7495.0, 4950.0, 3500.0, 11999.0, 9600.0, 1999.0, 4300.0, 3500.0, 4200.0]


    xs = np.linspace(0, 25, 100)  # from 0 to 25  @sampling 100
    ys = [price(mileage) for mileage in xs]

    plt.scatter(mileages,prices) 
    plt.plot(xs,ys, color='C1')   # (ref) https://matplotlib.org/2.0.2/users/colors.html

    plt.xlabel('Mileage (10,000s of miles)')
    plt.ylabel('Price ($)')
    plt.savefig('outputs/04_price_mileage.svg')



    """ Expectation 
    """ 
    target_mileage = log(10/26.5)/log(0.905)

    xlim,ylim = plt.xlim(), plt.ylim()

    plt.plot([-5,30],[10000,10000],color="gray",linestyle="dashed")
    plt.plot([target_mileage,target_mileage],[-5000,10000],color="gray",linestyle="dashed")
    plt.xlim(*xlim)
    plt.ylim(*ylim)

    plt.annotate('Expected mileage', xy=(9, 3000), xytext=(0, 3000),
            arrowprops=dict(facecolor='black', shrink=0.05))            
    plt.annotate('My budget', xy=(20, 10000), xytext=(20, 20000),
            arrowprops=dict(facecolor='black', shrink=0.05))            

    plt.savefig('outputs/05_price_mileage_expect.svg')
    plt.close()



def building_3D_graph():
    sys.path.append('../Chapter_03')
    from draw3d import draw3d , Polygon3D, Points3D

    triangle = [(2.3,1.1,0.9), (4.5,3.3,2.0), (1.0,3.5,3.9)]

    draw3d( 
    Polygon3D(*triangle),
    Points3D(*triangle),
    axes=False,
    origin=False, 
    save_as = "outputs/06_3D_triangle.svg")

    plt.close()



if __name__ == "__main__":


    market_movements()
    finding_good_deal()
    building_3D_graph()