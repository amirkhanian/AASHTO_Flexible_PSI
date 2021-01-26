# AASHTO_Flexible_PSI
Present serviceability index nomograph for the PSI equation in the original AASHO Road Test report. This is for flexible pavements. The basis equation is found on pages 14 and 23 of the Highway Research Board Special Report 61E (1962).

The scales for each of the parameters can be changed via the "u_min" and "u_max" values. The isopleth can be changed to create any example by modifying the "isopleth_values" array. The order of the isopleth values is the order of the variables shown in the "f_params" line. Simply put an 'x' where you want the code to solve.

# Requirements

In addition to Python, this requires the [PyNomo library](https://github.com/lefakkomies/pynomo).
