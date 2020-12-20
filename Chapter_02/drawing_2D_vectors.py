# coding = <utf-8>

import sys
import os 
import os.path as osp 
import logging 
from math import sqrt, log
import argparse
from pathlib import Path
sys.path.insert(0, osp.abspath(__file__))


import coloredlogs
import numpy as np 
from scipy import stats
import matplotlib.pyplot as plt


coloredlogs.install(level="INFO", fmt="%(asctime)s %(filename)s %(levelname)s %(message)s")

savePath = osp.join(os.getcwd(), "outputs")
SAVE_DIR = Path(savePath)
SAVE_DIR.mkdir(parents=True, exist_ok=True)





def picturing_2d_vectors():
    logging.info('2.1 Picturing 2D Vectors')
    from vector_drawing import draw, Points, Segment, Polygon
    
    dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
                    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
                    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1) 
                    ]

    draw( Points(*dino_vectors),  save_as="outputs/01_2D_vectors.svg" )

    draw( Points(*dino_vectors),  Segment((6,4),(3,1)), 
        save_as="outputs/02_2D_vector_segment.svg" 
        )

    draw(   Points(*dino_vectors),    
            Polygon(*dino_vectors),
            save_as="outputs/03_2D_vector_polygon.svg"
        )
    
    plt.close()

    draw(  Points(*[(x,x**2) for x in range(-10,11)]),
            grid=(1,10),
            nice_aspect_ratio=False,  # don't require x scale to match y scale
            save_as="outputs/04_2D_vector_convex.svg"
        )

    plt.close()



def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def plane_vector_arithmetic():
    logging.info('2.2 Plane Vector Arithmetic')
    from vector_drawing import draw, Points, Polygon,  Segment
    
    blue = 'C0'
    red = 'C3'
    black = 'k'

    dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
                    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
                    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1) 
                    ]    

    dino_vectors2 = [ add((-1.5,-2.5), v) for v in dino_vectors ]

    draw(   Points(*dino_vectors, color=blue),
            Polygon(*dino_vectors, color=blue),
            Points(*dino_vectors2, color=red),
            Polygon(*dino_vectors2, color=red),
            
            save_as="outputs/05_plane_vector.svg"
        )

    arrows = [Segment(tip,tail,color=black) for (tip,tail) in  zip(dino_vectors2, dino_vectors)]

    draw(   Points(*dino_vectors, color=blue),
            Polygon(*dino_vectors, color=blue),
            Points(*dino_vectors2, color=red),
            Polygon(*dino_vectors2, color=red),
            *arrows,
            
            save_as="outputs/06_plane_vector_segment.svg"
        )

    plt.close()



def length(v):
    return sqrt(v[0]**2 + v[1]**2) 

def vector_component_and_length(): 
    logging.info('2.3 Vector components and lengths')
    from vector_drawing import draw, Points, Segment

    red = 'C3'

    draw(   Points((2,2), (-1,3)),
            Segment((2,2), (-1,3), color=red), 
            save_as="outputs/07_segment.svg"
        )

    plt.close()


def addVec(*vectors):
    return (sum([v[0] for v in vectors]), sum([v[1] for v in vectors]))

def translate(translation, vectors):
    return [add(translation, v) for v in vectors]



def hundred_dinos():
    logging.info('2.4 hundred_dinos')
    from vector_drawing import draw, Points, Segment, Polygon

    blue = 'C0'

    dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
                    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
                    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1) 
                    ]    

    translations = [(12*x,10*y) 
                    for x in range(-5,5) 
                    for y in range(-5,5)]
    dinos = [Polygon(*translate(t, dino_vectors),color=blue)
                for t in translations]
    draw(*dinos, grid=None, axes=None, origin=None, 
    
            save_as="outputs/08_hundred_dinos"
        )

    plt.close()



if __name__ == "__main__":

    picturing_2d_vectors()
    plane_vector_arithmetic()
    vector_component_and_length()

    hundred_dinos()