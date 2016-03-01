
import os
import sys
import time
import imageio
import numpy as np

def reflect(filename):
    # Get filenames
    filename1 = filename
    base, ext = os.path.splitext(filename)
    filename2 = base + '_reflected' + ext
    # Get images 
    im1 = imageio.imread(filename)
    im2 = reflect_image(im1)
    # Write back
    imageio.imsave(filename2, im2)


def reflect_image(im1, distance=0, startAlpha=0.20, N=80):
    
    # Initialize im2
    shape = list(im1.shape)
    shape[0] *= 2
    im2 = np.zeros(shape, im1.dtype)
    im2[:im1.shape[0],:im1.shape[1],:] = im1
    
    y2_max = 0    
    for x in range(im1.shape[1]):
        
        # Search start of column
        y = im1.shape[0]
        while True:
            y -= 1
            if y<0:
                break
            if im1[y,x,3] > 0:
                break
        y0 = y
        if not y0:
            continue
        
        # Reflect
        for y in range(N):
            y1 = y0-y-bool(not distance)
            y2 = y0+y+distance
            im2[y2,x,:] = im1[y1,x,:]
            im2[y2,x,3] *= startAlpha * (1.0-float(y/N))
        y2_max = max(y2_max, y2)
    
    # Return im2, cropped appropriately
    return im2[:y2_max,:shape[1],:]


if __name__ == '__main__':
    filename = '/home/almar/projects/www/pyzo-www/wwwpyzo/_static/pyzo_box.png'
        
    im1 = imageio.imread(filename)
    im2 = reflect_image(im1)
    
    import visvis as vv
    vv.clf()
    vv.subplot(121); vv.imshow(im1)
    vv.subplot(122); vv.imshow(im2)
    
   # reflect(filename)