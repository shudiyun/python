# re-position

By taking 3 reference points we are able to define points on a plane. Then these points can be re-found by re-defining the position of the reference point if
the sample is displaced from its initial position.

## TrackOverlap

This Directory contains a script *scikit.py* that is capable of taking 2 images and overlap them over different color channels.
At the moment the script need major improvements but it works if the overlapping images are called:
	
	* "number"_Cell.tif
	* "number"_Neutron.tif

So to run the script you need to know the directory where the images are stored and the **number** of the images to overlap:

``` 
python scikit.py /path/to/img number
```
