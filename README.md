# GlitchEffect
<p>
    <img src="demo.jpg" width="400"> <img src="ChannelShiftGlitch.jpg" width="400">
    <img src="LineShiftGlitch.jpg" width="400"> <img src="MatrixGlitch.jpg" width="400">
</p>
<p style="text-align:justify">
    Due to singal interference or damaged singal, its quantized Image is changed in terms of color channels shift, Row Stripes in Images and sometimes pattern is seen over Image. we can create those effect after Quantized Image. these kind of effect is used by many social apps such as Facebook, SnapChat or Other Social platforms
</p>

## How to make these glitch Effects
## Four glitches, I made through image processing
1. ChannelShift glitch
2. LineShift glitch
3. MatrixShift glitch

<article>

### Channel Shift glitch

Image is basically replica of real wolrd object. Computer used colorspaces to represent images. these color spaces are RGB,YUV and HSV or anyother. Most famus colorspaced is RGB. Image is represented in three color channels namely Red, Green and Blue.

So Basically we shift each channel in X and Y Direction so It Creates an effect of glitch.
<p align="center">
    <img src="demo.jpg" width="400"> <img src="ChannelShiftGlitch.jpg" width="400">
</p>
<h4 align="center">Figure 1: Original Image to Channel shift glitch</h4>

Image is basically three dimensional matrix. 
1.first dimension represents rows of image.
1.second dimension represents column of image.
1.third dimension reprents RGB Color of Image, O=> Red, 1=> Green, 2=> Blue But it is up to which library you used.

CoreLogic:
<pre>
    So if our image Matrix 'Img' has size of m x n x c  where m = number of rows, n = number of column and c = number of channel
    then to shift channels is be like:
        Img[][][0] = Img[][][0] + OffsetOfRow + OffsetofColumn //For Red Channel
        Img[][][1] = Img[][][1] + OffsetOfRow + OffsetofColumn //For Blue Channel
    
    Never Touch third channel, it automatically create glitch effect.
</pre>
for More understanding check the code:<br>
ChannelShiftGlitch.py file<br><br>
To run file:-<Br>
<code>
    python ChannelShiftGlitch.py
</code>
</article>

<article>

### Row shift glitch

AS previously mentioned, Image is matrix with rows, columns and color channel so there is another glitch made possible when image's rows are shifted bit as signal can be shift or lossed.

So Basically we shift random rows in X Direction so It Creates an effect of glitch.
<p align="center">
    <img src="demo.jpg" width="400"> <img src="LineShiftGlitch.jpg" width="400">
</p>
<h4 align="center">Figure 2: Original Image to Line shift glitch</h4>

CoreLogic:
<pre>
    So if our image Matrix 'Img' has size of m x n x c  where m = number of rows, n = number of column and c = number of channel
    then to shift rows in x direction is be like:
        
        n = random_numer of rows shift
        repeat
        
            x = any row of image randomly choosed
            Img[x][][] = Img[x][][] + OffsetofColumn //For Red Channel
        
        until n rows are shifted

</pre>
for More understanding check the code:<br>
LineShiftGlitch.py<br><br>
To run file:-<br>
<code>
    python LineShiftGlitch.py
</code>

</article>

<article>

### Matrix Noise glitch

AS previously mentioned, Image is matrix with rows, columns and color channel so there is another glitch made possible when whole image is interfered with some other signal so all bits are altered bit.

So Basically we add random number of bytes to Original Image so It Creates an effect of glitch.
<p align="center">
    <img src="demo.jpg" width="400"> <img src="MatrixGlitch.jpg" width="400">
</p>
<h4 align="center">Figure 3: Original Image to Matrix glitch</h4>

CoreLogic:
<pre>

    So if our image Matrix 'Img' has size of m x n x c  where m = number of rows, n = number of column and c = number of channel
    then to shift rows in x direction is be like:
        
    Noise[][][] = Random bytes taken from memory
    Img[][][] = (Img[][][] * SingalStrength + Noise[][][]) / (SingalStrength - 1) + 2 //For Red Channel

    There is SignalStrenght variable which decides how much noise should be added to original Image.

</pre>
for More understanding check the code:<br>
MatrixGlitch.py<br><br>
To run file:-<Br>
<code>
    python MatrixGlitch.py
</code>

</article>

